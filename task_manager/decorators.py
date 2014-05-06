from django.contrib.auth.decorators import login_required


def login_required(fn):
    def wrapper(request, *args, **kwargs):
        user.au
        return fn(request, *args, **kwargs)

    return wrapper

