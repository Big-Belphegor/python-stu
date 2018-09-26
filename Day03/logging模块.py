__author__ = "Alien"
import logging,time
# 日志级别
# 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）
# 默认只输出大于warning级别日志内容
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# 通过basicConfig定义日志输出级别、格式等，具体参数访问有道云笔记--Python--02、模块及内置方法
# logging.basicConfig(level=logging.INFO,                             # 大于INFO级别的都输出
#                     format="%(asctime)s %(name)s %(levelname)s %(message)s",
#                     datefmt = '%Y-%m-%d  %H:%M:%S %a'               # 注意月份和天数不要搞乱了，这里的格式化符与time模块相同
#                     )
#
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')
# 注意：basicConfig是一次性的，不能重复调用

# 将日志写入到文件
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d  %H:%M:%S %a ',
                    filename='t1.log',
                    filemode='a',
                    )
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
