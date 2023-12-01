import logging


def log_utils() -> logging.Logger:
    """
    Вывод логов в файл
    :return: logging.Logger
    """
    file_formatter_1 = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler_1 = logging.FileHandler("utils_log.log", "w")
    file_handler_1.setFormatter(file_formatter_1)
    logger_1 = logging.getLogger(__name__)
    logger_1.addHandler(file_handler_1)
    logger_1.setLevel(logging.DEBUG)
    # print(type(logger_1))
    return logger_1





