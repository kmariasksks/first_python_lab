"""
This module includes decorators for logging.
"""
import logging  # pylint: disable=import-self


def logged(exception, mode):
    """
    A decorator that logs exceptions raised by the decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as error:
                if mode == "console":
                    logging.basicConfig(level=logging.INFO)  # pylint: disable=no-member
                    logging.error(str(error))
                elif mode == "file":
                    logging.basicConfig(filename='error.log', filemode='w', level=logging.INFO)
                    logging.error(str(error))
            return None
        return wrapper
    return decorator
