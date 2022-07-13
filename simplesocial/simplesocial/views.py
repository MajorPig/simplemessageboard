from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name: str = 'test.html'

class ThanksPage(TemplateView):
    template_name: str = 'thanks.html'

class HomePage(TemplateView):
    template_name: str = 'index.html'