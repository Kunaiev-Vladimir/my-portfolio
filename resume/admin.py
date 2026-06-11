from django.contrib import admin
from .models import Profile, Skill, Experience


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "position",
        "company",
        "work_type",
        "start_date",
        "end_date",
    )

    list_filter = (
        "work_type",
        "start_date",
    )

    search_fields = (
        "position",
        "company",
        "industry",
    )
