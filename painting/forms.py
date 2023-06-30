from django import forms 
from .models import Painting, avatar
# from .models import ImageAdd
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class avatar_user(forms.ModelForm):
    class Meta:
        model = avatar
        fields = ['avt']


