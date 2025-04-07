from utils import log_decorator

# pydantic
# pandera


@log_decorator
def sum(x, y):
    return x + y


sum(2, 3)
sum(20, 3)
