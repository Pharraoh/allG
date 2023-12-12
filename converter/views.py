from django.shortcuts import render

# Create your views here.
def alerts(request):
    return render(request, "converter/alerts.html")

def chart(request):
    return render(request, "converter/chart.html")

    
def converter(request):
    return render(request, "converter/converter.html")


def send_money(request):
    return render(request, "converter/send_money.html")
