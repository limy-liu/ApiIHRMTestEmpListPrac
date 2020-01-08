import logging.handlers
import os
HOST = 'http://182.92.81.159'
HEADERS = {"Content-Type":"application/json"}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def init_log():
    """封装日志函数"""
    # 实例化日志器对象
    logger = logging.getLogger()
    # 设置日志输出级别
    logger.setLevel(level=logging.INFO)
    # 实例化处理器对象
    # 控制台
    sh = logging.StreamHandler()
    # 文件数量
    filename = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(filename,
                                                   when='M',
                                                   interval=1,
                                                   backupCount=4)
    # 实例化格式化器对象
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 将格式化器设置给处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)



if __name__ == '__main__':
    init_log()