import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MTV_project.settings')
import django
django.setup()
from faker import Faker
import random
fake=Faker()# fake is an instance of Faker
from MTV_app.models import Address, User
def populate(N=5):
    for i in range(N):
        first=fake.first_name()
        last=fake.last_name()
        email_id=fake.email()
        add=fake.address()
        user_name=User(first_name=first,last_name=last,email=email_id)
        user_name.save()
        a=Address(address=add,user=user_name)
        a.save()

if __name__ == '__main__':
    print("Populating!!")
    populate(20)
    print("Populated Successfully!!")
