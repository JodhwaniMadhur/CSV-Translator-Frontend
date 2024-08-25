from django import forms

from uploads.core.models import downloadCSV,downloadPrevCSV


class DocumentForm(forms.ModelForm):
    class Meta:
        model = downloadCSV
        fields = ('file_name', 'language')

    
class DocumentForm2(forms.ModelForm):
    class Meta:
        model = downloadPrevCSV
        fields = ('file_name', 'language')
