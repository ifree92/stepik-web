# import sys
import os
import django
import lorem
import random
import time
from datetime import datetime

# sys.path.append("G:\\Projects\\stepik-web\\django-stepik\\ask")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")
django.setup()
from django.contrib.auth.models import User
from qa.models import Question, Answer


# =============== helpers ================

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def __randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)


def get_random_datetime():
    return datetime.strptime(randomDate("1/1/2016 1:30 PM", "1/1/2009 4:50 AM", random.random()), '%m/%d/%Y %I:%M %p')

# =============== /helpers ================

# =============== additional functions ==================


def get_random_users(users, count):
    max = len(users)
    _users = set()
    while 3 > len(_users):
        _users.add(users[random.randrange(0, max)])
    return _users


def create_users():
    users = list()
    for __i in range(10):
        _user = User.objects.create_user("username_" + str(__i))
        users.append(_user)
        print(str(_user) + " created")
    return users


def remove_users(users):
    for user in users:
        _user_name = user.username
        user.delete()
        print(_user_name + " removed")


def create_questions(users):
    for user in users:
        for __q in range(10):
            q = Question(title=lorem.sentence(),
                         text=lorem.text(),
                         added_at=get_random_datetime(),
                         rating=random.randint(0, 100),
                         author=user
                         )
            q.save()




# =============== additional functions ==================

users = create_users()

remove_users(users)
