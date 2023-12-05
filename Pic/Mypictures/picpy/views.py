from django.shortcuts import render
from .forms import HandleImage



def Home(request):
    tmp="htmls/main.html"
    if request.method=="POST":
        form=HandleImage(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            imgobj=form.instance
            

            return render(request,tmp,{"form":form,"imobj":imgobj})
    else:
        form=HandleImage()

    return render(request,tmp,{"form":form})