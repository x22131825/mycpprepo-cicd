from django.shortcuts import render, redirect
from .models import Parking
from django.contrib import messages
from .my_library import delete_parking_data


# Create your views here.
def index(request):
    data=Parking.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)


def insertData(request):
    
    if request.method=="POST":
        ownername=request.POST.get('ownername')
        contact=request.POST.get('contact')
        parkingslot=request.POST.get('parkingslot')
        entrydatetime=request.POST.get('entrydatetime')
        vehicle=request.POST.get('vehicletype')
        print(ownername,contact,parkingslot,entrydatetime,vehicle)
        query=Parking(ownername=ownername, contact=contact, parkingslot=parkingslot, entrydatetime=entrydatetime, vehicle=vehicle)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    
    return render(request,"index.html")

def updateData(request,id):

    if request.method=="POST":
        ownername=request.POST['ownername']
        contact=request.POST['contact']
        parkingslot=request.POST['parkingslot']
        entrydatetime=request.POST['entrydatetime']
        vehicle=request.POST['vehicletype']
        edit=Parking.objects.get(id=id)
        edit.ownername=ownername
        edit.contact=contact
        edit.parkingslot=parkingslot
        edit.entrydatetime=entrydatetime
        edit.vehicle=vehicle
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=Parking.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    delete_parking_data(id, request)
    return redirect("/")


# def deleteData(request,id):
#     d=Parking.objects.get(id=id)
#     d.delete()
#     messages.error(request,"Data Deleted Successfully", extra_tags='danger')
#     return redirect("/")