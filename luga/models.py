from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Choices for the status of a BlogPost
STATUS = ((0, "Draft"), (1, "Published"))


class BlogPost(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='luga_posts'
    )  # Author of the blog post, linked to the User model
    featured_image = CloudinaryField(
        'image', default='placeholder', blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  # Date and time of creation
    status = models.IntegerField(choices=STATUS, default=0)  # Status of the blog post (Draft or Published)
    excerpt = models.TextField(blank=True)  # Summary of the blog post
    updated_on = models.DateTimeField(auto_now=True)  # Date and time of last update

    class Meta:
        """
        Metadata for ordering blog posts by creation date, newest first.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        String representation of the blog post.
        """
        return f"{self.title} | written by {self.author}"

    def save(self, *args, **kwargs):
        """
        Override save method to automatically generate slug from title if not provided.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    """
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments'
    )  # BlogPost associated with the comment
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter'
    )  # User who authored the comment
    text = models.TextField()  # Content of the comment
    created_on = models.DateTimeField(auto_now_add=True)  # Date and time of comment creation
    updated_on = models.DateTimeField(auto_now=True)  # Date and time of last update
    approved = models.BooleanField(default=False)  # Approval status of the comment

    class Meta:
        """
        Metadata for ordering comments by creation date, newest first.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        String representation of the comment.
        """
        return f"Comment by {self.author} on {self.post}"


class Like(models.Model):
    """
    Model representing a like on a blog post.
    """
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='likes'
    )  # BlogPost associated with the like
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )  # User who liked the blog post
    liked = models.BooleanField(default=False)  # Boolean indicating if the post was liked or not

    def __str__(self):
        """
        String representation of the like.
        """
        return f"Like on {self.post.title} by {self.user.username}"
