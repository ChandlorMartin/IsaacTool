from django import forms
from decimal import Decimal
from .error_list import get_error_message


#-------------------------------------------------------
#                   UTILITY
#-------------------------------------------------------

def print_item(item_name, item):
    print(item_name + str(item))


#-------------------------------------------------------
#                   CONVERSIONS
#-------------------------------------------------------

# This converts a string list like 1,3,5,6, into a list of decimals.
def to_decimal_list(values_string):
    value_list = values_string.split(',')
    value_numbers = []

    for value in value_list:
        number = Decimal(value)
        value_numbers.append(number)

    return value_numbers


# This counts how many of the fields were filled and returns true of they all are filled.
def check_filled_field_count(self, data, field_count):
    full_fields = 0
    for key in data.keys():
        if data[key] is not None:
            full_fields += 1

    if full_fields >= field_count:
        self.add_error(None, get_error_message(1))

    return full_fields


#-------------------------------------------------------
#                   Form Validations
#-------------------------------------------------------

# This raises an error if the value isn't a valid decimal.
def is_decimal(value, form_field_name=""):
    try:
        value = Decimal(value)
    except Exception:
        raise forms.ValidationError(get_error_message(2, form_field_name))


# This iterates through each value and throws an error if a value wasn't a valid decimal.
def is_decimal_list(values):
    for value in values:
        if not value or value.isspace():
            raise forms.ValidationError(get_error_message(2))

        try:
            test_value = Decimal(value)
        except Exception:
            raise forms.ValidationError(get_error_message(3))

    return "Success"


# This checks that all lengths in the list are the same length and raises an error if they aren't.
def are_same_lengths(self, lengths_list):
    for length in lengths_list:
        for item in lengths_list:
            print("length: " + str(length))
            print('item: ' + str(item))
            if length != item:
                self.add_error(None, get_error_message(4))
                return False

    return True


# This counts how many of the fields were left empty and returns true of they all are empty.
def too_many_empty(self, data):
    empty_fields = 0

    for key in data:
        if data.get(key) is None:
            empty_fields += 1

    if empty_fields > 1:
        self.add_error(None, get_error_message(1))


# This decides if the equation is mathematically possible or not.
def is_possible(self, form_name, equation_type, data):
    match form_name:
        case "Average Speed Form":
            if equation_type == "Average Speed" and data["time_interval"] == str(0):
                self.add_error(None, get_error_message(101, "time interval", "average speed"))
            elif equation_type == "Time Interval" and data["average_speed"] == str(0):
                self.add_error(None, get_error_message(101, "average speed", "time interval"))
        case "Linear Thermal Expansion Form":
            print_item("data", data)
            if equation_type == "Length" and data["temperature_change"] == str(0):
                self.add_error(None, get_error_message(101, "temperature change", "length"))
            if equation_type == "Length" and data["linear_coefficient"] == str(0):
                self.add_error(None, get_error_message(101, "linear coefficient", "length"))
            if equation_type == "Linear Coefficient" and (data["length"] == str(0)):
                self.add_error(None, get_error_message(101,"length", "length change"))
            if equation_type == "Linear Coefficient" and (data["temperature_change"] == str(0)):
                self.add_error(None, get_error_message(101, "temperature change", "length change"))
            if equation_type == "Temperature Change" and (data["length"] == str(0)):
                self.add_error(None, get_error_message(101,"length", "temperature change"))
            if equation_type == "Temperature Change" and (data["linear_coefficient"] == str(0)):
                self.add_error(None, get_error_message(101, "linear coefficient", "temperature change"))
