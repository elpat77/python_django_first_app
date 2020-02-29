from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm

# Create your views here.


def home(request):

    if request.method == "POST":
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()

            todo_list = List.objects.all
            return render(request, 'home.html', {"todo_list": todo_list})

    else:
        todo_list = List.objects.all
        return render(request, 'home.html', {"todo_list": todo_list})


def delete(request, todo_id):
    item = List.objects.get(pk=todo_id)
    item.delete()
    return redirect('home')
