from django import forms

from .models import Contact_us
#
#
# class ContactForm(forms.ModelForm):
#
#     class Meta:
#         model = Contact_us
#         fields = [
#             'firstname',
#             'lastname',
#             'email',
#             'telephone',
#             'message',
#         ]
# class ContactweForm(forms.Form):
#     firstname = forms.CharField(label='', widget=forms.TextInput(attrs={ "placeholder": "First name"}))
#     lastname = forms.CharField(label='', widget=forms.TextInput(attrs={ "placeholder": "Last name"}))
#     email = forms.CharField(label='', widget=forms.TextInput(attrs={ "placeholder": "Email"}))
#     telephone = forms.CharField(label='', widget=forms.TextInput(attrs={ "placeholder": "Telephone"}))
#     messsage = forms.CharField(
#           required=False,
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder": "Your message",
#                 "class": "new-class-name two",
#                 "id":"my_id_for_textarea",
#                 "rows": 5,
#                 "cols":120,
#             }
#         )
#     )

class ContactForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
       attrs= {
           'rows':5, 'placeholder': 'write your message'
       }
    ), max_length=5000,
       help_text= 'the max length of text is 5000')

    class Meta:
        model = Contact_us
        fields = ['firstname', 'lastname','email', 'telephone','message']

