import pytest
from django.contrib.auth import get_user_model
from .models import ProjetPro


@pytest.fixture
def user():
    user = get_user_model().objects.create_user(
        username="testuser", email="test@email.com", password="testpassword"
    )
    return user


@pytest.fixture
def projet_pro(user):
    projet = ProjetPro.objects.create(
        author=user,
        nom="Test Projet",
        description="Test description",
        categorie=["Backend", "Fullstack"],
        start_date="2023-01-01",
        end_date="2023-02-01",
        url="http://example.com",
        github="http://github.com",
        technologies=["Django", "Flask"],
        clients="Test Client",
        lien_clients="http://client.com",
        problemes_resolus="Test problems",
    )
    return projet


@pytest.mark.django_db
def test_projet_pro_str(projet_pro):
    assert str(projet_pro) == "Test Projet"


@pytest.mark.django_db
def test_projet_pro_creation(user):
    projet_pro = ProjetPro.objects.create(
        author=user,
        nom="Test Projet",
        description="Test description",
        categorie=["Backend", "Fullstack"],
        start_date="2023-01-01",
        end_date="2023-02-01",
        url="http://example.com",
        github="http://github.com",
        technologies=["Django", "Flask"],
        clients="Test Client",
        lien_clients="http://client.com",
        problemes_resolus="Test problems",
    )
    assert projet_pro.author == user
    assert projet_pro.nom == "Test Projet"
    assert projet_pro.description == "Test description"
    assert projet_pro.categorie == ["Backend", "Fullstack"]
    assert projet_pro.start_date == "2023-01-01"
    assert projet_pro.end_date == "2023-02-01"
    assert projet_pro.url == "http://example.com"
    assert projet_pro.github == "http://github.com"
    assert projet_pro.technologies == ["Django", "Flask"]
    assert projet_pro.clients == "Test Client"
    assert projet_pro.lien_clients == "http://client.com"
    assert projet_pro.problemes_resolus == "Test problems"
