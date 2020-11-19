from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name = "drishtant",
                        email = "drishtant.rai2000@gmail.com",
                        is_staff = True,
                        is_superuser = True,
                        gender = "Male",
                        phone = "8127203067"
                    )
        user.set_password("markstark@3000")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data)
    ]