from django.shortcuts import render
from django.http import HttpResponse
from .models import Techblog, Card


def index(request):
    """
    Techblog 목록 출력
    """
    techblog_list = Techblog.objects.order_by("-create_date")
    context = {"techblog_list": techblog_list}

    return render(request, "techalook/techblog_list.html", context)


def detail(request, techblog_id):
    """
    Techblog 최근 콘텐츠 목록 출력
    """
    techblog = Techblog.objects.get(id=techblog_id)
    context = {"techblog": techblog}
    return render(request, "techalook/techblog_detail.html", context)
