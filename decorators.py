from log import get_logger


def none_if_exception(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except:
            return None

    return wrapper


def exception_logger(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as ex:
            get_logger(function.__module__) \
                .error(f'There is a error in function {function.__name__}'
                       f' and the error is {str(ex)}')
            raise
    return wrapper
