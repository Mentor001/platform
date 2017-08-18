import hashlib
from urllib.parse import urlencode

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from .choices import GENDER_CHOICES, ROLE_CHOICES
from core.choices import EDUCATION_CHOICES, MENTORSHIP_AREAS_CHOICES
from activities.models import Notification

from multiselectfield import MultiSelectField


class UserCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.IntegerField()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    bio = models.TextField(blank=True, default='')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    role = models.CharField(max_length=6,
        blank=False,
        default='mentee',
        choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=32)
    is_previously_logged_in = models.CharField(max_length=5, default=False)

    def is_mentor(self):
        return self.role == 'mentor'

    def is_mentee(self):
        return self.role == 'mentee'

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        return self.user.username

    def get_gravatar(self):
        gravatar_url = 'https://www.gravatar.com/avatar/{0}?{1}'.format(
            hashlib.md5(self.user.email.lower().encode('utf-8')).hexdigest(),
            urlencode({'s': '256'})
        )
        return gravatar_url

    def get_screen_name(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.username

    def notify_favorited(self, question):
        if self.user != question.user:
            Notification(notification_type=Notification.FAVORITED,
                         from_user=self.user, to_user=question.user,
                         question=question).save()

    def unotify_favorited(self, question):
        if self.user != question.user:
            Notification.objects.filter(
                notification_type=Notification.FAVORITED,
                from_user=self.user,
                to_user=question.user,
                question=question).delete()

    def notify_answered(self, question):
        if self.user != question.user:
            Notification(notification_type=Notification.ANSWERED,
                         from_user=self.user,
                         to_user=question.user,
                         question=question).save()

    def notify_also_answered(self, question):
        answers = question.get_answers()
        users = []
        for answer in answers:
            if answer.user != self.user and answer.user != question.user:
                users.append(answer.user.pk)
        users = list(set(users))
        for user in users:
            Notification(notification_type=Notification.ALSO_ANSWERED,
                         from_user=self.user, to_user=User(id=user),
                         question=question).save()

    def notify_accepted(self, answer):
        if self.user != answer.user:
            Notification(notification_type=Notification.ACCEPTED_ANSWER,
                         from_user=self.user,
                         to_user=answer.user,
                         answer=answer).save()

    def unotify_accepted(self, answer):
        if self.user != answer.user:
            Notification.objects.filter(
                notification_type=Notification.ACCEPTED_ANSWER,
                from_user=self.user,
                to_user=answer.user,
                answer=answer).delete()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
