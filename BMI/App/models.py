from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})

class BMIRecord(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    bmi_category = models.CharField(max_length=20, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"BMI Record on {self.date}"

    def get_absolute_url(self):
        return reverse("bmi_detail", kwargs={"pk": self.pk})