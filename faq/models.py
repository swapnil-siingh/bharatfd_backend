from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
from django.conf import settings

translator = Translator()

class FAQ(models.Model):
    """Model representing a Frequently Asked Question (FAQ)."""

    question = models.TextField()
    answer = RichTextField()  # Supports rich text formatting
    translations = models.JSONField(default=dict, blank=True, null=True)  # Stores translations in JSON format
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the FAQ was created

    def save(self, *args, **kwargs):
        """Auto-translate the question and answer into supported languages upon saving."""
        target_languages = list(settings.LANGUAGE_CODES)  # Ensure it's a list

        for lang in target_languages:
            if not self.translations.get(lang, {}).get("question"):
                try:
                    self.translations[lang] = {
                        "question": translator.translate(self.question, src='en', dest=lang).text,
                        "answer": translator.translate(self.answer, src='en', dest=lang).text,
                    }
                except Exception as e:
                    print(f"Translation failed for {lang}: {e}")
                    self.translations[lang] = {"question": self.question, "answer": self.answer}  # Fallback

        super().save(*args, **kwargs)
        self._clear_translation_cache()

    def get_translated_question(self, lang='en'):
        """Retrieve the translated question for the specified language."""
        return self._get_translated_field('question', lang)

    def get_translated_answer(self, lang='en'):
        """Retrieve the translated answer for the specified language."""
        return self._get_translated_field('answer', lang)

    def _get_translated_field(self, field_type, lang):
        """
        Fetch translated content from cache or JSONField.
        If translation is missing, fallback to the English version.
        """
        if lang not in settings.LANGUAGE_CODES:
            lang = 'en'  # Default to English if language is invalid

        cache_key = f"faq_{self.id}_{field_type}_{lang}"
        cached_value = cache.get(cache_key)

        if cached_value:
            return cached_value  # Return cached translation if available

        translated_data = self.translations.get(lang, {})

        if not isinstance(translated_data, dict):  
            translated_data = {field_type: translated_data}  # Convert to dictionary if necessary

        value = translated_data.get(field_type, '').strip()

        # Fallback to English if translation is missing
        if not value:
            value = getattr(self, field_type, '')

        # Cache translation for 1 hour
        cache.set(cache_key, value, timeout=60 * 60)
        return value

    def _clear_translation_cache(self):
        """Clear cached translations when FAQ is updated."""
        for lang in settings.LANGUAGE_CODES:
            cache.delete_many([
                f"faq_{self.id}_question_{lang}",
                f"faq_{self.id}_answer_{lang}",
            ])

    def __str__(self):
        return self.question
