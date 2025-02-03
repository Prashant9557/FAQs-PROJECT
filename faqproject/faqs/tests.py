import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_translation_and_api():
    # Create an FAQ instance
    faq = FAQ.objects.create(
        question="What is your return policy?",
        answer="Our return policy lasts 30 days.",
        question_hi="आपकी वापसी नीति क्या है?",
        answer_hi="हमारी वापसी नीति 30 दिनों तक चलती है।"
    )

    client = APIClient()
    url = reverse('faq-list')  # Ensure this matches your URL configuration
    response = client.get(f"{url}?lang=hi")
    assert response.status_code == 200
    data = response.json()
    # Check that the returned FAQ contains the Hindi translation
    assert any(faq_item["question"] == "आपकी वापसी नीति क्या है?" for faq_item in data)
# Create your tests here.
