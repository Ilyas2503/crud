from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm
from .models import Person
from django.http import HttpResponse


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1> Success </h1>")
        else:
            return HttpResponse("<h1> error </h1>")
    form = PostForm()
    return render(request, 'create.html', {'form': form})


def edit(request, pk):
    post = get_object_or_404(Person, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, 'create.html', {'form': form})
