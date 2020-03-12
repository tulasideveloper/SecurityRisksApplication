from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SecurityRiskAspects_Form, SecurityRiskAspects_Edit
from .models import SecurityRiskAspects
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request, 'base.html')

def Load_AddRiskAspect(request):
    if request.method == 'POST':
        AddRiskAspect = SecurityRiskAspects_Form(request.POST)
        if AddRiskAspect.is_valid():
            AddRiskAspect.save()
            return redirect('Load_HomePage')
    else:
        AddRiskAspect = SecurityRiskAspects_Form()
    return render(request, 'RiskAspects_t/AddRiskAspect.html', {'AddRiskAspect':AddRiskAspect})

def Load_HomePage(request):
    queryset_list = SecurityRiskAspects.objects.all()
    
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(RiskAspect_Name__icontains=query)|
            Q(RiskAspect_Description__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    context_data = {
        'object_list':queryset,
        'title':'List',
        'page_request_var':page_request_var
    }

    return render(request, 'RiskAspects_t/Home.html',context_data)


def Load_ViewRiskAspect(request, id):
    objViewRiskAspect = SecurityRiskAspects.objects.get(id=id)
    return render(request, 'RiskAspects_t/ViewRiskAspect.html',{'objViewRiskAspect':objViewRiskAspect})

def Load_EditRiskAspect(request,id):
    objEditRiskAspect = SecurityRiskAspects.objects.get(id=id)    
    if request.method == 'POST':
        form_SecurityRiskAspects_Edit = SecurityRiskAspects_Edit(request.POST, instance=objEditRiskAspect)       
        if form_SecurityRiskAspects_Edit.is_valid():
            form_SecurityRiskAspects_Edit.save()
            return redirect('Load_HomePage')
    else:
        form_SecurityRiskAspects_Edit = SecurityRiskAspects_Edit(instance=objEditRiskAspect)    
        return render(request, 'RiskAspects_t/EditRiskAspect.html', {'form_SecurityRiskAspects_Edit':form_SecurityRiskAspects_Edit})
