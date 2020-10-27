import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_django_project.settings')#to configure the settings
import django
django.setup()#to configure the project settings.

##Fake pop JavaScript
import random
from hello_world.models import AccessRecord,WebPage,Topic# we are importing our models
from faker import Faker
fake=Faker()
topics="Search Social Marketplace News Games".split(" ")
def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):# we are giving a default value as 5
    for entry in range(N):
        top=add_topic() # getting object as topic
        fake_name=fake.company()
        fake_url=fake.url()
        fake_date=fake.date()
        webpg=WebPage(topic=top,url=fake_url,name=fake_name)
        webpg.save()
        AccRec=AccessRecord(name=webpg,date=fake_date)
        AccRec.save()
if __name__ == '__main__':
    print("Populating database!!!")
    populate(30)
    print("Populated successfully!!!")
