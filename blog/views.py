from django.shortcuts import render
from django.utils import timezone
from .models import Post 



def post_list(request):
	"""
	Author: Meghan Debity
	Purpose: Requesting info from model to pass to template
	"""
	# Note that posts is a variable for QuerySet
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})