from django.db import models
from django.contrib.auth.models import User


class projectModel(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    max_number = models.IntegerField()
    estimate_time = models.CharField(max_length=50)
    isActive = models.BooleanField(null=True)
    coder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class requestModel(models.Model):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DECLINED = "Declined"

    STATUS = (
        (PENDING, PENDING),
        (ACCEPTED, ACCEPTED),
        (DECLINED, DECLINED),
    )
    coder_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default=PENDING)
    message = models.TextField()
    project = models.ForeignKey(projectModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.coder_profile.username
