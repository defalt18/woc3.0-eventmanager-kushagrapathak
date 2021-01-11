from django.db import models

# Create your models here.
class register(models.Model) :
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    link = models.CharField(max_length=300)
    deadline = models.DateField()
    date = models.DateField()
    E_id = models.CharField(max_length=200,default = "xywerwedkndskj2")

    def __str__(self):
        return self.name

class partregister(models.Model) :
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    contact = models.CharField(max_length=12)
    event_name = models.CharField(max_length=122)
    number = models.CharField(max_length=122,default = "1")
    p_id = models.CharField(max_length=200,default = "po1")

    def __str__(self):
        return self.name


class hosts(models.Model) :
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    h_id = models.CharField(max_length=200,default = "ho1")

    def __str__(self):
        return self.username