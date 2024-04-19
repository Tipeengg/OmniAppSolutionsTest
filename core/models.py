from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    imgPath = models.CharField(max_length=255)
    duration = models.IntegerField(max_length=255)
    language = models.CharField(max_length=100)
    userRating = models.CharField(max_length=10)
    mpaaRating = models.ForeignKey('MPAARating', on_delete=models.CASCADE, null=True) 
    genre1 = models.ForeignKey('Genre', related_name='primary_genre', on_delete=models.CASCADE, null=True)
    genre2 = models.ForeignKey('Genre', related_name='secondary_genre', on_delete=models.CASCADE, null=True)

    
    def image_url(self):
        return f'/static/img/{self.imgPath}'  
    
    def get_genres(self):
        return ", ".join(genre.name for genre in self.genres.all())
    
    def get_genre1(self):
        return Genre.objects.get(id=self.genre1_id) if self.genre1_id is not None else None
    
    def get_genre2(self):
        return Genre.objects.get(id=self.genre2_id) if self.genre2_id is not None else None

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MPAARating(models.Model):
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.type