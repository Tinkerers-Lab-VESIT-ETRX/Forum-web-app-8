from django.forms import ModelForm
from .models import *
# from django import form 

class Createinforum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"

class Createindiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"