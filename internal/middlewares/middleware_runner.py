import typing

def run_middlewares(middlewares: list[typing.Callable]) -> None:
    """Runs given middlewares"""

    for middleware in middlewares:
        middleware()