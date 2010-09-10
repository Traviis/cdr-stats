from django import *
from django import forms
from cdr.models import *
from cdr.functions_def import *
from django.forms import *
from django.contrib import *
from django.contrib.admin.widgets import *
from django.utils.translation import ugettext_lazy as _
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, Column, HTML



class CdrSearchForm(forms.Form):

    destination = forms.CharField(label=_('Destination'), required=False, widget=forms.TextInput(attrs={'size': 15}))
    destination_type = forms.TypedChoiceField(coerce=bool, required=False,
                    choices=((1, _('Equals')), (2, _('Begins with')), (3, _('Contains')), (4, _('Ends with'))),
                    widget=forms.RadioSelect)
    source = forms.CharField(label=_('Source'), required=False, widget=forms.TextInput(attrs={'size': 15}))
    source_type = forms.TypedChoiceField(coerce=bool, required=False,
                    choices=((1, _('Equals')), (2, _('Begins with')), (3, _('Contains')), (4, _('Ends with'))),
                    widget=forms.RadioSelect)
    channel = forms.CharField(label='Channel', required=False, widget=forms.TextInput(attrs={'size': 15}))


class MonthLoadSearchForm(CdrSearchForm):

    from_month_year= forms.CharField(label=_('Select date'), required=True, max_length=10, help_text="Please use the following format: <em>YYYY-MM</em>.")
    comp_months = forms.ChoiceField(label=_('Months to Compare'), required=False, choices=comp_month_range())
    
    # Attach a formHelper to your forms class.
    helper = FormHelper()
    
    submit = Submit('search', _('Search'))
    helper.add_input(submit)
    helper.use_csrf_protection = True
    
    def __init__(self, *args, **kwargs):
        super(MonthLoadSearchForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['from_month_year', 'comp_months', 'destination', 'destination_type', 'source', 'source_type', 'channel']


class DailyLoadSearchForm(CdrSearchForm):

    from_date = forms.CharField(label=_('Select date'), required=True, max_length=10, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    
    # Attach a formHelper to your forms class.
    helper = FormHelper()

    submit = Submit('search', _('Search'))
    helper.add_input(submit)
    helper.use_csrf_protection = True

    def __init__(self, *args, **kwargs):
        super(DailyLoadSearchForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['from_date', 'destination', 'destination_type', 'source', 'source_type', 'channel']
    

class CompareCallSearchForm(CdrSearchForm):

    from_date = forms.CharField(label=_('Select date'), required=True, max_length=10, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    comp_days = forms.ChoiceField(label=_('Days to Compare'), required=False, choices=comp_day_range())
    graph_view=forms.ChoiceField(label=_('Graph'), required=False,
            choices=((1, _('Calls per Hour')), (2,_('Minutes per Hour'))))

    # Attach a formHelper to your forms class.
    helper = FormHelper()
    
    submit = Submit('search', _('Search'))
    helper.add_input(submit)
    helper.use_csrf_protection = True

    def __init__(self, *args, **kwargs):
        super(CompareCallSearchForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['from_date','comp_days', 'destination', 'destination_type', 'source', 'source_type', 'channel','graph_view']


class CdrSearchForm(forms.Form):
    
    from_date = CharField(label=_('From'), required=True, max_length=10, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    to_date = CharField(label=_('To'), required=True, max_length=10, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    
    result = forms.TypedChoiceField(label=_('Result:'), required=False, coerce=bool,
                choices = (('1', _('Minutes')), ('2', _('Seconds'))),widget=forms.RadioSelect)

    # Attach a formHelper to your forms class.
    helper = FormHelper()
    helper.form_method = 'GET'
    submit = Submit('search', _('Search'))
    helper.add_input(submit)
    helper.use_csrf_protection = True

class ConcurrentCallForm(forms.Form):
    result = forms.TypedChoiceField( label=_('Result'), required=True, coerce=bool, empty_value=1,
                choices = (('1', _('Today')), ('2', _('Yesterday')), ('3', _('Current Week')), ('4', _('Previous Week')), ('5', _('Current Month')), ('6', _('Previous Month'))),widget=forms.RadioSelect)
    

    # Attach a formHelper to your forms class.
    helper = FormHelper()
    helper.form_method = 'POST'
    submit = Submit('search', _('Search'))
    helper.add_input(submit)
    helper.use_csrf_protection = True


class loginForm(forms.Form):

    user = forms.CharField(max_length=40, label=_('Login'), required=True, widget=forms.TextInput(attrs={'size':'10'}))
    password = forms.CharField(max_length=40, label=_('Password'), required=True, widget=forms.PasswordInput(attrs={'size':'10'}))
    
