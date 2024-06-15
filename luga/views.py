from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import BlogPost
from .forms import CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1)
    template_name = "luga/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = context['object_list']
        return context

def blogpost_detail(request, slug):
        """
        Display an individual from

        :template:`luga/post_detail.html`
        """

        queryset = BlogPost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.all().order_by("-created_on")
        comment_count = blogpost.comments.filter(approved=True).count()
        comment_form = CommentForm()
        return render(
            request,
            "luga/blogpost_detail.html", 
            {
                "blogpost": blogpost,
                "comments": comments,
                "comment_count": comment_count,
                "comment_form": comment_form,
                
            },
        )

class AboutView(TemplateView):
    template_name = 'luga/about.html'
    extra_context = {'title': 'About'}