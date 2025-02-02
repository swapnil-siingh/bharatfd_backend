from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """Admin panel configuration for managing FAQs."""

    list_display = ('question', 'get_translated_question_hi', 'get_translated_question_bn', 
                    'get_translated_question_fr', 'get_translated_question_ta')
    search_fields = ('question',)

    def get_translated_question(self, obj, lang):
        """Retrieve translated question for the given language."""
        return obj.translations.get(lang, {}).get('question', 'N/A')

    def get_translated_question_hi(self, obj):
        return self.get_translated_question(obj, 'hi')
    get_translated_question_hi.short_description = "Question (Hindi)"

    def get_translated_question_bn(self, obj):
        return self.get_translated_question(obj, 'bn')
    get_translated_question_bn.short_description = "Question (Bengali)"

    def get_translated_question_fr(self, obj):
        return self.get_translated_question(obj, 'fr')
    get_translated_question_fr.short_description = "Question (French)"

    def get_translated_question_ta(self, obj):
        return self.get_translated_question(obj, 'ta')
    get_translated_question_ta.short_description = "Question (Tamil)"
