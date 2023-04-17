from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,BadHeaderError
from .models import DGA_Values
from .forms import *
from . import analysis
from .utils import get_plot_duval_1, get_plot_duval_4, get_plot_duval_5
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def form_view(request):
    if request.method == 'POST':
        form = DGA_form(request.POST)
        if form.is_valid():
            hydrogen = form.cleaned_data['hydrogen']
            carbon_di_oxide = form.cleaned_data['carbon_di_oxide']
            carbon_monoxide = form.cleaned_data['carbon_monoxide']
            ethylene = form.cleaned_data['ethylene']
            ethane = form.cleaned_data['ethane']
            methane = form.cleaned_data['methane']
            acetylene = form.cleaned_data['acetylene']
            tdcg = form.cleaned_data['tdcg']

            # saving the form data
            dga_values = DGA_Values.objects.create(hydrogen=hydrogen,carbon_di_oxide=carbon_di_oxide,carbon_monoxide=carbon_monoxide,
            ethylene=ethylene,ethane=ethane,methane=methane,acetylene=acetylene,tdcg=tdcg)
            # Rogers Ratio
            ratio_c2h2_c2h4, ratio_ch4_h2, ratio_c2h4_c2h6, result = analysis.roger_ratio(ethylene,ethane,methane, acetylene,hydrogen)


            # Duval's triangle one
            duval_1, duval_1_area = get_plot_duval_1(methane, ethylene, acetylene)

            # Duval's triangle four
            duval_4, duval_4_area = get_plot_duval_4(methane, hydrogen, ethane)

            # Duval's triangle four
            duval_5, duval_5_area = get_plot_duval_5(ethylene, methane, ethane)

            context = {
                'hydrogen': hydrogen,
                'carbon_di_oxide': carbon_di_oxide,
                'carbon_monoxide': carbon_monoxide,
                'ethylene': ethylene,
                'ethane': ethane,
                'methane': methane,
                'acetylene': acetylene,
                'tdcg': tdcg,
                'ratio_c2h2_c2h4': ratio_c2h2_c2h4,
                'ratio_ch4_h2': ratio_ch4_h2,
                'ratio_c2h4_c2h6': ratio_c2h4_c2h6,
                'result': result,
                'duval_1': duval_1,
                'duval_1_area': duval_1_area,
                'duval_4': duval_4,
                'duval_4_area': duval_4_area,
                'duval_5': duval_5,
                'duval_5_area': duval_5_area,
            }
            return render(request, 'data.html', context)
    
    else:
        form = DGA_form()
    return render(request, 'form.html',{'form':form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('submitted_contact.html', {
                'name' : name,
                'email' : email,
                'subject' : subject,
                'message' : message
                })

            send_mail(subject, 
            message, 
            settings.EMAIL_HOST_USER,
            ['samsul.alam.stp@gmail.com'], 
            fail_silently=False,)

            return redirect('contact_view')

    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form':form})



def about_view(request):
    return render(request, 'about.html')    
    
    