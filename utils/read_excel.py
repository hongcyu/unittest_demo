# -*-coding: utf8 -*-

'''
read_excel.py
读取excel表单内的数据，通过配置文件实现测试用例的配置,只能是xslx
新建excel文件时不可以在项目内部直接建,否则会报错
'''

import project_path
from read_config import Read_config
from openpyxl import load_workbook

class Read_the_excel(object):

    @staticmethod
    def get_data(data_path,config_path):
        wb = load_workbook(data_path)   #创建workbook对象
        modes = eval(Read_config.get_config(config_path,'MODE','mode'))
        
        test_data = []
        for mode in modes:
            sheet = wb[mode]
            print(sheet)

data_path = project_path.test_case_path
config_path = project_path.config_path

excel = Read_the_excel.get_data(data_path,config_path)


