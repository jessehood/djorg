from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import UserFile
from .forms import UserFileForm

@require_http_methods(['GET', 'POST'])
def file_upload(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = user
            file.file_name = form.cleaned_data['file'].name
            file.save()
            return render(request, 'filestorage/files.html', {
                'form': form,
                'files': UserFile.objects.filter(user=user)
            })
    else:
        form = UserFileForm()
    return render(request, 'filestorage/files.html', {
        'form': form,
        'files': UserFile.objects.filter(user=user)
    })

@require_GET
def file_delete(request, pk):
    user = User.objects.get(username=request.user.username)
    file = get_object_or_404(UserFile, pk=pk)
    file.delete()
    return HttpResponseRedirect(reverse('file_upload'))