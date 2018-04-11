from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Bookmark
from .forms import BookmarkForm

def index(request):
    context = {'bookmarks': Bookmark.objects.all(), 'form': BookmarkForm()}
    return render(request, 'bookmarks/index.html', context)

@require_POST
def create(request):
    """Takes the bookform form data and saves it to the database."""
    form = BookmarkForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('index'))
