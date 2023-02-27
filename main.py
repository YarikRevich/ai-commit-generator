import fire

from internal.middlewares import run_middlewares
from internal.middlewares import (
    create_logger_middleware, 
    create_version_middleware, 
    create_license_middleware,
)

from internal.cli import CLI

def main():
    run_middlewares([
        create_version_middleware,
        create_license_middleware,
        create_logger_middleware,
    ])

    fire.Fire(CLI)   

if __name__ == "__main__":
    main()