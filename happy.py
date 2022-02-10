from datetime import datetime

PYTHON_BIRTH_MONTH = 2
PYTHON_BIRTH_DAY = 20
PYTHON_BIRTH_YEAR = 1992

sorryMessage = "Sorry Python, it's not your birthday."
happyMessage = "Happy %dth Birthday, Python!"
now = datetime.now()

if (now.month == PYTHON_BIRTH_MONTH and now.day == PYTHON_BIRTH_DAY):
    age = now.year - PYTHON_BIRTH_YEAR
    print(happyMessage % age)
else:
    print(sorryMessage)
