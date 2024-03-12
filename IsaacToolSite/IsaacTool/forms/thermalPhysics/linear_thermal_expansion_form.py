from django import forms
from decimal import Decimal
from IsaacTool.utilities import is_decimal, too_many_empty, check_filled_field_count, print_item, is_possible


class LinearThermalExpansionForm(forms.Form):
    length = forms.CharField(required=False)
    length_change = forms.CharField(required=False)
    linear_coefficient = forms.CharField(required=False)
    temperature_change = forms.CharField(required=False)

    # This validates the length and converts to None if it is empty.
    def clean_length(self):
        length = self.cleaned_data.get('length')
        if length == "":
            length = None

        if length is not None:
            is_decimal(length, "length")

        return length

    # This validates the length change and converts to None if it is empty.
    def clean_length_change(self):
        length_change = self.cleaned_data.get('length_change')
        if length_change == "":
            length_change = None

        if length_change is not None:
            is_decimal(length_change, "length change")

        return length_change

    # This validates the linear coefficient.
    def clean_linear_coefficient(self):
        linear_coefficient = self.cleaned_data.get('linear_coefficient')
        if linear_coefficient == "":
            linear_coefficient = None

        if linear_coefficient is not None:
            is_decimal(linear_coefficient, "linear coefficient")

        return linear_coefficient

    # This validates the temperature change and converts to None if it is empty.
    def clean_temperature_change(self):
        temperature_change = self.cleaned_data.get('temperature_change')
        if temperature_change == "":
            temperature_change = None

        if temperature_change is not None:
            is_decimal(temperature_change, "temperature change")

        return temperature_change

    # This provides needed validation for the form such as:
    # 1. There is only one empty field
    # 2. The equation to be performed is possible with the given data from the fields
    def clean(self):
        cleaned_data = super().clean()
        key_count = len(cleaned_data.keys())

        filled_count = check_filled_field_count(self, self.cleaned_data, 4)
        too_many_empty(self, self.cleaned_data)
        print_item("filled count", filled_count)
        if filled_count == 3:
            too_many_empty(self, self.cleaned_data)
            equation_type = self.choose_equation(self.cleaned_data, key_count)
            print_item("cleaned data", cleaned_data)
            is_possible(self, "Linear Thermal Expansion Form", equation_type, self.cleaned_data)

        return cleaned_data


    # This returns the value being solved for as a string
    def choose_equation(self, data, key_count):
        keys = data.keys()
        if key_count == 4:
            if data["length_change"] is None:
                return "Length Change"
            if data["length"] is None:
                return "Length"
            if data["temperature_change"] is None:
                return "temperature_change"
            if data["linear_coefficient"] is None:
                return "linear coefficient"
