from django.shortcuts import render, redirect
from django.views import View
from .models import Announcement

# Create your views here.

class RedirectView(View):
    def get(self, request):
        return redirect("home/")

class HomeView(View):
    def get(self, request):
        announcement_list = Announcement.objects.filter(archived=False).order_by("-created_at")[:2]
        context = {
           "announcement_list": announcement_list,
        };
        return render(request, 'home/main.html', context);

class AnnouncementListView(View):
    def get(self, request):
        announcement_list = Announcement.objects.filter(archived=False).order_by("-created_at")
        context = {
           "announcement_list": announcement_list,
        };
        return render(request, 'home/announcements.html', context);