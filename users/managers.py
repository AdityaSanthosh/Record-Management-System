from django.db import models
from record.models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin


class EntryQuerySet(LoginRequiredMixin, models.QuerySet):
    def get_query_value(self, entry_key, user):
        for entry in self.filter(user=user):
            query_value = entry
            if entry.name == entry_key:
                return query_value


class EntryManager(models.Manager):
    def get_queryset(self):
        return EntryQuerySet(Entry, using=self.db)

    def get_query_value(self, entry_key, user):
        return self.get_queryset().get_query_value(entry_key, user)
