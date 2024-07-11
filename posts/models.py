from django.db import models
from datetime import datetime





""" class Post(models.Model):
    title = models.CharField(max_length=100)
    body = HTMLField()  # Using HTMLField for rich text content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the creation time
    author = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Notify subscribers about new blog post
        subject = f'New Blog Post: {self.title}'
        message = f'Check out our new blog post: {self.get_absolute_url()}\n\n{self.body}'
        subscribers_emails = Subscriber.objects.values_list('email', flat=True)  # Assuming Subscriber model exists
        send_email_via_mailersend(subject, message, subscribers_emails) """


# posts/models.py

from django.db import models
import requests
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




class NewsletterUser(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Writer(models.Model):
    name = models.CharField(max_length=200)
    createdDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return u'%s' % (self.name)

class Article(models.Model):
    text_title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(max_length=200, null=True, blank=True)
    refWriter = models.ForeignKey(Writer, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return u'[%s] : %s' % (self.refWriter,self.text_title)
    



class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.email})'
    

