## Design outlines

- A web server designed by **Python3/Django** supports the questionnaire page.
- The **SQLite database engine** is employed to minimize prerequisites.
- The page uses **Bootstrap 4** and consequently **JQuery 3** in design.
- Only **minial theme** (some paddings and margins) added due to the web site
  context not available.
- Other pages such as `'^questions$'` or `'^answer/<slug:voter>$'` are designed
  to be servable however omitted.
- Developed in Ubuntu 16.04 LTS and tested in Windows 10.

## Usage

1. Install Python3, `virtualenv` (optional) and `Django 2.0.1`:
   ```bash
   sudo apt install python3 python3-pip
   sudo pip install virtualenv
   virtualenv -p python3 ~/python3
   source ~/python3/bin/activate
   pip install django==2.0.1
   ```

2. Set up database. A SQLite database is used for demo only, to initialize
   database tables and some data (questions), follow:
   ```bash
   cd ~/QuestionnairePageDjango
   python manage.py migrate           # Create tables
   python insert_sample_questions.py  # Inject sample questions
   ```

3. Startup the server:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   Now open the link http://localhost:8000/ to see the page and conduct the
   questionnaire.

4. Enable firewall to allow access from outside (optional for demostration):
   ```bash
   sudo ufw enable
   sudo ufw allow 8000
   sudo ufw reload
   sudo ufw status
   ```

## Screenshots

![The database - Question table](https://github.com/MarcoXZh/QuestionnairePageDjango/raw/master/screenshots/question.png)

There are 18 sample quetions injected to the database. Every time the page is
loaded, 12 randomly chosen quetions are shown.

![The database - Questioner table](https://github.com/MarcoXZh/QuestionnairePageDjango/raw/master/screenshots/questioner.png)

This table stores who, when and how the questions are answered:

- username would be "Guest" if not provided and be automatically numbered such
  as "Guest-1", "Guest-2" and so on;

- date is automatically generated when record aded;

- answers save the results in a JSON string, where the keys refer to the
  questions and values are the corresponding answers.
