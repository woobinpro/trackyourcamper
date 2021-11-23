from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Aspnetusers, Vehicleset, Vehicletypemaster, Users, Brandset, Vehicleimages, Campingplaces, CamperRegulationansmaster, Brandmodeltypeset, Aspnetroles, Salutationmaster, Aspnetuserroles, Merchants, Merchantbrands, Securitycompanies, Packagelist, Trackerlisitem, Trackercategory, Trackeritemimages, TblHeadercontent, Websitegraphics, TblTempsubscriptiongocardlessdata
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import VehicleForm, BrandForm, CampingplaceForm, MerchantForm, SecurityCompanyForm, PackagelistForm, TrackerForm, HeaderContentForm
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import datetime
import os
import string    
import random
import hashlib
import requests
import urllib.parse
import math
import googlemaps
gmaps = googlemaps.Client(key="AIzaSyCRiaPjThG3eZJcdetH5veIK6nCrmjIIJM")

# Create your views here.

def home(request):
    return render(request, "home.html")

def stocklist(request):
    return render(request, "stocklist.html")

def shop(request, id):
    context = {
        "id":id,
    }
    return render(request,"shop.html",context)
def tracker(request, id):
    context = {
        "id":id,
    }
    return render(request,"tracker.html",context)
def cart(request):
    return render(request,"cart.html")
def login(request):
    return render(request,"login.html")
def subscription(request):
    return render(request,"subscription.html")
def contactus(request):
    return render(request,"contactUs.html")


def admin(request):
    users = get_list_from_sql("select count(*) as count from users inner join aspnetusers on users.UserID = aspnetusers.Id")
    vehicle_count = Vehicleset.objects.count()
    campingsite_count = Campingplaces.objects.count()
    return render(request,"admin/home.html",{ "user_count": users[0]['count'], "vehicle_count": vehicle_count, "campingsite_count": campingsite_count})
def manageTrackerAlarm(request):
    alarm_list = get_list_from_sql("select trackeralarms.Location_Date, trackeralarms.Location_time, trackeralarms.Command, trackeralarms.Response, trackeralarms.CommandStatus, new.LicensePlate, new.Firstname, new.Lastname from trackeralarms inner join (select vehicleset.LicensePlate, users.Firstname, users.Lastname, vehicleset.TrackerId from vehicleset left join users on users.ID = vehicleset.UserId) as new on trackeralarms.TrackerID = new.TrackerID order by trackeralarms.ID desc")
    return render(request,"admin/manageTrackerAlarm.html",{"alarm_list":alarm_list})
def manageVehicles(request):
    vehicle_list = get_list_from_sql("select vehicletypemaster.VehicleType, brandset.Name, vehicleset.ModelTypeName, vehicleset.Color, users.Firstname, users.Lastname, vehicleset.LicensePlate, vehicleset.BuildingYear, vehicleset.id, vehicleset.Istrackerconfiguration, vehicleset.Isgeofanceactive, vehicleset.Isoverspeedactive, vehicleset.Islowbatteryactive, vehicleset.Ispoweroffactive from vehicleset left join vehicletypemaster on vehicleset.VehicleType = vehicletypemaster.Id left join brandset on brandset.Id = vehicleset.BrandId left join users on users.ID = vehicleset.UserId")
    return render(request,"admin/manageVehicles.html", {"vehicle_list":vehicle_list})
def manageVehicleEdit(request, id):
    if request.method == 'POST':
        instance = Vehicleset.objects.get(id=id)
        form = VehicleForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            saveModelId(request.POST['modeltypename'], request.POST['brandid'])
            return redirect('/Admin/ManageVehicles')
        else:
            print(form.errors)
        
    vehicle_info = Vehicleset.objects.get(id=id)
    vehicle_type_list = Vehicletypemaster.objects.all()
    user_list = Users.objects.all()
    brand_list = Brandset.objects.all()
    return render(request,"admin/manageVehicleCreate.html",{"vehicle_info":vehicle_info,"type_list":vehicle_type_list,"user_list":user_list,"brand_list":brand_list})
