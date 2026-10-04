from django import forms

from .models import Topic, Enntry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EnntryForm(forms.ModelForm):
    class Meta:
        model = Enntry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':60})}

