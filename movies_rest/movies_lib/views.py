from django.shortcuts import render
from .models import MovieItem, CommentItem
from django.http import HttpResponseRedirect, HttpResponse
import requests

# omdapi.com API key
api_key = 'apikey=8a9a1640'


def handle_movies(request):
	all_movies = MovieItem.objects.all()

	# request from external api on POST
	if request.method == 'POST':
		title_to_add = request.POST['movie_title']

		response = requests.get(f'http://www.omdbapi.com/?t={title_to_add}&{api_key}')
		if response.status_code != 200:
			return HttpResponse(request, f"<h2>Can't request API, code: {response.status_code}</h2>")

		json_data = response.json()

		# validate if have Title in response
		try:
			if json_data['Response'] == "True":
				new_movie = MovieItem(
						title=json_data['Title'],
						year=json_data['Year'],
						director=json_data['Director'],
						full_data=json_data,
					)
				new_movie.save()
		except Exception:
			return HttpResponse("<h2>No such movie in DB</h2>")
		
		return render(request, "added.html", {'new_movie': json_data})
	elif request.method == "GET":
		return render(request, "movies.html", {'all_movies': all_movies})


def handle_comments(request):
	all_comments = CommentItem.objects.all()

	# request from external api on POST
	if request.method == 'POST':
		try:
			movie_id = request.POST['movie_id']
			comment_body = request.POST['comment_body']
			movie = MovieItem.objects.get(pk=movie_id)

			new_comment = CommentItem(
						movie_id=movie,
						body=comment_body,
					)
			new_comment.save()

			#return render(request, "comments.html", {'all_comments': all_comments})
		except Exception:
			return HttpResponse("<h3>Wrong kwargs in your request</h3>")
	elif request.method == "GET":
		if len(all_comments) == 0:
			return HttpResponse("<h3>No Comments</h3>")

	return render(request, "comments.html", {'all_comments': all_comments})


def sort_by_movie(request, movie_id):
	try:
		movie = MovieItem.objects.get(pk=movie_id)
		movie_comments = CommentItem.objects.filter(movie_id=movie)

		return render(request, "comments.html", {'movie_comments': movie_comments})
	except Exception:
		return HttpResponse("<h3>Error: No such movie</h3>")


def top_movies(request, todo_id):
	pass
	# delete a new todo to add to all_items
	item_to_delete = TodoItem.objects.get(id=todo_id)
	# save
	item_to_delete.delete()
	# redirect the browser to "/todo/"
	return HttpResponseRedirect("/todo/")
