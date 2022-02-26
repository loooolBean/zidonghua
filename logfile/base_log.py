# 日志： 记录系统的一些信息，状态 日志文件中
# 作用： 了解系统的运行状态，通过日志去分析和定位错误问题

"""

debug：调试的级别 1级别
info：正常的级别 2级别
warning：警告级别 程序有问题，但是不影响程序正常运行 不提bug 3级别
error：错误级别 4级别
critical：严重级别 5级别

反应出日志错误信息的严重程度
"""

# 不需要安装直接引入
import logfile
# 设置日志格式 如，2020-11-27 17：19:29,165 excel_excutor.py INFO excute web 现在执行关键字：open_browser,操作描述：启动Chrome浏览器
# 对应的格式字符串可以百度搜索其他更多的
fm = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
# 设置日志级别
logfile.basicConfig(level=logfile.DEBUG, format=fm, filename='./log1.log')

# 建议用的时候 try： info except error
logfile.debug('调试级别')
logfile.info('正常级别')
logfile.warning('警告级别')
logfile.error('错误级别')
logfile.critical('严重级别')