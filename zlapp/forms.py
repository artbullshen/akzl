from django import forms

from .models import Topic, Entry, News

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['text','source','author','cont']
        labels = {'text':'标题','source':'来源','author':'作者', 'cont':''}
        widgets = {'cont':forms.Textarea(attrs={'cols':80})}


