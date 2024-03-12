from django import forms
from django.core.exceptions import ValidationError
from decimal import Decimal
from IsaacTool.utilities import is_decimal, too_many_empty, check_filled_field_count, is_possible


class AverageSpeedForm(forms.Form):
    # CharField is being used instead of DecimalField so that custom error messages are not overridden
    distance = forms.CharField(required=False)
    time_interval = forms.CharField(required=False)
    average_speed = forms.CharField(required=False)

    # This raises an error if the distance cannot be converted to the Decimal type
    def clean_distance(self):
        distance = self.cleaned_data.get('distance')
        if distance == "":
            distance = None

        if distance is not None:
            is_decimal(distance, "distance")

        return distance

    # This raises an error if the time interval cannot be converted to the Decimal type
    def clean_time_interval(self):
        time_interval = self.cleaned_data.get('time_interval')
        if time_interval == "":
            time_interval = None

        if time_interval is not None:
            is_decimal(time_interval, "time interval")

        return time_interval

    # This raises an error if the average speed cannot be converted to the Decimal type
    def clean_average_speed(self):
        average_speed = self.cleaned_data.get('average_speed')
        if average_speed == "":
            average_speed = None

        if average_speed is not None:
            is_decimal(average_speed, "average speed")

        return average_speed

    def clean(self):
        cleaned_data = super().clean()
        key_count = len(cleaned_data.keys())

        check_filled_field_count(self, self.cleaned_data, 3)

        if key_count is 3:
            too_many_empty(self, self.cleaned_data)
            equation_type = self.choose_equation(self.cleaned_data, key_count)
            is_possible(self, "Average Speed Form", equation_type, self.cleaned_data)

        return cleaned_data

    # This returns the value being solved for as a string
    def choose_equation(self, data, key_count):
        keys = data.keys()
        if key_count == 3:
            if data["average_speed"] is None:
                return "Average Speed"
            if data["time_interval"] is None:
                return "Time Interval"


