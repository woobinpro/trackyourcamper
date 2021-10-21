from django.urls import path

from .views import *

app_name = 'track'

urlpatterns = [
   path('', index,name = "index"),
   path('Stocklist', stocklist, name="stocklist"),
   path('Shop/Index/<int:id>', shop, name="shop"),
   path('Tracker/Detail/<int:id>', tracker, name="tracker"),
   path('Cart', cart, name="cart"),
   path('Login', login, name="login"),
   path('Subscription', subscription, name='subscription'),
   path('Contactus', contactus, name='contactus'),

   path('Admin', admin, name="admin"),
   path('Admin/ManageTrackerAlarm', manageTrackerAlarm, name="manageTrackerAlarm"),
   path('Admin/ManageVehicles', manageVehicles, name="manageVehicles"),
   path('Admin/ManageTrackerLoctionHistory', manageTrackerLoctionHistory, name="manageTrackerLoctionHistory"),
   path('Admin/ManageBrands', manageBrands, name="manageBrands"),
   path('Admin/ManageCampingPlace', manageCampingPlace, name="manageCampingPlace"),
   path('Admin/ManageOrders', manageOrders, name="manageOrders"),
   path('Admin/ManageUser', manageuser, name="manageuser"),
   path("Admin/ManageMerchant", manageMerchant, name="manageMerchant"),
   path("Admin/ManageSecurityCompany", manageSecurityCompany, name="manageSecurityCompany"),
   path("Admin/ManageSubscriptions", manageSubscriptions, name="manageSubscriptions"),
   path("Admin/Admin/ManageSubscriptionInvoice", manageSubscriptionInvoice, name="manageSubscriptionInvoice"),
   path("Admin/ManageTracker", manageTracker, name="manageTracker"),
   path("Admin/ShopCategory", shopCategory, name="shopCategory"),
   path("Admin/ManageForms", manageForms, name="manageForms"),
   path("Admin/ManageCustomerServicedata", manageCustomerServicedata, name="manageCustomerServicedata"),
   path("Admin/ManageCustomerServicedata/CustomerGraphics", manageCustomerGraphics, name="manageCustomerGraphics"),
   path("Admin/ManagePromotionCredit", managePromotionCredit, name="managePromotionCredit"),
   path("Admin/Reviewratting", reviewratting, name="reviewratting"),
   path("Admin/TermsOfService", termsOfService, name="termsOfService"),
   path("Admin/AdminPrivacypolicy", adminPrivacypolicy, name="adminPrivacypolicy"),
   path("Admin/AdminImprint", adminImprint, name="adminImprint"),
   path("Admin/Adminchangepassword", adminChangePassword, name="adminChangePassword")
]