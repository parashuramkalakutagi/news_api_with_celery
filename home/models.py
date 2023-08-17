from django.db import models


class NewsBusiness(models.Model):
    author = models.CharField(max_length=250,null=True)
    title = models.CharField(max_length=290,null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=1000,null=True)
    urlToImage = models.ImageField(upload_to='business_news Images')
    publishedAt = models.CharField(max_length=200,null=True)
    content = models.TextField(null=True)


    def __str__(self):
        return self.author


class journal(models.Model):
    author = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=290, null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=1000, null=True)
    urlToImage = models.ImageField(upload_to=' Images')
    publishedAt = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)


    def __str__(self):
        return self.author