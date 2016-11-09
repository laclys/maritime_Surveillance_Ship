from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
   # mail = forms.EmailField(required=False,label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Please your opinion and comment!'}))
    #def clean_message(self):
       # message = self.cleaned_data['message']
       # num_words = len(message.split())
        #if num_words < 4:
        #    raise forms.ValidationError("Not enough words!")
       # return message
