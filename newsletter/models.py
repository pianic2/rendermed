from django.db import models

# Create your models here.
class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Template(models.Model):
    """docstring for Template."""
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_template(self, pk):
        return Template.objects.get(id=pk)