def manageVehicleDelete(request, id):
    vehicle_info = Vehicleset.objects.get(id=id)
    vehicle_info.delete()
    return JsonResponse({'result':'success'})
def manageVehicleImageUpload(request, id):
    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        limit = 5 * 1024 * 1024
        if myfile.size > limit:
            return JsonResponse({'result':'fail','message':'Datei zu groß. Die Größe sollte 5 MiB nicht überschreiten.'})
        fs = FileSystemStorage()
        old_name, extension = os.path.splitext(myfile.name)
        new_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + extension
        filename = fs.save("static_in_env/upload/"+new_name, myfile)
        new_image = Vehicleimages(image=new_name)
        new_image.save()
        if id != 0:
            vehicle_info = Vehicleset.objects.get(id=id)
            vehicle_info.imageid = Vehicleimages.objects.latest('id').id
            vehicle_info.save()
            return JsonResponse({'result':'success','image_name':new_name})
        else:
            return JsonResponse({'result':'success','image_id':Vehicleimages.objects.latest('id').id})
    return JsonResponse({'result':'fail','message':'Datei ist nicht vorhanden.'})
def manageVehicleDetail(request, id):
    vehicle_info = get_list_from_sql("select vehicletypemaster.VehicleType as type_name, brandset.Name, vehicleset.*, users.Firstname, users.Lastname, vehicleimages.Image as img_name from vehicleset left join vehicletypemaster on vehicleset.VehicleType = vehicletypemaster.Id left join brandset on brandset.Id = vehicleset.BrandId left join users on users.ID = vehicleset.UserId left join vehicleimages on vehicleset.ImageId = vehicleimages.Id where vehicleset.id = " + str(id))
    # print(vehicle_info[0])
    return render(request,"admin/manageVehicleDetail.html", {"vehicle_info":vehicle_info[0], "vehicle_id":id})
def saveModelId(model, brandId):
    model_info = Brandmodeltypeset.objects.filter(brandid=brandId, name=model)
    if not model_info:
        new_model = Brandmodeltypeset(brandid=brandId, name=model)
        new_model.save()
