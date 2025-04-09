from django.db import models
from uuid import uuid4


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    length = models.IntegerField(help_text="Duration in minutes")
    description = models.TextField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "course"