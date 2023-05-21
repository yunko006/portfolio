from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField


class ProjetPro(models.Model):
    CATEGORIES = [
        ("Backend", "Backend"),
        ("Fullstack", "FullStack"),
        ("SQL", "SQL"),
        ("MongoDB", "mongodb"),
        ("Design", "Design"),
    ]

    TECHNO = [
        ("Django", "Django"),
        ("Flask", "Flask"),
        ("Python", "Python"),
        ("SQL", "SQL"),
        ("NoSQL", "NoSQL"),
        ("Docker", "Docker"),
        ("TailwindCSS", "tailwind"),
        ("Bootstrap", "Bootstrap"),
        ("HTMX", "Htmx"),
        ("Hyperscript", "Hyperscript"),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    categorie = MultiSelectField(
        choices=CATEGORIES, max_choices=5, max_length=20
    )  # select field
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    url = models.URLField()
    github = models.URLField()
    logo = models.URLField(null=True, blank=True)
    technologies = MultiSelectField(
        choices=TECHNO, max_choices=10, max_length=20
    )  # select field
    clients = models.CharField(max_length=50)
    lien_clients = models.URLField(null=True, blank=True)
    problemes_resolus = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
