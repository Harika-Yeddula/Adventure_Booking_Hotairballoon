from django import forms
from app.models import bookings

class BookingForm(forms.ModelForm):
    booking_for_the_date = forms.DateTimeInput()
    class Meta:
        model = bookings
        fields = ('location','booking_for_the_date','no_of_persons','view','guest')
        labels ={'location':'Location','booking_for_the_date':'Booking for the Date','view':'View for the day'}
        exclude = ['guest']
        widgets = {
            'booking_for_the_date': forms.DateInput(
                                             attrs={'placeholder': 'Select a date',
                                                    'type': 'date','id':'datefield','class':'form-control'},format='%Y-%m-%d',),
            'no_of_persons': forms.NumberInput(attrs={'class':'form-control'}),
            'location': forms.Select(attrs={'class':'form-control'}),
            'view':forms.Select(attrs={'class':'form-control'})

        }
        label_attr = {
            'Location': {'id': 'location-field'},
        }

        def __init__(self, *args, **kwargs):
            instance = kwargs.get('instance')
            if instance:
                # Convert the date to string in the desired format
                booking_date = instance.booking_for_the_date.strftime('%Y-%m-%d')
                initial = {
                    'location': instance.location,
                    'booking_for_the_date': instance.booking_date,
                    'no_of_persons': instance.no_of_persons,
                    'view': instance.view,
                }
                kwargs.setdefault('initial', initial)
            super().__init__(*args, **kwargs)
