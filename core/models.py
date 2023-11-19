from django.db import models
from django.contrib.auth.models import User


class ApplicationModel(models.Model):
    user = models.ForeignKey(User, related_name='forms',
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    educational_qualification = models.CharField(max_length=100)
    reason = models.TextField()
    cv = models.FileField(upload_to='static/CV')
    created_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return '/%s/' % self.first_name

    class Meta:
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
