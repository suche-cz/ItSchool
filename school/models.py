from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Course(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000, blank=True)
    # /media/course/...¨
    # blank = volené na úrovní UI
    # null =  volené na úrovní DB
    image = models.ImageField(blank=True, null=True, upload_to='course/')

    # vazba 1:N na User - Course.user_id -> User.id
    # on_delete co se má stát se záznamy Course, pokud vymažeme User
    # v tomto případě se nastaví null pokud uživatele vymažeme
    lector = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='lector_courses')

    # vazba M:N na User, blank - není povinné aby tam měl studenty
    students = models.ManyToManyField(User, blank=True, related_name='student_courses')

    def __str__(self):
        return self.name
