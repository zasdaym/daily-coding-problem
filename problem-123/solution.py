def is_number(s: str) -> bool:
    return is_scientific_number(s) or is_positive_number(s) or is_negative_number(s)

def is_scientific_number(s: str) -> bool:
    if s.count('e') != 1:
        return False
    
    before_e, after_e = s.split('e')
    return (is_positive_number(before_e) or is_negative_number(before_e)) and (is_positive_number(after_e) or is_negative_number(after_e))

def is_positive_number(s: str) -> bool:
    return is_positive_integer(s) or is_positive_decimal(s)

def is_positive_integer(s: str) -> bool:
    return s.isdigit()

def is_positive_decimal(s: str) -> bool:
    if s.count('.') != 1:
        return False
    
    integer_part, decimal_part = s.split('.')
    return is_positive_integer(integer_part) and is_positive_integer(decimal_part)

def is_negative_number(s: str) -> bool:
    if not s.startswith('-'):
        return False
    
    return is_positive_number(s[1:])

assert is_number('10')
assert is_number('-10')
assert is_number('10.1')
assert is_number('-10.1')
assert is_number('1e5')

assert not is_number('a')
assert not is_number('x 1')