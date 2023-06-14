from django.forms import ModelForm
from .models import Room


#built in form that uses meta data of Room class to create new room.
#We render a blank form with a url when user clicks create form, the form gets submitted to the same url
class RoomForm(ModelForm):
    class Meta:
        model= Room
        fields= '__all__'