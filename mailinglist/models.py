import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse


class MailingList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mailinglist:mailinglist_list')

    def user_can_use_mailing_list(self, user):
        return user == self.owner


class Subscriber(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)
    mailing_list = models.ForeignKey(to=MailingList, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['email', 'mailing_list', ]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        is_new = self.state.adding or force_insert
        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)
        if is_new:
            self.send_confirmation_email()

    def send_confirmation_email(self):
        emails.send_confirmation_email(self)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mailing_list = models.ForeignKey(to=MailingList,
                                     on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    body = models.TextField()
    started = models.DateTimeField(default=None, null=True)
    finished = models.DateTimeField(default=None, null=True)
