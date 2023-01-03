from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        username_ = "admin"
        password_= "admin123"
        if not User.objects.filter(username=username_).exists():
            #  change the username, email and password before use
            #   it is recomended to use environment variables for this to avoid pushing sensitive 
            #      info in remote repository
            
            User.objects.create_superuser(username_, "admin@xyzdomain.com", password_)
            s = "'"+username_ +"' user has created with password '"+password_+"'"
            self.stdout.write(self.style.SUCCESS(s))
        else:
            self.stdout.write(self.style.SUCCESS("admin user already exists"))

