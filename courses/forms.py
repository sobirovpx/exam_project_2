from django import forms
from courses.models import Course, Category, User
from teachers.models import Teacher

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password')
        if len(password1) < 2:
            raise forms.ValidationError('Password must be at least 3 characters long.')
        return password1

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user