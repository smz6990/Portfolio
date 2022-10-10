from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ContactForm


class IndexView(TemplateView):

    template_name = "website/index.html"
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        form = ContactForm
        data['form'] = form
        return data


class ContactFormView(CreateView):

    form_class = ContactForm
    http_method_names = ['post']
    success_url = reverse_lazy("website:index")
    template_name = "blank.html"

    def form_invalid(self, form):
        messages.error(self.request, "مشکلی در فرم وجود دارد")
        messages.error(self.request, form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        if form.is_valid():
            messages.success(self.request, "فرم به درستی ثبت شد")
            form.save()
        return super().form_valid(form)
