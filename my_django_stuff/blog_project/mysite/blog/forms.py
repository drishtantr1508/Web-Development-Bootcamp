from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model=Post
        fields=('author','title','text')
        widgets={
            'title':forms.TextInput(attrs={
                                    'class':'form-control textinputclass',
                                    'placeholder':'Title Here'

            }),
            'text':forms.Textarea(attrs={
                                    'class':'editable medium-editor-textarea postcontent',
                                    'placeholder':'Write Here'

            })
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        fields=('author','text')
        widgets={
            'author':forms.TextInput(attrs={
                                    'class':'form-control textinputclass',
                                    'placeholder':'Name Here'

            }),
            'text':forms.Textarea(attrs={
                                    'class':'editable medium-editor-textarea postcontent form-control',
                                    'placeholder':'Comment Here'

            })
        }
