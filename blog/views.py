from django.shortcuts import render



def post_list(request):
	"""
	Author: Meghan Debity
	Purpose: Requesting info from model to pass to template
	"""

	return render(request, 'blog/post_list.html', {})