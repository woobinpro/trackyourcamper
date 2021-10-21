from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
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
    return render(request,"admin/home.html")
def manageTrackerAlarm(request):
    return render(request,"admin/manageTrackerAlarm.html")
def manageVehicles(request):
    return render(request,"admin/manageVehicles.html")
def manageTrackerLoctionHistory(request):
    return render(request,"admin/manageTrackerLoctionHistory.html")
def manageBrands(request):
    return render(request,"admin/manageBrands.html")
def manageCampingPlace(request):
    return render(request,"admin/manageCampingPlace.html")
def manageOrders(request):
    return render(request,"admin/manageOrders.html")
def manageuser(request):
    return render(request,"admin/manageuser.html")
def manageMerchant(request):
    return render(request,"admin/manageMerchant.html")
def manageSecurityCompany(request):
    return render(request,"admin/manageSecurityCompany.html")
def manageSubscriptions(request):
    return render(request, "admin/manageSubscriptions.html")
def manageSubscriptionInvoice(request):
    return render(request,"admin/manageSubscriptionInvoice.html")
def manageTracker(request):
    return render(request,"admin/manageTracker.html")
def shopCategory(request):
    return render(request, "admin/shopCategory.html")
def manageForms(request):
    return render(request,"admin/manageForms.html")
def manageCustomerServicedata(request):
    return render(request, "admin/manageCustomerServicedata.html")
def manageCustomerGraphics(request):
    return render(request, "admin/manageCustomerGraphics.html")
def managePromotionCredit(request):
    return render(request,"admin/managePromotionCredit.html")
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