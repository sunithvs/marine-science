"""
Views of home page
"""

from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Notice, notice_types, Gallery, Seminar, Journals, Publication, Facility


class HomeView(TemplateView):
    """
    return home/index.html
    """
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = [
            {
                "name": "Department of Atmospheric Sciences",
                "website": "http://das.cusat.ac.in/",
                "courses": [
                    "M. Sc. Meteorology",
                    "Ph. D."
                ]
            },
            {
                "name": "Department of Physical Oceanography",
                "website": "https://dpo.cusat.ac.in/",
                "courses": [
                    "M. Sc. Oceanography",
                    "Ph. D."
                ]
            },
            {
                "name": "Department of Chemical Oceanography",
                "website": "https://cod.cusat.ac.in/",
                "courses": [
                    "M. Sc. Hydrochemistry",
                    "Ph. D.",
                ]
            },
            {
                "name": "Department of Marine Biology, Microbiology, Biochemistry",
                "website": "https://mbmb.cusat.ac.in/",
                "courses": [
                    "M. Sc. Marine Biology",
                    "M. Sc. Marine Genomics",
                    "Ph. D."
                ]
            },
            {
                "name": "Department of Marine Geology and Geophysics",
                "website": "https://marinegeo.cusat.ac.in/",
                "courses": [
                    "M. Sc. Marine Geology",
                    "M. Sc. Marine Geophysics",
                    "Ph. D."
                ]
            },
        ]
        notices = {}
        for notice_type in notice_types:
            if Notice.objects.filter(type=notice_type).order_by('-date').exists():
                notices[notice_type] = Notice.objects.filter(type=notice_type).order_by('-date')[:6]
        context["notices"] = notices
        context['gallery'] = Gallery.objects.all()
        context['seminars'] = Seminar.objects.all()
        context['journals'] = Journals.objects.all()
        context['publications'] = Publication.objects.all()
        context['facilities'] = Facility.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
