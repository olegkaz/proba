from django.db import models
from django.db.models import Sum


class Article(models.Model):
    class Meta:
        db_table = "article"
    article_title = models.CharField(max_length=100)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)



    def __str__(self):
        return self.article_title


class Comments(models.Model):
    class Meta:
        db_table = "comments"
    comments_text = models.TextField(verbose_name='Поле комментария')
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)


    def __str__(self):
        return self.comments_text
