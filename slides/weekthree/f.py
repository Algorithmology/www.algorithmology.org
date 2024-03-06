"""f.py: A module to benchmark Python function call overhead."""


def f():
    pass


def loop_0_empty(n):
    """Run empty loop n times."""
    for i in range(n):
        pass


def loop_1_f(n):
    """Run loop with empty function n times."""
    for i in range(n):
        f()


def loop_2_f_twice(n):
    """Run loop calling empty function twice per loop, n times."""
    for i in range(n):
        f()
        f()
