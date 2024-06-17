from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='luga_posts'
    )
    featured_image = CloudinaryField('image', default='placeholder', blank=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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

class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return f"Like on {self.post.title} by {self.user.username}"