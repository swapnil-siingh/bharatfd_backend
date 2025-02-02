from django.contrib import admin
from .models import FAQ


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'get_question_hi', 'get_question_bn', 'get_question_fr','get_question_ta')
    search_fields = ('question',)

    def get_question_hi(self, obj):
        return obj.translations.get('hi', {}).get('question', 'N/A')
    get_question_hi.short_description = "Question (Hindi)"

    def get_question_bn(self, obj):
        return obj.translations.get('bn', {}).get('question', 'N/A')
    get_question_bn.short_description = "Question (Bengali)"

    def get_question_fr(self, obj):
        return obj.translations.get('fr', {}).get('question', 'N/A')
    get_question_fr.short_description = "Question (French)"


    def get_question_ta(self, obj):
        return obj.translations.get('ta', {}).get('question', 'N/A')
    get_question_ta.short_description = "Question (Tamil)"

