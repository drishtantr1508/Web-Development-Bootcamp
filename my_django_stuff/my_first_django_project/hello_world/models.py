from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=264,unique=True)
    def __str__(self):
        return self.top_name
class WebPage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)#this will link different models through common ids
    name=models.CharField(max_length=264,unique=True)
    url=models.URLField(unique=True)#this will check for a valid url. as some naughty users type "gwjcbjcnakcnbj" like this
    def __str__(self):
        return self.url
class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return str(self.date)