def manageVehicleCreate(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            saveModelId(request.POST['modeltypename'], request.POST['brandid'])
            return redirect('/Admin/ManageVehicles')
    vehicle_type_list = Vehicletypemaster.objects.all()
    user_list = Users.objects.all()
    brand_list = Brandset.objects.all()
    return render(request,"admin/manageVehicleCreate.html",{"type_list":vehicle_type_list,"user_list":user_list,"brand_list":brand_list})
def manageTrackerLoctionHistory(request):
    return render(request,"admin/manageTrackerLoctionHistory.html")
def manageBrands(request):
    brand_list = get_list_from_sql("select brandset.Name, brandset.Id, brand_model.count as Count from brandset left join (select count(BrandId) as count, BrandId from brandmodeltypeset group by BrandId) as brand_model on brand_model.BrandId = brandset.Id")
    return render(request,"admin/manageBrands.html",{"brand_list":brand_list})
def getModelList(request, id):
    model_list = Brandmodeltypeset.objects.filter(brandid=id).values()
    return JsonResponse({"result":list(model_list)})
def manageBrandDetail(request, id):
    brand_info = Brandset.objects.get(id=id)
    model_list = get_list_from_sql("select * from brandmodeltypeset where BrandId =" + str(id))
    return render(request,"admin/manageBrandDetail.html",{"brand_info":brand_info,"model_list":model_list, "brand_id":id})
def manageBrandEdit(request, id):
    if request.method == 'POST':
        instance = Brandset.objects.get(id=id)
        form = BrandForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageBrands')
    brand_info = Brandset.objects.get(id=id)
    return render(request,"admin/manageBrandCreate.html",{"brand_info":brand_info})
def manageBrandDelete(request, id):
    brand = Brandset.objects.get(id=id)
    brand.delete()
    return JsonResponse({'result':'success'})
def modelDelete(request, id):
    model = Brandmodeltypeset.objects.get(id=id)
    model.delete()
    return JsonResponse({'result':'success'})
def manageBrandCreate(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageBrands')
        else:
            print(forms.errors())
    return render(request,"admin/manageBrandCreate.html")
def manageCampingPlace(request):
    campingPlace_list = get_list_from_sql("select campingplaces.ID, campingplaces.Name, campingplaces.address_city, campingplaces.address_road, campingplaces.address_degreeoflatitude, campingplaces.address_degreeoflongitude, users.Firstname, users.Lastname from campingplaces left join users on users.id = campingplaces.QwnerId order by campingplaces.ID")
    return render(request,"admin/manageCampingPlace.html",{"campingplace_list":campingPlace_list})
def manageCampingPlaceDelete(request, id):
    campingplace = Campingplaces.objects.get(id=id)
    campingplace.delete()
    return JsonResponse({'result':'success'})
def manageCampingPlaceDetail(request, id):
    campingplace_info = Campingplaces.objects.get(id=id)
    print(campingplace_info.qwnerid)
    user_info = Users.objects.get(id=campingplace_info.qwnerid)
    return render(request,"admin/manageCampingPlaceDetail.html",{"campingplace_info":campingplace_info,"user_info":user_info})
def manageCampingPlaceEdit(request, id):
    if request.method == 'POST':
        instance = Campingplaces.objects.get(id=id)
        form = CampingplaceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageCampingPlace')
        else:
            print(form.errors)
    camping_status = CamperRegulationansmaster.objects.all()
    user_list = Users.objects.all()
    campingplace_info = Campingplaces.objects.get(id=id)
    return render(request,"admin/manageCampingPlaceCreate.html",{"campingplace_info":campingplace_info,"camping_status":camping_status,'user_list':user_list})
def manageCampingPlaceCreate(request):
    if request.method == 'POST':
        form = CampingplaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageCampingPlace')
    camping_status = CamperRegulationansmaster.objects.all()
    user_list = Users.objects.all()
    return render(request,"admin/manageCampingPlaceCreate.html", {"camping_status":camping_status,'user_list':user_list})
def manageOrders(request):
    return render(request,"admin/manageOrders.html")
def manageuser(request):
    users = get_list_from_sql("select users.UserID as id, users.Firstname as firstname, users.Lastname as lastname, users.Email as email, campingplaces.Name as campingsite_name, GROUP_CONCAT(aspnetroles.Name) as role_name, users.DOB as birthday, aspnetusers.LockoutEnabled as lock_status, aspnetuserroles.RoleId as role_id from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID left join aspnetroles on aspnetuserroles.RoleId like CONCAT('%', CONCAT(aspnetroles.Id, '%')) left join campingplaces on users.ResponsibleForCampingPlaceId = campingplaces.ID group by id, firstname, lastname, email, campingsite_name, birthday, lock_status, role_id, users.ID order by users.ID desc")
    admin_users = get_list_from_sql("select count(*) as count from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID left join aspnetroles on aspnetuserroles.RoleId like CONCAT('%', CONCAT(aspnetroles.Id, '%')) where aspnetroles.Name like 'Admin'")
    role_list = Aspnetroles.objects.all()
    return render(request,"admin/manageUser.html",{"users":users, "admin_users":admin_users[0]['count'], "role_list":role_list})
def generateUserId(id):
    customer_id = "T-"
    for i in range(8-len(str(id))):
        customer_id += "0"
    customer_id += str(id)
    # ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))  
    # ran += "-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k = 4))
    # ran += "-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k = 4))
    # ran += "-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k = 4))
    # ran += "-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k = 12))
    # print(str(ran))
    return customer_id

def make_password(password):
    assert password
    hash = hashlib.md5(password.encode('utf8')).hexdigest()
    return hash
def getCoordinate(request, street):
    loc = gmaps.geocode(street.replace("+"," "))
    if len(loc) > 0:
        coordinate = loc[0]['geometry']['location'] 
        return JsonResponse({"result":"success",'lat':coordinate['lat'],"lng":coordinate['lng']})
    else:
        return JsonResponse({"result":"fail"})
def check_password(hash, password):
    generated_hash = make_password(password)
    return hash == generated_hash
def manageUserDelete(request, id):
    aspuser = Aspnetusers.objects.get(id=id)
    aspuser.delete()
    user = Users.objects.get(userid=id)
    user.delete()
    execute_sql("Delete from aspnetuserroles where UserId like '" + id + "'")
    return JsonResponse({'result':'success'})
def manageUserDetail(request, id):
    user_info = get_list_from_sql("select users.ID as id, users.Firstname as firstname, users.Lastname as lastname, users.Email as email, users.Phoneno as phone, users.Address_City as city, users.Address_Country as country, users.Address_State as state, users.Address_Street as street, users.Address_Postal as postal, users.Address_Latitude as lat, users.Address_Longitude as lon, campingplaces.Name as campingsite_name, GROUP_CONCAT(aspnetroles.Name) as role_name, users.DOB as birthday, aspnetusers.LockoutEnabled as lock_status, aspnetuserroles.RoleId as role_id, salutationmaster.salutation as salutation from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID left join aspnetroles on aspnetuserroles.RoleId like CONCAT('%', CONCAT(aspnetroles.Id, '%')) left join campingplaces on users.ResponsibleForCampingPlaceId = campingplaces.ID left join salutationmaster on salutationmaster.ID = users.salutation where users.UserID like '"+ id +"' group by id, firstname, lastname, email, phone, city, country, state, street, postal, lat, lon, campingsite_name, birthday, lock_status, role_id, salutation")
    vehicle_list = get_list_from_sql("select vehicletypemaster.VehicleType as v_type, vehicleset.LicensePlate as license, vehicleset.Id as id from vehicleset left join vehicletypemaster on vehicletypemaster.Id = vehicleset.VehicleType where vehicleset.UserId = "+str(user_info[0]['id']))
    return render(request,"admin/manageUserDetail.html",{"user_info":user_info[0], "vehicle_list":vehicle_list, "user_id":id})
def manageUserChangePassword(request, id):
    if request.method == 'POST':
        aspuser = Aspnetusers.objects.get(id=id)
        aspuser.passwordhash = make_password(request.POST['password'])
        aspuser.save()
        return redirect('/Admin/ManageUser')
    user_info = Users.objects.get(userid=id)
    return render(request,"admin/manageUserChangePassword.html",{'user_info':user_info})
def manageUserEdit(request, id):
    if request.method == 'POST':
        aspuser = Aspnetusers.objects.get(id=id)
        aspuser.email=request.POST['email']
        aspuser.phonenumber=request.POST['phoneno']
        aspuser.save()
        user = Users.objects.get(userid=id)
        user.salutation=request.POST['salutation']
        user.firstname=request.POST['firstname']
        user.lastname=request.POST['lastname']
        user.email=request.POST['email']
        user.phoneno=request.POST['phoneno']
        user.dob=request.POST['dob']
        user.responsibleforcampingplaceid=request.POST['responsibleforcampingplaceid']
        user.address_city=request.POST['address_city']
        user.address_country=request.POST['address_country']
        user.address_street=request.POST['address_street']
        user.address_postal=request.POST['address_postal']
        user.address_state=request.POST['address_state']
        user.address_latitude=request.POST['address_latitude']
        user.address_longitude=request.POST['address_longitude']
        user.lastupdatedon=datetime.datetime.now()
        user.save()
        execute_sql("update aspnetuserroles set RoleId = '" + request.POST['user_roles'] + "' where UserId like '"+ id + "'")
        
        return redirect('/Admin/ManageUser')
    user_info = get_list_from_sql("select users.*, aspnetusers.LockoutEnabled as lock_status, aspnetuserroles.RoleId as role_id from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID where users.UserID like '" + id + "'")
    salutation_list = Salutationmaster.objects.all()
    campingsite_list = Campingplaces.objects.all()
    role_list = Aspnetroles.objects.all()
    return render(request,"admin/manageUserCreate.html",{"salutation_list":salutation_list,"campingsite_list":campingsite_list,"role_list":role_list,"user_info":user_info[0]})
def manageUserCreate(request):
    if request.method == 'POST':
        new_user = Users(salutation=request.POST['salutation'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'],phoneno=request.POST['phoneno'],dob=request.POST['dob'],responsibleforcampingplaceid=request.POST['responsibleforcampingplaceid'], address_city=request.POST['address_city'],address_country=request.POST['address_country'],address_street=request.POST['address_street'],address_postal=request.POST['address_postal'],address_state=request.POST['address_state'],address_latitude=request.POST['address_latitude'],address_longitude=request.POST['address_longitude'],createdon=datetime.datetime.now())
        new_user.save()
        last_id = Users.objects.latest('id').id
        user_id = generateUserId(last_id)
        last_user = Users.objects.get(id=last_id)
        last_user.userid = user_id
        last_user.save()
        new_aspuser = Aspnetusers(id=user_id,email=request.POST['email'],passwordhash=make_password(request.POST['password']),phonenumber=request.POST['phoneno'])
        new_aspuser.save()
        new_userrole = Aspnetuserroles(userid=user_id,roleid=request.POST['user_roles'])
        new_userrole.save()
        return redirect('/Admin/ManageUser')
    salutation_list = Salutationmaster.objects.all()
    campingsite_list = Campingplaces.objects.all()
    role_list = Aspnetroles.objects.all()
    return render(request,"admin/manageUserCreate.html",{"salutation_list":salutation_list,"campingsite_list":campingsite_list,"role_list":role_list})
def manageUserChangeRock(request, user_id, value):
    user = Aspnetusers.objects.get(id=user_id)
    user.lockoutenabled = value
    user.save()
    return JsonResponse({'result':'success'})
def manageMerchant(request):
    merchant_list = Merchants.objects.all()
    return render(request,"admin/manageMerchant.html",{"merchant_list":merchant_list})
def manageMerchantChangeActiveStatus(request, merchant_id, value):
    merchant = Merchants.objects.get(id=merchant_id)
    merchant.isactive = value
    merchant.save()
    return JsonResponse({'result':'success'})
def getIncludingStatus(lat1, lng1, lat2, lng2, radius):
    # distance = math.acos(math.sin(float(lat1)) *  math.sin(float(lat2)) + math.cos(float(lat1)) * math.cos(float(lat2)) * math.cos(float(lng2) - float(lng1))) * 6371
    R = 6373.0
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lng1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lng2))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    print(distance)
    return distance < float(radius)
def searchFromCoordinate(request):
    loc = gmaps.geocode(request.GET["center_address"].replace("+"," "))
    response = loc[0]['geometry']['location'] 
    coordinate_list = request.GET["list_coordinates"].split("$")
    result = []
    for coordinate in coordinate_list:
        latLng = coordinate.split(",")
        if latLng[0]=="None" or latLng[1]=="None":
            result.append(False)
        else:
            result.append(getIncludingStatus(response["lat"],response["lng"],latLng[0],latLng[1],request.GET['radius']))
    return JsonResponse({'result':result})
def manageMerchantDelete(request, id):
    merchant = Merchants.objects.get(id=id)
    merchant.delete()
    return JsonResponse({'result':'success'})
def manageMerchantDetail(request, id):
    merchant_info = Merchants.objects.get(id=id)
    user_info = Users.objects.get(id=merchant_info.userid)
    brand_list = Brandset.objects.all()
    merchant_brands = get_list_from_sql("select GROUP_CONCAT(BrandId) as brands from merchantbrands where MerchantId = "+str(id)+" group by MerchantId")
    return render(request,"admin/manageMerchantDetail.html",{"merchant_info":merchant_info,"user_info":user_info,"brand_list":brand_list,"merchant_brands":merchant_brands[0]['brands']})
def manageMerchantEdit(request, id):
    if request.method == 'POST':
        instance = Merchants.objects.get(id=id)
        form = MerchantForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            merchant_brands = Merchantbrands.objects.filter(merchantid=id)
            merchant_brands.delete()
            brand_list = request.POST["merchant_brands"].split(",")
            for brand_id in brand_list:
                new_merchant_brand = Merchantbrands(merchantid=id, brandid=brand_id)
                new_merchant_brand.save()
            return redirect('/Admin/ManageMerchant')
    merchant_info = Merchants.objects.get(id=id)
    merchant_brands = get_list_from_sql("select GROUP_CONCAT(BrandId) as brands from merchantbrands where MerchantId = "+str(id)+" group by MerchantId")
    # print(merchant_brands[0]['brands'])
    user_list = Users.objects.all()
    brand_list = Brandset.objects.all()
    return render(request,"admin/manageMerchantCreate.html",{"merchant_info":merchant_info,"user_list":user_list,"brand_list":brand_list,"merchant_brands":merchant_brands[0]['brands']})
def manageMerchantCreate(request):
    if request.method == 'POST':
        form = MerchantForm(request.POST)
        if form.is_valid():
            form.save()
            brand_list = request.POST["merchant_brands"].split(",")
            for brand_id in brand_list:
                new_merchant_brand = Merchantbrands(merchantid=Merchants.objects.latest('id').id, brandid=brand_id)
                new_merchant_brand.save()
            return redirect('/Admin/ManageMerchant')
        else:
            print(form.errors)
    user_list = Users.objects.all()
    brand_list = Brandset.objects.all()
    return render(request,"admin/manageMerchantCreate.html",{"user_list":user_list,"brand_list":brand_list})
def manageSecurityCompany(request):
    company_list = get_list_from_sql("select securitycompanies.*, users.Firstname, users.Lastname from securitycompanies left join users on users.ID = securitycompanies.OwnerId")
    return render(request,"admin/manageSecurityCompany.html",{"security_company_list":company_list})
def manageSecurityCompanyDetail(request, id):
    company_info = Securitycompanies.objects.get(id=id)
    user_info = Users.objects.get(id=company_info.ownerid)
    return render(request,"admin/manageSecurityCompanyDetail.html",{"user_info":user_info,"company_info":company_info})
def manageSecurityCompanyEdit(request, id):
    if request.method == 'POST':
        instance = Securitycompanies.objects.get(id=id)
        form = SecurityCompanyForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSecurityCompany')
    user_list = Users.objects.all()
    company_info = Securitycompanies.objects.get(id=id)
    return render(request,"admin/manageSecurityCompanyCreate.html",{"user_list":user_list,"company_info":company_info})
def manageSecurityCompanyCreate(request):
    if request.method == 'POST':
        form = SecurityCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSecurityCompany')
        else:
            print(form.errors)
    user_list = Users.objects.all()
    return render(request,"admin/manageSecurityCompanyCreate.html",{"user_list":user_list})
def manageSecurityCompanyDelete(request, id):
    company_info = Securitycompanies.objects.get(id=id)
    company_info.delete()
    return JsonResponse({'result':'success'})
def manageSubscriptionEdit(request, id):
    if request.method == 'POST':
        instance = Packagelist.objects.get(id=id)
        form = PackagelistForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSubscriptions')
        else:
            print(form.errors)
    subscription_info = Packagelist.objects.get(id=id)
    return render(request,"admin/manageSubscriptionCreate.html",{"subscription_info":subscription_info})
def manageSubscriptionDetail(request, id):
    subscription_info = Packagelist.objects.get(id=id)
    return render(request,"admin/manageSubscriptionDetail.html",{"subscription_info":subscription_info})
def manageSubscriptionCreate(request):
    if request.method == 'POST':
        form = PackagelistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSubscriptions')
        else:
            print(form.errors)
    return render(request,"admin/manageSubscriptionCreate.html",{})
def manageSubscriptions(request):
    subscription_list = Packagelist.objects.all()
    return render(request, "admin/manageSubscriptions.html",{"subscription_list":subscription_list})
def manageSubscriptionChangeActiveStatus(request, id, value):
    subscription = Packagelist.objects.get(id=id)
    subscription.isactive = value
    subscription.save()
    return JsonResponse({'result':'success'})
def manageSubscriptionDelete(request, id):
    subscription = Packagelist.objects.get(id=id)
    subscription.delete()
    return JsonResponse({'result':'success'})
def manageSubscriptionInvoice(request):
    return render(request,"admin/manageSubscriptionInvoice.html")
def manageTracker(request):
    tracker_list = get_list_from_sql("select trackerlisitem.Id as id, trackercategory.Tracker_Category as category_name, trackerlisitem.Trackername as tracker_name, trackerlisitem.Articlenumber as article_number, trackerlisitem.Price as price, trackerlisitem.DicountPrice as discount_price, trackerlisitem.Isactive as isactive from trackerlisitem left join trackercategory on trackerlisitem.TrackerCategory = trackercategory.Id order by id")
    return render(request,"admin/manageTracker.html",{"tracker_list":tracker_list})
def manageTrackerImageUpload(request, id):
    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        limit = 5 * 1024 * 1024
        if myfile.size > limit:
            return JsonResponse({'result':'fail','message':'Datei zu groß. Die Größe sollte 5 MiB nicht überschreiten.'})
        fs = FileSystemStorage()
        old_name, extension = os.path.splitext(myfile.name)
        new_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + extension
        filename = fs.save("static_in_env/upload/"+new_name, myfile)
        new_image = Trackeritemimages(imagename=new_name,trackerid=id)
        new_image.save()
        return JsonResponse({'result':'success','image_name':new_name,'image_id':Trackeritemimages.objects.latest('id').id})
    return JsonResponse({'result':'fail','message':'Datei ist nicht vorhanden.'})
def manageTrackerImageDelete(request, id):
    image = Trackeritemimages.objects.get(id=id)
    image.delete()
    return JsonResponse({'result':'success'})

def manageTrackerEdit(request, id):
    if request.method == 'POST':
        instance = Trackerlisitem.objects.get(id=id)
        form = TrackerForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageTracker')
        else:
            print(form.errors)
    tracker = Trackerlisitem.objects.get(id=id)
    category_list = Trackercategory.objects.all()
    tracker_images = Trackeritemimages.objects.filter(trackerid=id)
    return render(request,"admin/manageTrackerCreate.html",{"category_list":category_list,"tracker_info":tracker,"tracker_images":tracker_images})
def manageTrackerCreate(request):
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageTracker')
        else:
            print(form.errors)
    category_list = Trackercategory.objects.all()
    return render(request,"admin/manageTrackerCreate.html",{"category_list":category_list})
def manageTrackerDetail(request,id):
    tracker = Trackerlisitem.objects.get(id=id)
    category_info = Trackercategory.objects.get(id=tracker.trackercategory)
    tracker_images = Trackeritemimages.objects.filter(trackerid=id)
    return render(request,"admin/manageTrackerDetail.html",{"category_name":category_info.tracker_category,"tracker_info":tracker,"tracker_images":tracker_images})
def manageTrackerChangeActiveStatus(request, id, value):
    tracker = Trackerlisitem.objects.get(id=id)
    tracker.isactive = value
    tracker.save()
    return JsonResponse({'result':'success'})
def manageTrackerDelete(request, id):
    tracker = Trackerlisitem.objects.get(id=id)
    tracker.delete()
    return JsonResponse({'result':'success'})
def shopCategory(request):
    category_list = Trackercategory.objects.all()
    return render(request, "admin/shopCategory.html",{"category_list":category_list})
def shopCategorySubmit(request):
    if request.GET["id"] == 'new':
        category = Trackercategory(tracker_category=request.GET["name"], isactive=request.GET["isactive"])
        category.save()
        return JsonResponse({'result':'success','type':'new','id':Trackercategory.objects.latest('id').id})
    else:
        category = Trackercategory.objects.get(id=request.GET['id'])
        category.tracker_category = request.GET["name"]
        category.isactive = request.GET["isactive"]
        category.save()
        return JsonResponse({'result':'success','type':'update'})
def shopCategoryDelete(request, id):
    category = Trackercategory.objects.get(id=id)
    category.delete()
    return JsonResponse({'result':'success'})
def manageForms(request):
    return render(request,"admin/manageForms.html")
def manageCustomerServicedata(request):
    if request.method == 'POST':
        if request.POST["id"] != "":
            instance = TblHeadercontent.objects.get(id=request.POST["id"])
            form = HeaderContentForm(request.POST, instance=instance)
        else:
            form = HeaderContentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    header_content = TblHeadercontent.objects.all()
    if len(header_content) > 0:
        return render(request, "admin/manageCustomerServicedata.html",{"header_content":header_content[0]})
    else:
        return render(request, "admin/manageCustomerServicedata.html")
def saveFile(file):
    fs = FileSystemStorage()
    old_name, extension = os.path.splitext(file.name)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 4)) 
    new_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ran + extension
    filename = fs.save("static_in_env/upload/"+new_name, file)
    return new_name
