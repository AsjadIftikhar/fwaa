from django.http import HttpResponseRedirect
from django.shortcuts import render


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def homePage(request):
    if request.method == 'POST':
        f = request.FILES['sentFile']  # here you get the files needed
        print(f.name)
        print(f.size)
    context = {}
    return render(request, 'home.html', context)
