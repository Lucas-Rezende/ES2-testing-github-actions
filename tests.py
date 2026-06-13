from validate_password import is_password_valid


def test_is_password_valid():
    assert is_password_valid("Senha123") == True


def test_is_password_valid_too_short():
    assert is_password_valid("Sen1") == False


def test_is_password_valid_without_uppercase():
    assert is_password_valid("senha123") == False


def test_is_password_valid_without_number():
    assert is_password_valid("Senhaabc") == False


def test_is_password_valid_empty():
    assert is_password_valid("") == False