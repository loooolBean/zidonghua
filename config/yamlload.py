# 这个文件用来读取yaml数据
import yaml
# 读取yaml的方法
def loadyaml(filename):
    files = open(filename, 'r',encoding='utf-8')
    # 读取
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

