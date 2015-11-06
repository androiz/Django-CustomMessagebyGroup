# Django-CustomMessagebyGroup
Field where you can edit custom messages for group inside an other model object 
For Django 1.8 or higher.

#Interesting files

CustomMessageApp/Models.py
    RoleMessage Class

CustomMessageApp/Admin.py
    Whole ServicesForm Class
    Whole ServicesAdmin Class

CustomMessageApp/Static/js/box.py

#Project Installation
python manage.py migrate
python manage.py collectstatic

Then, you can create a new Service and surprise editing it!