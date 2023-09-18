from django.shortcuts import redirect, render


def login_one_required(ref):
    def inner(*args, **kwargs):
        valid = args[0].session.get('id', None)
        if valid:
            return ref(*args, **kwargs)
        return render(args[0], 'login.html', {'mssg': 'First Need To Login For Check Out'})
    return inner