"""Validators: functions that answer yes/no. Every validator RETURNS True or False (never prints)."""


def is_in_range(value, low, high):
    """Return True if low <= value <= high (both ends included)."""
    if low <= value <= high:
        return True
    return False 


def is_valid_test_id(test_id, prefix="TC", digits=3):
    """Return True for IDs like 'TC-007': the prefix, a dash, then exactly `digits` digits."""
    if test_id.startswith(prefix):
        if '-' in test_id:
            _, check = test_id.split('-')
        else:
            return False
        if check.isdigit() and len(check) == digits:
            return True
    return False


def is_valid_email(email):
    """Return True for a simple email shape (a deliberately simple teaching version).

    Rules: no spaces, exactly one '@', something before the '@',
    and a domain that contains a '.' but does not start or end with one.
    """
    if ' ' in email:
        return False
    if email.count("@") != 1:
        return False
    name, domain = email.split("@")
    if name == '':
        return False
    if domain[0] == '.' or domain[-1] == '.':
        return False
    if domain.count('.') == 0:
        return False
    return True 

    


def is_strong_password(password, min_length=8):
    """Return True if the password has at least `min_length` characters and
    contains at least one uppercase letter, one lowercase letter and one digit."""
    up = False
    low = False
    dig = False
    
    if len(password) < min_length:
        return False
    for c in password:
        
        if c.isupper():
            up = True
        if c.islower():
            low = True
        if c.isdigit():
            dig = True
        if up and low and dig:
            return True
        
    return False


def is_valid_status_code(code):
    """Return True for HTTP status codes from 100 to 599. Reuses is_in_range."""
    return is_in_range(code, 100, 599)


def all_pass(value, *checks):
    """Return True only if EVERY check function returns a true value for `value`.

    With no checks at all, return True.
    Example: all_pass("TC-001", is_valid_test_id, lambda s: s.endswith("1"))
    """
    # TODO: loop over `checks`; return False as soon as one fails; return True after the loop
    for fun in checks:
        out = fun(value)
        if out == False:
            return False
    return True
