from django import forms
from . import models


class HeaderTopForm(forms.ModelForm):
    class Meta:
        model = models.HeaderTop
        fields = ['text','icon','adress']
        
class HeaderCenterForm(forms.ModelForm):
    class Meta:
        model = models.HeaderCenter
        fields = ['name','adress']
        
class HeaderEndForm(forms.ModelForm):
    class Meta:
        model = models.HeaderEnd
        fields = ['text_top','text_big','text_end','but_name']
        
        
class HeaderSliderForm(forms.ModelForm):
    class Meta:
        model = models.HeaderSlider
        fields = ['img','name','text']

class MainOneTopForm(forms.ModelForm):
    class Meta:
        model = models.MainOneTop
        fields = ['name']

class MainOneLeftForm(forms.ModelForm):
    class Meta:
        model = models.MainOneLeft
        fields = ['name','text','but_name','but_adress']

class MainOneRightForm(forms.ModelForm):
    class Meta:
        model = models.MainOneRight
        fields = ['pay','img','number','name','text']

class MainTwoLeftForm(forms.ModelForm):
    class Meta:
        model = models.MainTwoLeft
        fields = ['name','text','but_name','but_adress']

class MainTwoRightForm(forms.ModelForm):
    class Meta:
        model = models.MainTwoRight
        fields = ['name','text']
        


class MainTheeTopForm(forms.ModelForm):
    class Meta:
        model = models.MainTheeTop
        fields = ['name']
        
class MainTheeContentForm(forms.ModelForm):
    class Meta:
        model = models.MainTheeContent
        fields = ['img','name','pay']




class MainFourTopForm(forms.ModelForm):
    class Meta:
        model = models.MainFourTop
        fields = ['name']

class MainFourLeftForm(forms.ModelForm):
    class Meta:
        model = models.MainFourLeft
        fields = ['name','number','nametwo','numbertwo']

class MainFourRightForm(forms.ModelForm):
    class Meta:
        model = models.MainFourRight
        fields = ['img']


class FooterForm(forms.ModelForm):
    class Meta:
        model = models.Footer
        fields = ['name','adress']

