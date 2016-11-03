from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})

def post_details(request, id):
    """Create a view that returns a single Post object based on the post D and render it to the 'postdetail.html' template.
    Or return a 404 error if the opst is not found"""

    post=get_object_or_404(Post, pk=id)
    return render(request, "postdetail.html",{'post': post})