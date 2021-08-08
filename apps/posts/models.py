from django.db import models


class Author(models.Model):
    chelovek = models.CharField(max_length=100)

    def __str__(self):
        return self.chelovek


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

