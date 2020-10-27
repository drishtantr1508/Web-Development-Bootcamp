from django.contrib import admin
from hello_world.models import AccessRecord,WebPage,Topic
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
