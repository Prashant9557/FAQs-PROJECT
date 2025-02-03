from django.db import models
from ckeditor.fields import RichTextField
# faq/models.py

from django.utils.translation import get_language

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    # Add translated fields for each language
    # question_hi = models.CharField(max_length=255, blank=True, null=True)
    # answer_hi = models.TextField(blank=True, null=True)
    # question_bn = models.CharField(max_length=255, blank=True, null=True)
    # answer_bn = models.TextField(blank=True, null=True)

    # Add fields for other languages as needed

    def get_translation(self, lang_code=None):
        if lang_code is None:
            lang_code = get_language()  # Get the current active language

        translation = {
            'question': getattr(self, f'question_{lang_code}', self.question),
            'answer': getattr(self, f'answer_{lang_code}', self.answer),
        }
        return translation