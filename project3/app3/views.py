from django.shortcuts import render
from .models import foodcart


# Create your views here.
def index(request):

    cart1 = foodcart.objects.all()
    
    return render(request,'index.html',{'cart':cart1})
