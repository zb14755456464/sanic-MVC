#!/usr/bin/env python
import os
import logging

def load_config():
    """
    Load a config class
    """

    mode = os.environ.get('MODE', 'DEV')
    try:
        if mode == 'PRO':
            from .pro_config import ProConfig
            return ProConfig
        elif mode == 'DEV':
            from .dev_config import DevConfig
            return DevConfig
        else:
            from .dev_config import DevConfig
            return DevConfig
    except ImportError:
        from .config import Config
        return Config





CONFIG = load_config()

# 配置日志
logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s:%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.DEBUG,
    filename=os.path.join(CONFIG.BASE_DIR, 'logs/log')
)


# 直接就可以调用日志
LOGGER = logging.getLogger()
