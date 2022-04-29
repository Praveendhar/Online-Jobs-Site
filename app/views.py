from django.shortcuts import render


def login(request):
    return render(request,'login.html')

def user_register(request):
    return render(request,'user_register.html')

def company_register(request):
    return render(request,'company_register.html')

def user_index(request):
    return render(request,'user_index.html')

def user_dash(request):
    return render(request,'user_dash.html')

def user_view_companies(request):
    return render(request,'user_view_companies.html')

def user_view_company(request):
    return render(request,'user_view_company.html')
    
def company_dash(request):
    return render(request,'company_dash.html')

def company_index(request):
    return render(request,'company_index.html')

def company_dash(request):
    return render(request,'company_dash.html')
    