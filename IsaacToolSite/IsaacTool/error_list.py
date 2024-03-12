# List of error messages to be used
# 1 - 100:   These are designated for non formula specific field errors such as too many empty fields.
# 101 - 200: These are designated for mathematical issues such as trying to divide by 0.
def get_error_message(error_number, form_field_name_one="", form_field_name_two=""):
    match error_number:
        case 1:
            return "Error: There must be one and only one field empty."
        case 2:
            return 'Error: Entered ' + form_field_name_one + ' value must be a valid number.'
        case 2:
            return 'Error: The list may not contain an empty value.'
        case 3:
            return 'Error: The list must contain valid numbers.'
        case 4:
            return "Error: All fields must have the same number of elements."
        case 101:
            return "Error: The " + form_field_name_one + " cannot be 0 when calculating the " + form_field_name_one +"."
        case _:
            return "DEFAULT ERROR"