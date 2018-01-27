# QuestionnairePageDjango

A single page to provide questionnaire and collect answers

## Usage

1. This is developed with [`Django 2.0.1`][django] under [`virtualenv`][venv] of
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

   - and install `Django 2.0.1`:

     ```bash
     pip install django==2.0.1
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
     python manage.py runserver 0.0.0.0:8000
     ```

   - Open the link http://localhost:8000/ to see the page and conduct the
     questionnaire.

   - To allow access from outside, set firewall to allow port 80:

     ```bash
     sudo ufw enable
     sudo ufw allow port 8000
     sudo ufw reload
     sudo ufw status

     # The following should be in the output:
     #    8000                       ALLOW       Anywhere
     #    8000 (v6)                  ALLOW       Anywhere (v6)
     ```


[django]: https://www.djangoproject.com/
[venv]: https://virtualenv.pypa.io/en/stable/
