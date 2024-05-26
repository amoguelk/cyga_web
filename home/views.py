from django.shortcuts import render, redirect
from django.views import View
from .models import Announcement, Content

# Create your views here.

class RedirectView(View):
    def get(self, request):
        return redirect("home/")

class HomeView(View):
    def get(self, request):
        announcement_list = Announcement.objects.filter(archived=False).order_by("-created_at")[:2]
        slide_list = Content.objects.filter(type="SL", archived=False).order_by("order")
        context = {
           "announcement_list": announcement_list,
           "slide_list": slide_list
        };
        return render(request, 'home/main.html', context);

class AnnouncementListView(View):
    def get(self, request):
        announcement_list = Announcement.objects.filter(archived=False).order_by("-created_at")
        context = {
           "announcement_list": announcement_list,
        };
        return render(request, 'home/announcements.html', context);