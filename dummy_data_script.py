import os,sys
sys.path.append("C:\Users\pr_stellar\Desktop\democaller\venv\callerapp")
os.environ.setdefault("DJANGO_SETTING_MODULE","callerapp.settings")

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
		phone = '+91'
		phone.append(phone)
		print(name,' ',email,' ',phone)


if __name__ == '__main__':
	print('generating random data')
	call(10)
