from django.shortcuts import render

# Create your views here.

def terms(request):
    return render(request, "pages/terms.html")


def testimonials(request):
    return render(request, "pages/testimonials.html")

def recover_password(request):
    return render(request, "pages/recover_password.html")
