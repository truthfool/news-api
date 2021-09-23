from django.db import models

# Create your models here.
class NewsModel(models.Model):
    entity_type_id=models.CharField(max_length=50)
    dictionary_tokens=models.CharField(max_length=50)
    news_type=models.CharField(max_length=50)
    news_headline=models.TextField(max_length=100)
    news_article=models.TextField(max_length=250)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_by=models.CharField(max_length=50,blank=True)
    updated_on=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=["-updated_on"]
    
    def __str__(self):
        return self.news_headline
