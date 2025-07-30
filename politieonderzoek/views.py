from django.shortcuts import render
from django.views import View
from .forms import PolitietermSearchForm, AutoSearchForm, PersoonSearchForm
from .models import Politieterm, Auto, Persoon
from django.contrib.auth.mixins import LoginRequiredMixin

class MainPageView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
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
                    normalized = term.replace(" ", "").lower()
                    
                    # Search for partials
                    partial_matches = Persoon.objects.filter(
                                        voornaam__icontains=term
                                    ) | Persoon.objects.filter(
                                        familienaam__icontains=term
                                    )
                    
                    # Include exact match of voornaam + familienaam (normalized)
                    all_matches = list(partial_matches)
                    
                    # Add additional exact matches (not already in the partials)
                    for persoon in Persoon.objects.all():
                        full_name = (persoon.voornaam + persoon.familienaam).replace(" ", "").lower()
                        if full_name == normalized and persoon not in all_matches:
                            all_matches.append(persoon)
                    
                    if all_matches:
                        context['persoon_results'] = all_matches
                    else:
                        context['persoon_error'] = "Geen personen gevonden."

            return render(request, self.template_name, context)
