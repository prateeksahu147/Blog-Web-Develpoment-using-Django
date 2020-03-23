from django.db import models


class TopPosts(models.Model):
    img_top= models.ImageField(upload_to="images")
    top_post_heading= models.CharField(max_length=50, default="")
    summary_top= models.CharField(max_length= 100)


class Projects(models.Model):
    Title= models.CharField(max_length=50 , default='')
    Description= models.CharField(max_length=500, default='')
    Images= models.ImageField(upload_to='images')
    Date= models.DateTimeField()
    Content=models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.Title ## by this function we can see our objects as title name in admin


