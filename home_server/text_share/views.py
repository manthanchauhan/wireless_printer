from django.shortcuts import render
from .forms import TextShare
from .models import SavedText

# Create your views here.
def view_shared_text(request):
    if request.method == 'GET':
        saved_text = list(SavedText.objects.all())
        if not saved_text:
            form = TextShare()
        else:
            form = TextShare(instance=saved_text[0])

        return render(request, template_name='text_share/text_share.html', context={'form': form})

    elif request.method == 'POST':
        form = TextShare(request.POST)

        if form.is_valid():
            a = SavedText.objects.get(pk=1)
            TextShare(request.POST, instance=a).save()

        return render(request, template_name='text_share/text_share.html', context={'form': form})
