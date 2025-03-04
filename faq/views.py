from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from .models import FAQ
from .serializers import FAQSerializer
from .forms import SignUpForm, FAQForm


class FAQViewSet(viewsets.ModelViewSet):
    """ViewSet for handling FAQs with optional language translation."""
    
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        """
        Override the list method to support language selection via the 'lang' query parameter.
        If the provided language is not supported, defaults to English ('en').
        """
        lang = request.query_params.get('lang', 'en')

        if lang not in settings.LANGUAGE_CODES:
            lang = 'en'

        faqs = self.get_queryset()
        data = []

        for faq in faqs:
            faq_data = FAQSerializer(faq, context={'request': request}).data
            faq_data['translated_question'] = faq.get_translated_question(lang)
            faq_data['translated_answer'] = faq.get_translated_answer(lang)
            data.append(faq_data)

        return Response(data)


@login_required
def homepage(request):
    """
    Render the homepage with translated FAQ content.
    Superusers can edit FAQs, while others can only view them.
    """
    selected_language = request.GET.get('lang', 'en')

    if selected_language not in settings.LANGUAGE_CODES:
        selected_language = 'en'

    faqs = FAQ.objects.all()

    # Attach translated questions/answers to each FAQ object
    for faq in faqs:
        faq.translated_question = faq.get_translated_question(selected_language)
        faq.translated_answer = faq.get_translated_answer(selected_language)

    return render(request, 'faq/homepage.html', {
        'faqs': faqs,
        'is_superuser': request.user.is_superuser,
        'languages': settings.LANGUAGE_CODES,
        'selected_language': selected_language,
    })


@login_required
def add_faq(request):
    """
    Allow superusers to add new FAQs.
    If a non-superuser tries to access this view, they are redirected to the homepage.
    """
    if not request.user.is_superuser:
        return redirect('homepage')

    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FAQForm()

    return render(request, 'faq/faq_form.html', {'form': form, 'action': 'Add'})


@login_required
def edit_faq(request, faq_id):
    """
    Allow superusers to edit existing FAQs.
    If a non-superuser tries to access this view, they are redirected to the homepage.
    """
    if not request.user.is_superuser:
        return redirect('homepage')

    faq = get_object_or_404(FAQ, id=faq_id)

    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = FAQForm(instance=faq)

    return render(request, 'faq/faq_form.html', {'form': form, 'action': 'Edit'})


@login_required
def delete_faq(request, faq_id):
    """
    Allow superusers to delete existing FAQs.
    If a non-superuser tries to access this view, they are redirected to the homepage.
    """
    if not request.user.is_superuser:
        return redirect('homepage')

    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return redirect('homepage')


def signup_view(request):
    """
    User Signup View.
    Redirects authenticated users to the homepage.
    If a valid signup form is submitted, the user is created and logged in.
    """
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')  # Redirect after successful signup
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})
