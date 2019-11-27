from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from wiki.models import Page
from wiki.forms import PageForm


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })


class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })


# class PageSignUpView(SignupView):
#     """ Renders sign up page """
#     model = Page
#     form_class = django.auth.forms.UserCreationForm
#
#     def get(self, request):
#         return render(request, 'registration/signup.html', )


class PageAddcardView(CreateView):
    template_name = 'addcard.html'

    def get(self, request):
        form = PageForm()
        print('get_method')
        return render(request, 'addcard.html', {'form': form})

    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            newcard = form.save()
            return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[newcard.slug]))
        return render(request, 'addcard.html', {'form': form})
