from django.shortcuts import render

#This view is for dashboard
def dashboard(request):
    return render(request, "dashboard/dashboard.html")
