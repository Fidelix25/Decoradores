# Criação de logs
from loguru import logger

# Cria um documento com os logs
logger.add("my_app.log", level="CRITICAL")


def sum(x, y):
    try:
        sum = x + y
        logger.info(
            f"You have inserted correct values, congratulation the result is {sum}"
        )
        return sum
    except:
        logger.critical("You have inserted incorrect values")

    # logger.info(x)
    # logger.info(y)
    # logger.info(x + y)
    # return x + y


sum(2, 5)
sum(10, 25)
sum(15, "12")
