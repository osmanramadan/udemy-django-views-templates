from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name','slug', 'content']



#class BlogPostForm(forms.Form):
   # title = forms.CharField(max_length=50)
    #content = forms.CharField(widget=forms.Textarea)
    #slug = forms.SlugField()

