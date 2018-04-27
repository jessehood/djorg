from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Bookmark
from .forms import BookmarkForm

def index(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse('index'))
    context = {'bookmarks': Bookmark.objects.filter(user=request.user), 'form': BookmarkForm()}
    return render(request, 'bookmarks/index.html', context)

@require_POST
def create(request):
    """Takes the bookmark form data and saves it to the database."""
    form = BookmarkForm(request.POST)
    if form.is_valid():
        bookmark = form.save(commit=False)
        bookmark.user = request.user
        bookmark.save()
        return HttpResponseRedirect(reverse('index'))

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['name', 'url', 'notes']
    template_name = 'bookmarks/edit.html'
    success_url = reverse_lazy('index')

@require_GET
def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.delete()
    return HttpResponseRedirect(reverse('index'))