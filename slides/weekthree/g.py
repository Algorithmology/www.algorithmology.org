"""g.py: A module to benchmark Python function call overhead."""


def g(*args, **kwargs):
    pass


def loop_3_g(n):
    """Run loop with empty function taking args, n times."""
    for i in range(n):
        g()


def loop_5_g_arg(n):
    """Run loop with empty function passing an arg, n times."""
    for i in range(n):
        g(n)


def loop_6_g_kwarg(n):
    """Run loop with empty function passing a kwarg, n times."""
    for i in range(n):
        g(n=n)
