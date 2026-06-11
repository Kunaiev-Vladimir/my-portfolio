from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="profile/", blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    short_description = models.TextField(blank=True)
    about_text = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name


class Experience(models.Model):
    WORK_TYPE_CHOICES = [
        ("main", "Основное место работы"),
        ("part_time", "Совместительство"),
    ]

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    industry = models.CharField(max_length=200, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    is_current = models.BooleanField(
        default=False,
        verbose_name="I currently work here"
    )

    work_type = models.CharField(
        max_length=20,
        choices=WORK_TYPE_CHOICES,
        default="main"
    )

    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} — {self.company}"
