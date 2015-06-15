from django import forms

class SearchForm(forms.Form):
    query = forms.CharField()

    def clean_query(self):
        query = self.cleaned_data['query']
        if len(query) < 3:
            raise forms.ValidationError('Query too short, min 3 characters')
        return query
