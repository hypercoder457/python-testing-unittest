def get_formatted_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    full_name_title_case = full_name.title()
    return full_name_title_case