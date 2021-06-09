from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from django import db
db.connections.close_all()
from Student.models import User,ServiceBox,Rolrq,Orgdetails,MedicineInfo,Organization,Donate



class ChpwdForm(PasswordChangeForm):
		old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"old password"}))
		new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"new password"}))
		new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"confirm password"}))
		class Meta:
			model=User
			fields=['oldpassword','newpassword','confirmpassword']
			
class UsrReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Confirm Password"}))	
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Email Id",
			}),
		}

class PrfUpd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email","dob","gender","ph_no","pan_no","address","city","postal_code","state","country","img"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readOnly":True,
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			}),
		"dob":forms.DateInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			"placeholder":"select Your Date of Birth",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"ph_no":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Phone number",
			}),
		"pan_no":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Pan Number",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Address",
			"rows":5,
			}),
		"city":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update City",
			}),
		"state":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update State",
			}),
		"postal_code":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Postal Code",
			}),
		"country":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Update Country",
			}),
		}

class RolerqForm(forms.ModelForm):
	class Meta:
		model = Rolrq
		fields = ["uname","roltype","prf"]
		widgets = {
		"uname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readOnly":True,
			}),
		"roltype":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"prf":forms.FileInput(attrs={
			"class":"form-control my-2",
			}),
		}

class GvForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readOnly":True,
			}),
		"role":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		}
class OrgForm(forms.ModelForm):
	class Meta:
		model = Orgdetails
		fields = ["org_name","found_name","est_date"]
		widgets = {
		"org_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"found_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			}),
		"est_date":forms.DateInput(attrs={
			"class":"form-control my-2",
			"type":"date",
			}),
		}



class ServiceForm(forms.ModelForm):
	class Meta:
		model=ServiceBox
		fields=["name","email","change_role","impf"]
		widgets={
		"name":forms.TextInput(attrs={"class":"form-control","placeholder":"UserName",}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"email"}),
		"change_role":forms.TextInput(attrs={"class":"form-control","placeholder":"Request your role to change"})
		}

class Medform(forms.ModelForm):
	class Meta:
		model=MedicineInfo
		fields=['pharmacy_name','medicine_name','quantity','category','production_date','entry_date','expiry_date']
		widgets={
		"pharmacy_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pharmacy name"}),
		"medicine_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Medicine name"}),
		"quantity":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Quantity"}),
		"category":forms.Select(attrs={"class":"form-control","placeholder":"Enter category"}),
		"production_date":forms.DateInput(attrs={"class":"form-control","placeholder":"YYYY-MM-DD"}),
		"entry_date":forms.DateInput(attrs={"class":"form-control","placeholder":"YYYY-MM-DD"}),
		"expiry_date":forms.DateInput(attrs={"class":"form-control","placeholder":"YYYY-MM-DD"}),
		}

class MedRequired(forms.ModelForm):
	class Meta:
		model=MedicineInfo
		fields=['pharmacy_name','medicine_name']
		widgets={
		"pharmacy_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter pharmacy name"}),
		"medicine_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Medicine name"}),
		}

# class ContForm(forms.ModelForm):
# 	class Meta:
# 		model=Contains
# 		fields=['quantity']
# 		widgets={
# 		"quantity":forms.TextInput(attrs={"class":"form-control","placeholder":"Quantity"}),
# 		}
class RequestForm(forms.ModelForm):
	class Meta:
		model=Organization
		fields=['org_name','required_tablets']
		widgets={
		"org_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Org name"}),
		"required_tablets":forms.TextInput(attrs={"class":"form-control","placeholder":"Tablets required"}),
		}
# class RequestForm(forms.ModelForm):
# 	class Meta:
# 		model=OrgRequires
# 		fields=['required_tablets']
# 		widgets={
# 		"required_tablets":forms.TextInput(attrs={"class":"form-control","placeholder":"Tablets required"}),
# 		}