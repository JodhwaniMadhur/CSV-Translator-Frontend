from django.shortcuts import render, redirect
from uploads.settings import SERVER_URL,MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
import requests
from django.http import HttpResponse
from uploads.core.models import downloadCSV
from uploads.core.forms import DocumentForm, DocumentForm2


def home(request):
    documents = downloadCSV.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        header = {'file_name':f"{myfile.name}"}
        requests.post(SERVER_URL+"/translate", headers=header,files={'file':open(MEDIA_ROOT+'/'+myfile.name,'rb')})
        return render(request, 'core/upload.html', {
            'uploaded_file_url': uploaded_file_url,
        })
    return render(request, 'core/upload.html')


def download_translated_csv(request):
    if request.method == 'POST':
        form = DocumentForm2(request.POST)
        if form.is_valid():
            file_name,language = request.POST.get('file_name'),request.POST.get('language')
            header = {'file_name':request.POST.get('file_name'),'language':request.POST.get('language')}
            requests.Response = requests.post(SERVER_URL+"/download-translated-csv", headers=header)
            file_path = MEDIA_ROOT+'/'+f"{language}_{file_name}"

            with open(file_path, "wb") as f:
                f.write(requests.Response._content)

            with open(file_path) as myfile:
                response = HttpResponse(myfile, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename='+f"{language}_{file_name}"
            return response
        else:
            return redirect('home')
    else:
        form = DocumentForm2()
    return render(request, 'core/download_translated_csv.html',{'form': form})


def download_previously_translated_csv(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            file_name,language = request.POST.get('file_name'),request.POST.get('language')
            header = {'file_name':request.POST.get('file_name'),'language':request.POST.get('language')}
            requests.Response = requests.post(SERVER_URL+"/download-previously-translated-csv", headers=header)
            file_path = MEDIA_ROOT+'/'+f"{language}_{file_name}"

            with open(file_path, "wb") as f:
                f.write(requests.Response._content)

            with open(file_path) as myfile:
                response = HttpResponse(myfile, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename='+f"{language}_{file_name}"
            return response
        else:
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/download_translated_csv.html',{'form': form})
