from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='Title', 
					widget=forms.TextInput(attrs={"placeholder": "Enter title here"}))
	email 		= forms.EmailField()
	description	= forms.CharField(
							required=False, 
							widget=forms.Textarea(
								attrs={
									"placeholder": "Your description",
									"class": "new-class-name two",
									"id": "my-id-text",
									"rows": 10,
									"columns": 20
								}
							)
						) 
	price 		= forms.DecimalField(initial=9.99)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]


	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "cfe" in title:
			raise forms.ValidationError("This is not a valid title")
		return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("com"):
			raise forms.ValidationError("This is not a valid email")
		return email

class RawProductForm(forms.Form):
	title 		= forms.CharField(
								label='', 
								widget=forms.TextInput(
									attrs={"placeholder": "Enter title here..."
									}
								)
							)
	description	= forms.CharField(
								required=False, 
								widget=forms.Textarea(
									attrs={
										"placeholder": "Your description",
										"class": "new-class-name two",
										"id": "my-id-text",
										"rows": 10,
										"columns": 20
									}
								)
							)
	price 		= forms.DecimalField()