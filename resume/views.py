from django.shortcuts import render
from .models import Profile, Skill, Experience


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all().order_by("-level")
    experiences = Experience.objects.all()

    context = {
        "profile": profile,
        "skills": skills,
        "experiences": experiences,
    }

    return render(request, "resume/home.html", context)
