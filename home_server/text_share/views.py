from django.shortcuts import render
from django.http import JsonResponse
from http import HTTPStatus
from .forms import TextShare
from .models import SavedText
from broadcast_service.server import HOST, PORT


# Create your views here.
def view_shared_text(request):
    if request.method == "GET":
        saved_text = list(SavedText.objects.all())
        if not saved_text:
            form = TextShare()
        else:
            form = TextShare(instance=saved_text[0])

        return render(
            request,
            template_name="text_share/text_share.html",
            context={"form": form, "server_socket": {"host": HOST, "port": PORT}},
        )

    elif request.method == "POST":
        form = TextShare(request.POST)

        if form.is_valid():
            a = SavedText.objects.get(pk=1)
            TextShare(request.POST, instance=a).save()

        return render(
            request, template_name="text_share/text_share.html", context={"form": form}
        )


def refresh_text(request):
    text = list(SavedText.objects.all())

    if not text:
        return JsonResponse(
            data={}, status=HTTPStatus.NOT_FOUND, reason="No Saved Text Found!!"
        )

    text_data = {"text": text[0].content}

    return JsonResponse(data=text_data, status=HTTPStatus.OK, reason="Success!!")
