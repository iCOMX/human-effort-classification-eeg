
from contextlib import contextmanager

class skip(object):
    """A decorator to skip function execution.

    Parameters
    ----------
    f : function
        Any function whose execution need to be skipped.

    Attributes
    ----------
    f

    """

    def __init__(self, f):
        self.f = f

    def __call__(self, *args):
        print('skipping : ' + self.f.__name__)


class SkipWith(Exception): pass


@contextmanager
def skip_run_code(flag, f):
    """To skip a block of code.

    Parameters
    ----------
    flag : str
        skip or run.

    Returns
    -------
    None

    """

    @contextmanager
    def check_active():
        deactivated = ['skip']
        if flag in deactivated:
            raise SkipWith()
        else:
            yield
    try:
        yield check_active
        print('Running the code: ' + f)
    except SkipWith:
        print('Skipping the code: ' + f)
