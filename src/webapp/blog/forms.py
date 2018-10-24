from django import forms

from .validators import validate_author_email

from .models import PostModel

SOME_CHOICES = [
('1','One'),
('2','Two'),
('3','Three')
]

PUBLISH_CHOICES = [
('draft','Draft'),
('publish','Publish'),
('private','Private')
]

YEARS = [ x for x in range(1980,250)]


COUNT_CHOICES = [ tuple([x,x]) for x in range(1,10)]


class PostModelForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = [
            'title','content','active',
            'publish','author_email'
            ]
        # labels = {
        #     "title": "title",
        #     "content": "Content"
        # }
        # help_text = {
        #     "title": "this is title",
        #     "slug": "This is content"
        # }
        #
        # widget = {
        # 'title' : TextInput(attrs={'placeholder':'title'}),
        # #'content'  : forms.TextInput(attrs={'placeholder':'title'})
        # }



class PostForm(forms.Form):

    title = forms.CharField()
    content = forms.CharField()
    active  = forms.BooleanField()
