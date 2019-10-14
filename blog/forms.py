from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


        
class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30 , required=False)    
    blood_group = forms.CharField(max_length=1,required=True)
    email = forms.EmailField(max_length=254)
    address =forms.CharField(max_length=100)
    city =forms.CharField(max_length =100)
    about_me =forms.CharField(max_length=1000)
    

    class meta:
        model =User
        fields =('name','email','blood_group','address','city','password2','about_me')
