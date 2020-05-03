from django.shortcuts import render, redirect
from .forms import PrintForm
import os
from django.conf import settings


# Create your views here.
def print_file(request):
    if request.method == 'GET':
        form = PrintForm()
        return render(request, template_name='print/printForm.html', context={'form': form})

    if request.method == 'POST':
        form = PrintForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, template_name='print/printForm.html', context={'form': form})

        file = list(request.FILES.values())[0]
        file_ext = file.name[file.name.rindex('.')+1:]
        file_name = 'test.' + file_ext
        media_path = os.path.join(settings.BASE_DIR, 'media')

        with open(os.path.join(media_path, file_name), 'wb+') as dest:
            for chunk in file.chunks():
                dest.write(chunk)

        os.system('lp ' + os.path.join(media_path, file_name))

        if os.path.exists(os.path.join(media_path, file_name)):
            os.remove(os.path.join(media_path, file_name))

        return redirect('print_file')
