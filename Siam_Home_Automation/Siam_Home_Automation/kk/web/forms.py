from django import forms
from kk.models import AuthUser, Rooms

class RoomForm(forms.ModelForm):

    class Meta:
        model = Rooms
        fields = ('id', 'displayname')