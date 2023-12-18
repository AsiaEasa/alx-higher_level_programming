#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        val = fct(*args)
        return val
    except Exception as _e:
        print("Exception: {}".format(_e), file=sys.stderr)
        return None
