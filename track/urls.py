from django.urls import path

from .views import *

app_name = 'track'

urlpatterns = [
   path('', home, name="home"),
   path('Stocklist', stocklist, name="stocklist"),
   path('Shop/Index/<int:id>', shop, name="shop"),
   path('Tracker/Detail/<int:id>', tracker, name="tracker"),
   path('Cart', cart, name="cart"),
   path('setCartQty', setCartQty, name="setCartQty"),
   path('checkEmailExist', checkEmailExist, name="checkEmailExist"),
   path('Myaccount', myAccount, name="myAccount"),
   path('Usersubscription', userSubscription, name="userSubscription"),
   path('Usersubscription/detail', userSubscriptionDetail, name="userSubscriptionDetail"),
   path('saveBillingAddress', saveBillingAddress, name="saveBillingAddress"),
   path('saveShippingAddress', saveShippingAddress, name="saveShippingAddress"),
   path('Checkout', checkout, name="checkout"),
   path('Checkout/Checkoutaddress', checkoutAddress, name="checkoutAddress"),
   path('Checkout/Checkoutconfirm', checkoutConfirm, name="checkoutConfirm"),
   path('Checkout/Receipt', checkoutReceipt, name="checkoutReceipt"),
   # path('paypal/', include('paypal.standard.ipn.urls')),
   path('payment', payment, name='payment'),
   path('removeCart', removeCart, name="removeCart"),
   path('Login', login, name="login"),
   path('Subscription', subscription, name='subscription'),
   path('Contactus', contactus, name='contactus'),
   path('Conditions',conditions, name="conditions"),
   path("Privacypolicy",privacypolicy,name="privacypolicy"),
   path("imprint",imprint,name="imprint"),

   path('Admin', admin, name="admin"),
   path('Admin/Login', admin_login, name="admin_login"),
   path('Admin/Logout', logout, name="logout"),
   path('Admin/ManageTrackerAlarm', manageTrackerAlarm, name="manageTrackerAlarm"),
   path('Admin/ManageVehicles', manageVehicles, name="manageVehicles"),
   path('Admin/ManageVehicles/Edit/<int:id>', manageVehicleEdit, name="manageVehicleEdit"),
   path('Admin/ManageVehicles/Delete/<int:id>', manageVehicleDelete, name="manageVehicleDelete"),
   path('Admin/ManageVehicles/Detail/<int:id>', manageVehicleDetail, name="manageVehicleDetail"),
   path('Admin/ManageVehicles/getModelList/<int:id>', getModelList, name="getModelList"),
   path('Admin/ManageVehicles/ImageUpload/<int:id>', manageVehicleImageUpload, name="manageVehicleImageUpload"),
   path("Admin/ManageVehicle/Create", manageVehicleCreate, name="manageVehicleCreate"),
   path('Admin/ManageTrackerLocationHistory', manageTrackerLocationHistory, name="manageTrackerLocationHistory"),
   path('Admin/ManageBrands', manageBrands, name="manageBrands"),
   path('Admin/ManageBrands/Edit/<int:id>', manageBrandEdit, name="manageBrandEdit"),
   path('Admin/ManageBrands/Delete/<int:id>', manageBrandDelete, name="manageBrandDelete"),
   path('Admin/ManageBrands/Detail/<int:id>', manageBrandDetail, name="manageBrandDetail"),
   path("Admin/ManageBrand/Create", manageBrandCreate, name="manageBrandCreate"),
   path("Admin/ModelDelete/<int:id>", modelDelete, name="modelDelete"),
   path('Admin/ManageCampingPlace', manageCampingPlace, name="manageCampingPlace"),
   path('Admin/ManageCampingPlaces/Delete/<int:id>', manageCampingPlaceDelete, name="manageCampingPlaceDelete"),
   path("Admin/ManageCampingPlace/Create", manageCampingPlaceCreate, name="manageCampingPlaceCreate"),
   path('Admin/ManageCampingPlaces/Edit/<int:id>', manageCampingPlaceEdit, name="manageCampingPlaceEdit"),
   path('Admin/ManageCampingPlaces/Detail/<int:id>', manageCampingPlaceDetail, name="manageCampingPlaceDetail"),
   path('Admin/ManageOrders', manageOrders, name="manageOrders"),
   path('Admin/ManageUser', manageuser, name="manageuser"),
   path('Admin/ManageUser/ChangeRock/<str:user_id>/<int:value>', manageUserChangeRock, name="manageUserChangeRock"),
   path("Admin/ManageUser/Create", manageUserCreate, name="manageUserCreate"),
   path("Admin/ManageUser/Delete/<str:id>", manageUserDelete, name="manageUserDelete"),
   path("Admin/ManageUser/Edit/<str:id>", manageUserEdit, name="manageUserEdit"),
   path("Admin/ManageUser/Detail/<str:id>", manageUserDetail, name="manageUserDetail"),
   path("Admin/ManageUser/GetCoordinate/<str:street>", getCoordinate, name="getCoordinate"),
   path("Admin/ManageUser/ChangePassword/<str:id>", manageUserChangePassword, name="manageUserChangePassword"),
   path("Admin/ManageMerchant", manageMerchant, name="manageMerchant"),
   path('Admin/ManageMerchant/ChangeActiveStatus/<int:merchant_id>/<int:value>', manageMerchantChangeActiveStatus, name="manageMerchantChangeActiveStatus"),
   path("Admin/ManageMerchant/Delete/<int:id>", manageMerchantDelete, name="manageMerchantDelete"),
   path("Admin/ManageMerchant/Edit/<int:id>", manageMerchantEdit, name="manageMerchantEdit"),
   path("Admin/ManageMerchant/Create", manageMerchantCreate, name="manageMerchantCreate"),
   path("Admin/getMerchantList", getMerchantList, name="getMerchantList"),
   path("Admin/searchFromCoordinate", searchFromCoordinate, name="searchFromCoordinate"),
   path("Admin/ManageMerchant/Detail/<int:id>", manageMerchantDetail, name="manageMerchantDetail"),
   path("Admin/ManageSecurityCompany", manageSecurityCompany, name="manageSecurityCompany"),
   path("Admin/ManageSecurityCompany/Create", manageSecurityCompanyCreate, name="manageSecurityCompanyCreate"),
   path("Admin/ManageSecurityCompany/Delete/<int:id>", manageSecurityCompanyDelete, name="manageSecurityCompanyDelete"),
   path("Admin/ManageSecurityCompany/Edit/<int:id>", manageSecurityCompanyEdit, name="manageSecurityCompanyEdit"),
   path("Admin/ManageSecurityCompany/Detail/<int:id>", manageSecurityCompanyDetail, name="manageSecurityCompanyDetail"),
   path("Admin/ManageSubscriptions", manageSubscriptions, name="manageSubscriptions"),
   path("Admin/ManageSubscription/Delete/<int:id>", manageSubscriptionDelete, name="manageSubscriptionDelete"),
   path('Admin/ManageSubscription/ChangeActiveStatus/<int:id>/<int:value>', manageSubscriptionChangeActiveStatus, name="manageSubscriptionChangeActiveStatus"),
   path("Admin/ManageSubscription/Create", manageSubscriptionCreate, name="manageSubscriptionCreate"),
   path("Admin/ManageSubscription/Edit/<int:id>", manageSubscriptionEdit, name="manageSubscriptionEdit"),
   path("Admin/ManageSubscription/Detail/<int:id>", manageSubscriptionDetail, name="manageSubscriptionDetail"),
   path("Admin/ManageSubscriptionInvoice", manageSubscriptionInvoice, name="manageSubscriptionInvoice"),
   path("Admin/ManageTracker", manageTracker, name="manageTracker"),
   path("Admin/ManageTracker/Create", manageTrackerCreate, name="manageTrackerCreate"),
   path("Admin/ManageTracker/Edit/<int:id>", manageTrackerEdit, name="manageTrackerEdit"),
   path("Admin/ManageTracker/Delete/<int:id>", manageTrackerDelete, name="manageTrackerDelete"),
   path("Admin/ManageTracker/Detail/<int:id>", manageTrackerDetail, name="manageTrackerDetail"),
   path('Admin/ManageTracker/ChangeActiveStatus/<int:id>/<int:value>', manageTrackerChangeActiveStatus, name="manageTrackerChangeActiveStatus"),
   path('Admin/ManageTracker/ImageUpload/<int:id>', manageTrackerImageUpload, name="manageTrackerImageUpload"),
   path('Admin/ManageTracker/ImageDelete/<int:id>', manageTrackerImageDelete, name="manageTrackerImageDelete"),
   path("Admin/ShopCategory", shopCategory, name="shopCategory"),
   path("Admin/ShopCategory/Submit", shopCategorySubmit, name="shopCategorySubmit"),
   path("Admin/ShopCategory/Delete/<int:id>", shopCategoryDelete, name="shopCategoryDelete"),
   path("Admin/ManageForms", manageForms, name="manageForms"),
   path("Admin/ManageCustomerServicedata", manageCustomerServicedata, name="manageCustomerServicedata"),
   path("Admin/ManageCustomerServicedata/CustomerGraphics", manageCustomerGraphics, name="manageCustomerGraphics"),
   path("Admin/ManagePromotionCredit", managePromotionCredit, name="managePromotionCredit"),
   path("Admin/ManagePromotionCredit/Edit/<int:id>", managePromotionCreditEdit, name="managePromotionCreditEdit"),
   path("Admin/ManagePromotionCreditSubscription/Delete/<int:id>", managePromotionCreditSubscriptionDelete, name="managePromotionCreditSubscriptionDelete"),
   path("Admin/ManagePromotionCredit/Delete/<int:id>", managePromotionCreditDelete, name="managePromotionCreditDelete"),
   path("Admin/ManagePromotionCredit/Create", managePromotionCreditCreate, name="managePromotionCreditCreate"),
   path("Admin/Reviewratting", reviewratting, name="reviewratting"),
   path("Admin/Reviewratting/Delete/<int:id>", reviewRattingDelete, name="reviewRattingDelete"),
   path("Admin/Reviewratting/Detail/<int:id>", reviewRattingDetail, name="reviewRattingDetail"),
   path("Admin/Reviewratting/ChangeLock/<int:id>/<int:value>", reviewRattingChangeLockStatus, name="reviewRattingChangeLockStatus"),
   path("Admin/TermsOfService", termsOfService, name="termsOfService"),
   path("Admin/AdminPrivacypolicy", adminPrivacypolicy, name="adminPrivacypolicy"),
   path("Admin/AdminImprint", adminImprint, name="adminImprint"),
   path("Admin/Adminchangepassword", adminChangePassword, name="adminChangePassword")
]