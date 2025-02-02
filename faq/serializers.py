from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()


    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at']


    def get_question(self, obj):
        """Return translated question based on the selected language."""
        request = self.context.get('request', None)
        lang = request.query_params.get('lang', 'en') if request else 'en'
        return obj.get_translated_question(lang)

    def get_answer(self, obj):
        """Return translated answer based on the selected language."""
        request = self.context.get('request', None)
        lang = request.query_params.get('lang', 'en') if request else 'en'
        return obj.get_translated_answer(lang)
        
