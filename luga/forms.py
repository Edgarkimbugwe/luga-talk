from django_summernote.widgets import SummernoteWidget
from .models import Comment, BlogPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'featured_image', 'excerpt', 'content']
        widgets = {
            'content': SummernoteWidget(attrs={'class': 'summernote'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['featured_image'].required = False
