from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, UserManager

  class UserCreationForm(forms.ModelForm):
      password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
      password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta: #(UserCreationForm.Meta):
        model = User
        fields = ('email')
            #UserCreationForm.Meta.fields
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

  class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email' , 'password', 'is_active', 'is_admin')
        #UserChangeForm.Meta.fields
        def clean_password(self):
            return self.initial["password"]