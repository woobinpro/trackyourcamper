from django import forms
from .models import Vehicleset, Brandset, Campingplaces, Merchants, Securitycompanies, Packagelist, Trackerlisitem, TblHeadercontent
class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicleset
        fields = "__all__"
class BrandForm(forms.ModelForm):

    class Meta:
        model = Brandset
        fields = "__all__"
class CampingplaceForm(forms.ModelForm):

    class Meta:
        model = Campingplaces
        fields = "__all__"
class MerchantForm(forms.ModelForm):

    class Meta:
        model = Merchants
        fields = "__all__"
class SecurityCompanyForm(forms.ModelForm):

    class Meta:
        model = Securitycompanies
        fields = "__all__"
class PackagelistForm(forms.ModelForm):

    class Meta:
        model = Packagelist
        fields = "__all__"
class TrackerForm(forms.ModelForm):

    class Meta:
        model = Trackerlisitem
        fields = "__all__"
class HeaderContentForm(forms.ModelForm):

    class Meta:
        model = TblHeadercontent
        fields = "__all__"
