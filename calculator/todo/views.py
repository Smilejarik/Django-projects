from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect

def todoView(request):
	all_items = TodoItem.objects.all()
	return render(request, "todo.html",
		{'all_items': all_items})

def addTodo(request):
	# create a new todo to add to all_items
	new_item = TodoItem(content = request.POST['content'])
	# save
	new_item.save()
	# redirect the browser to "/todo/"
	return HttpResponseRedirect("/todo/")

def deleteTodo(request, todo_id):
	# delete a new todo to add to all_items
	item_to_delete = TodoItem.objects.get(id=todo_id)
	# save
	item_to_delete.delete()
	# redirect the browser to "/todo/"
	return HttpResponseRedirect("/todo/")