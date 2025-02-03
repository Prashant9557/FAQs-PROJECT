from django.utils.translation import activate
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.html import strip_tags
from django.http import JsonResponse
from django.views import View
from .models import FAQ

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()  # Query the FAQ model
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.GET.get('lang', 'en')  # Get language from query parameter
        activate(lang)  # Set the active language to the one passed in the request
        return FAQ.objects.all() 


class FaqSearchView(View):
    def get(self, request):
        query = request.GET.get("query", "").strip()
        if not query:
            return JsonResponse({"error": "Query parameter is required"}, status=400)
        
        faqs = FAQ.objects.filter(question__icontains=query)  # Adjust based on model
        data = [{"question": faq.question, "answer": faq.answer} for faq in faqs]

        return JsonResponse({"results": data})