from django.shortcuts import render, redirect
from django.contrib import messages

# import TodoForm from forms
from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by("-date")
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm()

    page = {
        "form": form,  # Corrected 'forms' to 'form'
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)

# Corrected the typo 'TodoFrom' to 'TodoForm'
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed !!!")  # Corrected 'item' to 'Item'
    return redirect('todo')


