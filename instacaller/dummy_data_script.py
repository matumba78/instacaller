import os
os.environ.setdefault('DJANGO_SETTING_MODULE','callerapp.settings')

import 	django
django.setup()

from instacaller.models import User,UserAttached
from faker import Faker

obj = Faker()

def call():
	num = 1
	for i in range(N):
		full_name = obj.name()
		_list = full_name.split()
		name = _list[0]
		email = obj.email()
		phone_list = obj.msisdn()
		phone = '+91' + phone_list


if __name__ == '__main__':
	call(10)
