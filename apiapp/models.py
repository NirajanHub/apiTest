from django.db import models

# Create your models here.
class newsFeed(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    image=models.ImageField(upload_to='pics',max_length=225,null=True,blank=True)
    emp_id=models.IntegerField()
    def _str_(self):
        return self.firstname