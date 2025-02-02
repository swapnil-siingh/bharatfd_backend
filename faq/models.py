from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache
from django.conf import settings


translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Support
    translations = models.JSONField(default=dict, blank=True, null=True)  # Store translations as JSON
    created_at = models.DateTimeField(auto_now_add=True)  # Track FAQ creation time

    def save(self, *args, **kwargs):
        """Auto-translate the question and answer into other languages on save."""
        target_languages = list(settings.LANGUAGE_CODES)  # Ensure it's a list    
        for lang in target_languages:
            if lang not in self.translations or not self.translations[lang] or not self.translations[lang].get("question"):
                try:
                    translated_question = translator.translate(self.question, src='en', dest=lang).text
                    translated_answer = translator.translate(self.answer, src='en', dest=lang).text
                    self.translations[lang] = {
                        "question": translated_question,
                        "answer": translated_answer
                    }
                except Exception as e:
                    print(f"Translation failed for {lang}: {e}")
                    self.translations[lang] = {"question": self.question, "answer": self.answer}  # Fallback

        super().save(*args, **kwargs)
        self._clear_translation_cache()

    def get_translated_question(self, lang='en'):
        """Retrieve translated question."""
        return self._get_translated_field('question', lang)

    def get_translated_answer(self, lang='en'):
        """Retrieve translated answer."""
        return self._get_translated_field('answer', lang)

    def _get_translated_field(self, field_type, lang):
        """Fetch translated text from cache or JSONField."""
        if lang not in settings.LANGUAGE_CODES:
            lang = 'en'  # Default to English if language is invalid

        cache_key = f"faq_{self.id}_{field_type}_{lang}"
        cached_value = cache.get(cache_key)

        if cached_value:
            return cached_value  # Return cached translation if available

        translated_data = self.translations.get(lang, {})

        if not isinstance(translated_data, dict):  
            translated_data = {field_type: translated_data}  # Convert single value to dict

        value = translated_data.get(field_type, '').strip()

        # Fallback to English if translation is missing
        if not value:
            value = getattr(self, field_type, '')

        # Cache translation for 1 hour
        cache.set(cache_key, value, timeout=60 * 60)
        return value

    def _clear_translation_cache(self):
        """Clear cached translations after updates."""
        for lang in settings.LANGUAGE_CODES:
            cache.delete_many([
                f"faq_{self.id}_question_{lang}",
                f"faq_{self.id}_answer_{lang}"
            ])

    def __str__(self):
        return self.question

