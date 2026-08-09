from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")

        return name

    def clean_message(self):
        message = self.cleaned_data['message']

        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters.")

        return message