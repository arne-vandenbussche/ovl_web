from django.shortcuts import render
from django.views import View
from .forms import PolitietermSearchForm, AutoSearchForm, PersoonSearchForm
from .models import Politieterm, Auto, Persoon

class MainPageView(View):
    template_name = "politieonderzoek/index.html"

    def get(self, request):
        return render(request, self.template_name,
            {
                        'politieterm_form': PolitietermSearchForm(),
                        'auto_form': AutoSearchForm(),
                        'persoon_form': PersoonSearchForm(),
                    })

    def post(self, request):
            form_type = request.POST.get("submit_type")
            context = {
                'politieterm_form': PolitietermSearchForm(),
                'auto_form': AutoSearchForm(),
                'persoon_form': PersoonSearchForm(),
            }

            if form_type == "politieterm":
                form = PolitietermSearchForm(request.POST)
                context['politieterm_form'] = form
                if form.is_valid():
                    afk = form.cleaned_data['afkorting']
                    print("DEBUG afk = ", afk)
                    try:
                        result = Politieterm.objects.get(afkorting=afk)
                        context['politieterm_result'] = result
                    except Politieterm.DoesNotExist:
                        context['politieterm_error'] = "Afkorting niet gevonden."

            elif form_type == "auto":
                form = AutoSearchForm(request.POST)
                context['auto_form'] = form
                if form.is_valid():
                    plate = form.cleaned_data['nummerplaat']
                    try:
                        result = Auto.objects.get(nummerplaat=plate)
                        context['auto_result'] = result
                    except Auto.DoesNotExist:
                        context['auto_error'] = "Nummerplaat niet gevonden."

            elif form_type == "persoon":
                form = PersoonSearchForm(request.POST)
                context['persoon_form'] = form
                if form.is_valid():
                    term = form.cleaned_data['zoektermpersoon']
                    results = Persoon.objects.filter(
                        voornaam__icontains=term
                    ) | Persoon.objects.filter(
                        familienaam__icontains=term
                    )
                    if results.exists():
                        context['persoon_results'] = results
                    else:
                        context['persoon_error'] = "Geen persoon gevonden."

            return render(request, self.template_name, context)
