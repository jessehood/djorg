from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Bookmark
from .forms import BookmarkForm

def index(request):
    context = {'bookmarks': Bookmark.objects.all(), 'form': BookmarkForm()}
    return render(request, 'bookmarks/index.html', context)

@require_POST
def create(request):
    """Takes the bookmark form data and saves it to the database."""
    form = BookmarkForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))

@require_http_methods(['GET', 'POST'])
def edit(request):
    raise NotImplementedError()

@require_GET
def read(request, pk):
    """Display the details of a single bookmark."""
    bookmark = get_object_or_404(Bookmark, pk=pk)
    context = {'bookmark': bookmark}
    return render(request, 'bookmarks/read.html', context)

@require_POST
def delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.delete()
    return HttpResponseRedirect(reverse('index'))