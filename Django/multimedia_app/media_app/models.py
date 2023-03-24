from django.db import models

# Create your models here.



class Media(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    media_file = models.FileField(upload_to='media/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name