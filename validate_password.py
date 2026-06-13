def is_password_valid(password):
    if len(password) < 8: return False

    have_caps = any(letter.isupper() for letter in password)
    have_number = any(letter.isdigit() for letter in password)

    return have_caps and have_number