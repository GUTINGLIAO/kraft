__date__ = '21/03/08'

import os
import shutil


def classfiy_pic(num: int):
    _create_dir(num)

    result_file = open(r"./results.txt")  # 打开文件
    line = result_file.readline()  # 读取每一行
    while line:
        print(line.split('\t'))
        num = line.split('\t', 1)[1][0]  # 找到txt文件中的分类
        file_name = line.split('\t', 1)[0]
        shutil.copyfile('./picture/' + file_name, './' + str(num) + '/' + file_name)
        line = result_file.readline()
    result_file.close()  # 关闭文件


def _create_dir(num: int):
    for i in range(num):
        if not os.path.exists(r'./%d' % i):
            os.makedirs(r'./%d' % i)
