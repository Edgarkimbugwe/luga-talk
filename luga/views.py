from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from .models import BlogPost, Comment, Like
from .forms import CommentForm, BlogPostForm
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


STATUS = ((0, "Draft"), (1, "Published"))


# View for displaying a list of published blog posts
class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1)
    template_name = "luga/index.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = context['object_list']
        return context


# View for displaying details of a specific blog post
def blogpost_detail(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug, status=1)
    comments = blogpost.comments.filter(approved=True).order_by("-created_on")
    comment_count = comments.count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = blogpost
            comment.save()

            # Example of setting a first-party cookie
            response = HttpResponse('Comment submitted successfully!')
            response.set_cookie(
                'comment_submitted', 'true',
                max_age=3600, secure=True, httponly=True, samesite='Strict')

            messages.success(
                request,
                'Your comment has been submitted and is awaiting approval.')
            return redirect('blogpost_detail', slug=slug)
        else:
            messages.error(
                request, 'Error submitting comment. Please try again.')
    else:
        comment_form = CommentForm()

    return render(request, "luga/blogpost_detail.html", {
        "blogpost": blogpost,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    })



# View for editing a comment
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = BlogPost.objects.filter(status=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = blogpost
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment has been updated! successfully.')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))


# View for displaying the index page
def index(request):
    post_list = BlogPost.objects.select_related('author').all()
    return render(request, 'index.html', {'post_list': post_list})


# View for deleting a comment
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = BlogPost.objects.filter(status=1)
    blogpost = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
    else:
        messages.error(
            request,
            'You are not authorized to delete this comment.')

    return HttpResponseRedirect(reverse('blogpost_detail', args=[slug]))


# View for creating a new blog post
@login_required
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.status = 0
            blog_post.save()
            messages.success(
                request,
                'Your blog post has been created and is pending approval')
            return redirect('user_blogposts')
    else:
        form = BlogPostForm()

    return render(request, 'luga/create_blogpost.html', {'form': form})


# View for displaying the about page
class AboutView(TemplateView):
    template_name = 'luga/about.html'
    extra_context = {'title': 'About'}


# function that will retrieve the blog posts created by the logged-in user
@login_required
def user_blogposts(request):
    blogposts = BlogPost.objects.filter(author=request.user)
    liked_posts = Like.objects.filter(
        user=request.user, liked=True).select_related('post')
    return render(request, 'luga/user_blogposts.html', {
        'blogposts': blogposts,
        'liked_posts': [like.post for like in liked_posts],
    })


# View for liking/unliking a blog post
@login_required
def like_blogpost(request, post_id):
    blogpost = get_object_or_404(BlogPost, id=post_id)
    if blogpost.author == request.user:
        messages.warning(request, 'You cannot like your own blog post!')
        return redirect('blogpost_detail', slug=blogpost.slug)
    like, created = Like.objects.get_or_create(
        post=blogpost, user=request.user)
    like.liked = not like.liked
    like.save()
    return redirect('blogpost_detail', slug=blogpost.slug)


# View for removing a blog post from favorites
@login_required
def remove_favorite(request, post_id):
    blogpost = get_object_or_404(BlogPost, id=post_id)
    if request.method == "POST":
        like = get_object_or_404(Like, post=blogpost, user=request.user)
        like.liked = False
        like.save()
        messages.success(
            request, 'The post has been removed from your favorites.')
        return redirect('user_blogposts')
    return render(
        request, 'luga/remove_favorite.html', {'blogpost': blogpost})


# View for editing a blog post
@login_required
def blogpost_edit(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug, author=request.user)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            messages.success(request, 'Blog post updated successfully.')
            return redirect('blogpost_detail', slug=slug)
    else:
        form = BlogPostForm(instance=blogpost)
    return render(
        request,
        'luga/blogpost_edit.html', {'form': form, 'blogpost': blogpost})


# View for deleting a blog post
@login_required
def blogpost_delete(request, slug):
    blogpost = get_object_or_404(BlogPost, slug=slug, author=request.user)
    if request.method == "POST":
        blogpost.delete()
        messages.success(request, 'Blog post deleted successfully.')
        return redirect('user_blogposts')
    return render(
        request, 'luga/blogpost_delete.html', {'blogpost': blogpost})


# Custom 404 error page view
def custom_404(request, exception):
    return render(request, '404.html', status=404)


# Custom 500 error page view
def custom_500(request):
    return render(request, '500.html', status=500)

# def test_500(request):
    # This will raise an exception to test the 500 error page
    # raise Exception("Test 500 error")
