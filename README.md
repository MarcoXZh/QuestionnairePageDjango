# QuestionnairePageDjango

A single page to provide questionnaire and collect answers

## Usage

1. This is developed with [`Django`][django] under [`virtualenv`][venv] of
   Python3, so the prerequisites include:

   - Install Python3:

     ```bash
     sudo apt install python3 python3-pip
     ```

   - install and activate `virtualenv` (optional):

     ```bash
     sudo pip install virtualenv
     virtualenv -p python3 ~/python3
     source ~/python3/bin/activate
     ```

   - and install `Django`:

     ```bash
     pip install django
     # or
     pip install -r requirements.txt
     ```

2. Run the sever:

   - Setup the database. A SQLite database is used for demo only, to initialize
     database tables and some data (questions), follow:

     ```bash
     python manage.py migrate           # Create tables
     python insert_sample_questions.py  # Inject sample questions
     ```

   - Startup the server:

     ```bash
     python manage.py runserver
     ```

   - Open the link http://localhost:8000/ to see the page and conduct the
     questionnaire.

[django]: https://www.djangoproject.com/
[venv]: https://virtualenv.pypa.io/en/stable/
