from django.shortcuts import render
from .models import Post

fake_post = [
	{
		'author' : 'Mijato',
		'title' : 'Blog Post 1',
		'content': 'Somo dummy post ',
		'date' : '08.08.1998'


	},
		{
		'author' : 'Jane Doe',
		'title' : 'Blog Post 2',
		'content': 'Somo dummy post 2 ',
		'date' : '16.08.1998'


	},
		{
		'author' : 'Furnis',
		'title' : 'Blog Post 3',
		'content': 'Somo dummy post 3',
		'date' : '22.08.1998'

	}
]

def home(request):
	context = {'posts': Post.objects.order_by('-created_date')}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})