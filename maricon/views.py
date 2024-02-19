from django.views.generic import TemplateView

from .models import Speaker, Faq, Sponsor, Schedule, Gallery, CommitteeMember, Committee


class IndexView(TemplateView):
    template_name = 'new_maricon/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['speakers'] = Speaker.objects.all()
        context['faqs'] = Faq.objects.all()
        context['sponsors'] = Sponsor.objects.all()
        context['schedule'] = [
            {
                'day': 'Day 1',
                'schedule': Schedule.objects.filter(day='Day 1')
            },
            {
                'day': 'Day 2',
                'schedule': Schedule.objects.filter(day='Day 2')
            },
            {
                'day': 'Day 3',
                'schedule': Schedule.objects.filter(day='Day 3')
            },
        ]
        context['gallery'] = Gallery.objects.all()
        committees = Committee.objects.only('name').order_by('-size_on_website')
        context['committees'] = committees
        return context


class CommitteeView(TemplateView):
    template_name = 'maricon/committee.html'

    def get_context_data(self, **kwargs):
        context = super(CommitteeView, self).get_context_data(**kwargs)
        committees = Committee.objects.all().order_by('-size_on_website')
        context['committee_names'] = committees
        context['committees'] = [
            {
                'committee': committee,
                'members': CommitteeMember.objects.filter(committee=committee)
            }
            for committee in committees
        ]
        return context


class RegisterView(TemplateView):
    template_name = 'maricon/register.html'


class OtpView(TemplateView):
    template_name = 'maricon/otp.html'


class SubmissionView(TemplateView):
    template_name = 'maricon/submission.html'
