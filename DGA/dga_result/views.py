from django.shortcuts import render
from .models import DGA_Values
from .forms import *
from . import analysis
from .utils import get_plot_duval_1, get_plot_duval_4, get_plot_duval_5


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

            # Rogers Ratio
            ratio1, ratio2, result = analysis.roger_ratio(carbon_di_oxide, carbon_monoxide,ethylene,ethane)
            print(result)

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
                'ratio1': ratio1,
                'ratio2': ratio2,
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

def data_view(request):
    objects = DGA_Values.objects.all()
    context = {
        'objects':objects,
    }
    return render(request, 'data.html', context)
