#!/usr/bin/env python
# coding=utf-8
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField(max_value=20)
    b = forms.IntegerField(max_value=20)