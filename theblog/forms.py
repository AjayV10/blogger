from django import forms
from .models import Post, Category, Comment

#choice = [('coding','coding'),('sports','sports'),('entertainments','entertainments')]
choices = Category.objects.all().values_list('name','name')

choice_list=[]
for item in choices:
	choice_list.append(item)
choice_list.sort()
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','author','Category','body','header_image')

		widgets = {
		     'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
		     'title_tag' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title tag'}),
		     'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'daniel','type':'hidden'}),
		     #'author' : forms.Select(attrs={'class':'form-control','placeholder':'Select author'}),
		     'Category' : forms.Select(choices=choice_list, attrs={'class':'form-control','placeholder':'Select category'}),
		     'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Should be more minimum 150 words'}),    
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','title_tag','Category','body')

		widgets = {
		     'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
		     'title_tag' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title tag'}),
		     #'author' : forms.Select(attrs={'class':'form-control','placeholder':'Select author'}),
		     'Category' : forms.Select(choices=choice_list, attrs={'class':'form-control','placeholder':'Select category'}),
		     'body' : forms.Textarea(attrs={'class':'form-control','placeholder':'Should be more minimum 150 words'}),    
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')

		widgets = {
		     'name' : forms.TextInput(attrs={'class':'form-control'}),
		     'body' : forms.Textarea(attrs={'class':'form-control'}),    
		}