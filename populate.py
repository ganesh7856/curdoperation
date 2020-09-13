import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','curdproject1.settings')
import django
django.setup()


from curdapp.models import *
from faker import Faker
from random import *

faker=Faker()

def populate(n):
    for i in range(n):
        fno=randint(1001,9999)
        fname=faker.name()
        fsal=randint(10000,60000)
        faddrs=faker.city()
        emp_records=Employee.objects.get_or_create(no=fno,name=fname,salary=fsal,address=faddrs)

populate(20)
