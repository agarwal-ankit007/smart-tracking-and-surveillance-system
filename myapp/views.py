from django.shortcuts import render, redirect
from myapp.forms import Employeeform
from myapp.models import Employee
from myapp.models import Person_Info
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os


def index(request):
    return render(request, "wlcm.html")


def Signup(request):
    if request.method == "POST":
        print(request.POST)
        emp = Employee.objects.filter(Employee_Id=request.POST["id"])
        if emp.exists():
            messages.error(request, "Employee with that Employee ID already exists")
            return redirect("/")
        else :
            form = Employee.objects.create(
                Employee_Id=request.POST["id"],
                Emplyee_Name=request.POST['name'],
                Email_Id=request.POST['email'],
                Contact_No=request.POST['contact'],
                Address=request.POST['address'],
                Username=request.POST['username'],
                Password=request.POST['password']
            )
            #form.save()
        #form = Employeeform(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/")
                except:
                    pass
    else:
        print("hey")
        #form = Employeeform()
    return render(request, "Signup.html")


def login(request):
    if request.method == "POST":
        # verification needed
        return redirect("/missing_details")
    else:
        print("hey")
    return render(request, "login.html")
folder=''
folderpath=''
def missing_details(request):
    is_private = request.POST.get('is_private', False)
    if request.method == "POST":
        print("entered")
        myfile = request.FILES['image'] if 'image' in request.FILES else None
        if myfile:
            print("welcome")
            print(myfile.name)
            #fs = FileSystemStorage()
            #filename = fs.save(myfile.name, myfile)
            #uploaded_file_url = fs.url(filename)
            #---------------TRIAL--------------#
            from PIL import Image
            import PIL

            #url = "C:/Users/vivek/PycharmProjects/webapp"+uploaded_file_url.rsplit('.', 1)[0]
            url = "C:/Users/vivek/PycharmProjects/webapp/media/"+(myfile.name).split(".")[0]
            print(url)
            os.mkdir(url, mode=777)
            url+="/"
            #url+=(uploaded_file_url.rsplit('.', 1)[0]).split("/")[-1]
            # creating a image object (main image)
            #img = Image.new('RGB', (60, 30), color='red')
            #img.save(url+".jpeg")
            url += myfile.name
            im1 = Image.open(myfile)

            # save a image using extension
            im1 = im1.save(url)
            uploaded_file_url="media/"+(myfile.name).split(".")[0]+"/"+myfile.name

            #-----------TRIAL OVER----------#

            #global folder
            #folder = uploaded_file_url[1:]
            form=Person_Info.objects.create(
                Missing_Id=request.POST['mid'],
                Name=request.POST['fullname'],
                Image=uploaded_file_url,
                Age=request.POST['Age'],
                Email_Id=request.POST['email'],
                Contact_No=request.POST['contact'],
                Address=request.POST['Address'],
                Date_Missing=request.POST['dt_missing'],
                Date_Found='1111-11-11',
                Status=False,
                Employee_Id_id=request.POST['e_id'],
            )
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        print("failed")
        #form = Employeeform()
    return render(request, "missing_details.html")

# def path(request):
#     global folder, folderpath
#     folderpath = folder.rsplit('.', 1)[0]
#     os.mkdir(folderpath)
#     return [folder,folderpath]