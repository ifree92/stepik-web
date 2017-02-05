from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response


def test(request):
    return HttpResponse("OK")


@csrf_exempt
@require_GET
def my_test(request, *args, **kwargs):
    response = HttpResponse(
        content="this is finish",
        content_type="text/html",
        status=200
    )
    response["Age"] = 120
    response.set_cookie("visited", "1")
    # print("*args: ", args)
    # print("**kwargs:", kwargs)
    # print("request.method", request.method)
    # print("request.GET", request.GET)
    # print("request.POST", request.POST)
    # print("request.COOKIES", request.COOKIES)
    # print("request.FILES", request.FILES)
    # print("request.META", request.META)
    # print("request.session", request.session)
    # print("request.user", request.user)

    resp = render(request, "index.html", {
        "title": "This is main title",
        "caption": "Hello guys!",
        "text": "This is my first site on django framework!",
        "menu": ["item1", "item2", "item3"]
    })

    resp.set_cookie("hello", "world")
    resp["DA"] = "net"

    return resp
