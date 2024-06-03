from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='luga_posts'
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on =models.DateTimeField(auto_now=True)


    class Meta:
        """
        To order blog posts, recent posts appear on top
        """
        ordering = ["-created_on"]
    

    def __str__(self):
        """
        To display the title and author of the blog posts to the admin panel
        """
        return f"{self.title} | written by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    text = models.TextField()  
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


    class Meta:

        """
        To order comments, recent comments appear on top
        """
        ordering = ["-created_on"]

    def __str__(self):

        """
        To display the comment body and author of a comment on the amin panel
        """
        return f"Comment by {self.author} on {self.post}"