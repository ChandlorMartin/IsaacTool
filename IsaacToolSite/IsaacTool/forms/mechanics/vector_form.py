from django import forms
from decimal import Decimal, InvalidOperation
from IsaacTool.utilities import is_decimal_list, to_decimal_list, are_same_lengths, print_item


class VectorForm(forms.Form):
    i = forms.CharField(required=False)
    j = forms.CharField(required=False)
    k = forms.CharField(required=False)

    def clean_i(self):
        i = self.cleaned_data.get('i')
        i_list = i.split(',')

        is_decimal_list(i_list)
        return i

    def clean_j(self):
        j = self.cleaned_data.get('j')
        j_list = j.split(',')

        is_decimal_list(j_list)
        return j

    def clean_k(self):
        k = self.cleaned_data.get('k')
        k_list = k.split(',')

        is_decimal_list(k_list)
        return k

    def clean(self):
        cleaned_data = super().clean()
        i = self.cleaned_data.get('i')
        j = self.cleaned_data.get('j')
        k = self.cleaned_data.get('k')

        if i and j and k:
            lengths = [len(to_decimal_list(i)), len(to_decimal_list(j)), len(to_decimal_list(k))]
            are_same_lengths(self, lengths)

        return cleaned_data
