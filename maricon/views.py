from django.contrib import messages
from django.contrib.auth import login
# import send email function
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from auth_login.forms import SignUpForm
from auth_login.models import User
from .models import Speaker, Faq, Sponsor, Schedule, Gallery, CommitteeMember, Committee, OTP


class AbstractView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(AbstractView, self).get_context_data(**kwargs)
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


class IndexView(AbstractView):
    template_name = 'new_maricon/index.html'


class CommitteeView(AbstractView):
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


class RegisterView(AbstractView):
    template_name = 'new_maricon/signup.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context['form'] = SignUpForm()
        return context

    def post(self, request):
        if request.method == 'POST':
            # Assuming you have a custom User model, adjust the form accordingly
            form = SignUpForm(request.POST)

            if form.is_valid():
                # Create a new user with the extended information
                user = form.save(commit=False)
                user.full_name = form.cleaned_data['full_name']
                user.gender = form.cleaned_data['gender']
                user.mobile_number = form.cleaned_data['mobile_number']
                user.save()
                messages.success(request, 'Account created successfully.')
                context = self.get_context_data()
                OTP.objects.create(user=user).send_email()
                context['otp'] = True
                context['email'] = user.email
                print("KKKKKKKKKKKKKKKKKKKKKKKK")
                return render(request, 'new_maricon/signup.html', context)
            else:
                print(form.errors.as_data())
                messages.error(request, 'Error creating the account. Please check the form.')

        return render(request, 'new_maricon/signup.html', self.get_context_data())


class OtpView(AbstractView):
    template_name = 'new_maricon/login.html'

    def post(self, request):
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        print(email, otp)
        if not email or not otp:
            return redirect('maricon:login')
        email = email.lower().strip()
        otp = otp.strip()
        otp_obj = OTP.objects.filter(user__email=email, otp=otp)
        if otp_obj.exists() and otp_obj.first().is_valid():
            print("kkkkkkkkkkkkkkkkkoii")
            login(request, otp_obj.first().user)
            return redirect('submission')
        else:
            context = self.get_context_data()
            context['err'] = True
            context['msg'] = "Invalid OTP"
            context['email'] = email
            context['otp'] = True
            return render(request, self.template_name, context)


def submission_view(request):
    if request.user.is_authenticated:
        return render(request, 'new_maricon/index.html')
    return redirect('login')


class LoginView(AbstractView):
    template_name = 'new_maricon/login.html'

    # handle post request
    def post(self, request):
        email = request.POST.get('email')
        context = self.get_context_data()

        if User.objects.filter(email=email).exists():
            otp = OTP.objects.create(user=User.objects.get(email=email))
            context['otp'] = True
            context['email'] = email
            otp.send_email()
            response = render(request, self.template_name, context)

            return response
        context['err'] = True
        context['msg'] = "Invalid Email Please Register to continue"
        print(context)
        return render(request, self.template_name, context)
