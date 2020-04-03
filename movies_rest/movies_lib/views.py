from django.shortcuts import render
from .models import MovieItem
from django.http import HttpResponseRedirect

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

def handleMovies(request):
	all_items = MovieItem.objects.all()

	# request from external api on POST
	if request.method == 'POST':
		title_to_add = request.POST['movie_title']
		all_movies.append(title_to_add)
		new_movie = MovieItem(title=title_to_add)
		new_movie.save()
		
		return render(request, "index.html",
			{'all_movies': all_items})
	else:
		return render(request, "index.html",
			{'all_movies': all_movies})

def handleComments(request):
	pass
	# create a new todo to add to all_items
	new_item = TodoItem(content = request.POST['content'])
	# save
	new_item.save()
	# redirect the browser to "/todo/"
	return HttpResponseRedirect("/todo/")

def topMovies(request, todo_id):
	pass
	# delete a new todo to add to all_items
	item_to_delete = TodoItem.objects.get(id=todo_id)
	# save
	item_to_delete.delete()
	# redirect the browser to "/todo/"
	return HttpResponseRedirect("/todo/")
