import datetime, sqlite3


questions = [
    'What is the name of the most funny guy you ever met?',
    'How much is your birth year plus your birth month plus your birth day?',
    'Which city did you go for your last trip?',
    'What is the name of your firt pet?',
    'What is the name of your first math teacher?',
    'Who is your best friend?',
    'When is the most important day, YYYY-MM-DD please?',
    'Which day was your last convocation day?',
    'Which day of a week do you like most?',
    'Which day of a week do you hate most?',
    'Which city did you live during the last Christmas day?',
    'What is the first job that you ever get paid?',

    'What is your favorite color?',
    'What is the most impressive programming language you ever heard of?',
    'Which web site do you visit most?',
    'What is the model of your favorit cellphone?',
    'What is your favorite video game?',
    'What is the color of you first car?'
] # questions = [ ... ]

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create necessary tables
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "questionnaire_question" (
        "id"        integer         NOT NULL PRIMARY KEY AUTOINCREMENT,
        "text"      varchar(256)    NOT NULL UNIQUE
    );
    '''
) # cursor.execute( ... )
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS "questionnaire_questioner" (
        "id"        integer         NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name"      varchar(256)    NOT NULL,
        "date"      datetime        NOT NULL,
        "questions" varchar(256)    NOT NULL,
        "answers"   varchar(256)    NOT NULL
    );
    '''
) # cursor.execute( ... )
conn.commit()

# Insert sample questions
for i, q in enumerate(questions):
    cursor.execute(
        '''
        INSERT INTO `questionnaire_question`(`text`) VALUES ('%s');
        ''' % q
    )
    print('%s Question inserted (%d/%d) - %s'
                % (datetime.datetime.now(), i+1, len(questions), q))
# for i, q in enumerate(questions)
conn.commit()

# Verify insertions
cursor.execute('SELECT * FROM `questionnaire_question`;')
questions = cursor.fetchall()
for i, q in enumerate(questions):
    print('%s Question (%d/%d): %s'
                % (datetime.datetime.now(), i+1, len(questions), q))
# for i, q in enumerate(questions)
conn.close()
