from django.shortcuts import render


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def user_index(request):
    return render(request,'user_index.html')

def user_dash(request):
    return render(request,'user_dash.html')

def user_view_companies(request):
    return render(request,'user_view_companies.html')
    
def company_dash(request):
    return render(request,'company_dash.html')
    