def manageCustomerGraphics(request):
    if request.method == 'POST':
        if "banner_image1" in request.FILES: banner_image1 = request.FILES['banner_image1']
        if "banner_image2" in request.FILES: banner_image2 = request.FILES['banner_image2']
        if "banner_image3" in request.FILES: banner_image3 = request.FILES['banner_image3']
        if "product_image1" in request.FILES: product_image1 = request.FILES['product_image1']
        if "product_image2" in request.FILES: product_image2 = request.FILES['product_image2']
        if "product_image3" in request.FILES: product_image3 = request.FILES['product_image3']
        if "shop_background_image" in request.FILES: shop_background = request.FILES['shop_background_image']
        if request.POST["id"] != "":
            graphics = Websitegraphics.objects.get(id=request.POST["id"])
        else:
            graphics = Websitegraphics()
        if "banner_image1" in request.FILES: graphics.banner_image1 = saveFile(banner_image1)
        if "banner_image2" in request.FILES: graphics.banner_image2 = saveFile(banner_image2)
        if "banner_image3" in request.FILES: graphics.banner_image3 = saveFile(banner_image3)
        if "product_image1" in request.FILES: graphics.product_image1 = saveFile(product_image1)
        if "product_image2" in request.FILES: graphics.product_image2 = saveFile(product_image2)
        if "product_image3" in request.FILES: graphics.product_image3 = saveFile(product_image3)
        if "shop_background_image" in request.FILES: graphics.shop_background_image = saveFile(shop_background)
        graphics.save()
    result = Websitegraphics.objects.all()
    if len(result) > 0:
        return render(request, "admin/manageCustomerGraphics.html",{"graphics":result[0]})    
    else:
        return render(request, "admin/manageCustomerGraphics.html")
def managePromotionCredit(request):
    promotionCreditList = TblTempsubscriptiongocardlessdata.objects.all()
    return render(request,"admin/managePromotionCredit.html",{"catalog_list":promotionCreditList})
def reviewratting(request):
    return render(request,"admin/reviewratting.html")
def termsOfService(request):
    return render(request,"admin/termsOfService.html")
def adminPrivacypolicy(request):
    return render(request,"admin/adminPrivacypolicy.html")
def adminImprint(request):
    return render(request,"admin/adminImprint.html")
def adminChangePassword(request):
    return render(request,"admin/adminChangePassword.html")
def get_list_from_sql(str):
    cursor = connection.cursor()    
    cursor.execute(str)
    row = dictfetchall(cursor)
    return row
def execute_sql(str):
    cursor = connection.cursor()    
    cursor.execute(str)
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]