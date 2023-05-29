#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as u:
        return (False)
    else:
        return (True)
