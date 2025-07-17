from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(content__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already in use.")
        return data
    

class ArticleFormOld(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.Textarea(attrs={
                'placeholder': 'Title...',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Content...',
                'class': 'form-control',
                'rows': 5
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['content'].required = True
