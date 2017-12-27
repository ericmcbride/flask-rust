from . import _native

def test():
    return _native.lib.a_function_from_rust()
