from select import select
from tkinter.ttk import Style
from django import forms



class CHOICES(forms.Form):
    opts= [
    ('Only left one', 'Only left one'),
    ('Only right one', 'Only right one'),
    ('Both of them', 'Both of them'),
    ('None of them', 'None of them'),

    ]

    opts = forms.CharField(widget=forms.RadioSelect(choices=opts))