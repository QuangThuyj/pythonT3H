from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(label='Ảnh sản phẩm', required=False)

    class Meta:
        model = Product
        fields = ('category', 'code', 'name', 'description', 'unitPrice', 'freeShip')

        error_messages = {
            "code": {
                "unique": "Mã sản phẩm đã tồn tại"
            }
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        id = self.cleaned_data.get('id')

        if id == None and image == None:
            raise forms.ValidationError('Cần chọn ảnh sản phẩm')

        return image

    def save(self):
        product = super().save()
        image = self.cleaned_data['image']

        if image and image.name:
            product.saveImage(image)


class PaymentForm(forms.Form):
    fullname = forms.CharField(label='Họ và tên')
    mobile = forms.CharField(label='Số điện thoại')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Địa chỉ')
