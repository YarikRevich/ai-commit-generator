import logging

def create_logger_middleware() -> None:
    """Middleware, which initializes basic logger"""

    logging.basicConfig(filename='myfirstlog.log', 
    level=logging.DEBUG, 
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')