from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from upload_process.controller import execute_script


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def homePage(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.getlist('sentFile')
        fs = FileSystemStorage()
        for f in uploaded_file:
            fs.save(f.name, f)

        execute_script()


    context = {}
    return render(request, 'home.html', context)
