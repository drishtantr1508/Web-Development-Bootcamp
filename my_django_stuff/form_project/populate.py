import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'form_project.settings')
import django
django.setup()
from faker import Faker
from form_app.models import Address,User
import random
def fake_contact():
    no=[]
    no.append(str(random.randint(6,9)))
    for i in range(9):
        no.append(str(random.randint(0,9)))
    return int("".join(no))
def populate(N=5):
    fake=Faker()
    for i in range(N):
        first=fake.first_name()
        last=fake.last_name()
        address_=fake.address()
        email=fake.email()
        contact=fake_contact()
        users=User(first_name=first,last_name=last,Email=email,mobile_no=contact)
        users.save()
        addresses=Address(user=users,address=address_)
        addresses.save()
if __name__ == '__main__':
    print('populating')
    populate(20)
    print("populated")
