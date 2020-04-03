from django.shortcuts import render
from .models import MovieItem
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse

all_movies = [
{
	'title': "Mov1",
	'author': "Cameron",
	'date': "today"
},
{
	'title': "Mov2",
	'author': "James",
	'date': "yesterday"
}
]


def handle_movies(request):
	all_items = MovieItem.objects.all()

	# request from external api on POST
	if request.method == 'POST':
		title_to_add = request.POST['movie_title']
		all_movies.append(title_to_add) # remove this line, it's dict
		new_movie = MovieItem(title=title_to_add)
		new_movie.save()
		
		return render(request, "index.html", {'all_movies': all_items})
	else:
		return render(request, "index.html", {'all_movies': all_movies})


def handle_comments(request):
	return render(request, "comments.html")


def top_movies(request, todo_id):
	pass
	# delete a new todo to add to all_items
	item_to_delete = TodoItem.objects.get(id=todo_id)
	# save
	item_to_delete.delete()
	# redirect the browser to "/todo/"
	return HttpResponseRedirect("/todo/")
