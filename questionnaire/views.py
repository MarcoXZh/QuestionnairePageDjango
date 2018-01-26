from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Question, Questioner
import json, random


# path('', views.index, name='index')
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        # Prepare data - randomly pick 12 questions from question base
        questions = Question.objects.all()
        ids = list(range(len(questions)))
        random.shuffle(ids)
        qs = [{ 'id':idx, 'number':i+1, 'text':questions[idx].text}
                for i, idx in enumerate(ids[:12])]

        # Render the page with data
        return render(request, 'index.html',
                      { 'title':'Questionnaire', 'questions': qs })
    else:   # if request.method == 'POST'
        try:
            # Prepare data - find if the name exists
            name = None
            answers = {}
            for k, v in request.POST.items():
                if k == 'name':
                    name = v.strip()
                elif k.startswith('answer'):
                    answers[int(k.split('-')[-1].split(']')[0])] = v.strip()
                # if ... - elif
            # for k, v in request.POST.items()
            if name == '':
                name = 'Guest'
            # if name == ''
            questioners = Questioner.objects.all()
            names = [q.name for q in questioners]
            if name in names:
                cnt = 1
                while '%s-%d' % (name, cnt) in names:
                    cnt += 1
                # while '%s-%d' % (name, cnt) in names
                name = '%s-%d' % (name, cnt)
            # if name in names

            # Save database
            q = Questioner(name=name, answers=json.dumps(answers))
            q.save()

            # Respond to web page
            return HttpResponse(json.dumps({ 'post_status':'Succeed' }),
                                content_type='application/json')
        except Exception as err:
            return HttpResponse(json.dumps({ 'post_status':'Fail - %s' % str(err) }),
                                content_type='application/json')
        # try - except Exception as err
    # else - if request.method == 'GET'
# def index(request)
