from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from notification.signals import notify


class NotificationQuerySet(QuerySet):
    def unsent(self):
        return self.filter(emailed=False)

    def sent(self):
        return self.filter(emailed=True)

    def unread(self, include_deleted=False):
        return self.filter(unread=True)

    def read(self, include_deleted=False):
        return self.filter(unread=False)

    def mark_all_as_read(self, recipient=None):
        qset = self.unread(True)
        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(unread=False)

    def mark_all_as_unread(self, recipient=None):
        qset = self.read(True)

        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(unread=True)

    def deleted(self):
        return self.filter(deleted=True)

    def active(self):
        return self.filter(deleted=False)

    def mark_all_as_deleted(self, recipient=None):
        qset = self.active()
        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(deleted=True)

    def mark_all_as_active(self, recipient=None):
        qset = self.deleted()
        if recipient:
            qset = qset.filter(recipient=recipient)

        return qset.update(deleted=False)

    def mark_as_unsent(self, recipient=None):
        qset = self.sent()
        if recipient:
            qset = qset.filter(recipient=recipient)
        return qset.update(emailed=False)

    # def mark_as_sent(self, recipient=None):
    #     qset = self.unsent()
    #     if recipient:
    #         qset = qset.filter(recipient=recipient)
    #     return qset.update(emailed=True)


class Notification(models.Model):
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        related_name="notifications",
        on_delete=models.CASCADE,
    )
    unread = models.BooleanField(default=True, blank=False, db_index=True)

    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    # public = models.BooleanField(default=True, db_index=True)
    deleted = models.BooleanField(default=False, db_index=True)
    # emailed = models.BooleanField(default=False, db_index=True)

    objects = NotificationQuerySet.as_manager()

    class Meta:
        ordering = ("-timestamp",)
        # index_together = ('recipient', 'unread')

    def __str__(self):
        return self.description

    def timesince(self, now=None):
        from django.utils.timesince import timesince as timesince_

        return timesince_(self.timestamp, now)

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def mark_as_unread(self):
        if not self.unread:
            self.unread = True
            self.save()


def notify_handler(**kwargs):
    recipient = kwargs.pop("recipient")
    # public = bool(kwargs.pop('public', True))
    description = kwargs.pop("description", None)
    timestamp = kwargs.pop("timestamp", timezone.now())

    new_notifications = []
    try:
        for receiver in recipient:
            newnotify = Notification(
                recipient=receiver,
                description=description,
                # timestamp=timestamp,
            )

            newnotify.save()
            new_notifications.append(newnotify)
    except:

        newnotify = Notification(
            recipient=recipient,
            description=description,
            # timestamp=timestamp,
        )

        newnotify.save()
        new_notifications.append(newnotify)

    return new_notifications


notify.connect(notify_handler, dispatch_uid="notifications.models.notification")
