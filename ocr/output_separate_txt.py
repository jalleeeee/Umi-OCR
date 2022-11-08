# 输出到每个图片同名的单独txt文件
from utils.config import Config
from utils.logger import GetLog
from ocr.output import Output

import os

Log = GetLog()


class OutputSeparateTxt(Output):

    def __init__(self):
        self.panelOutput = Config.main.panelOutput  # 输出接口
        self.isDebug = Config.get('isDebug')  # 是否输出调试
        self.outputPath = Config.get('outputFilePath')  # 输出文件夹，用于计划任务的完成后打开文件夹

    def print(self, text, highlight=''):
        pass

    def debug(self, text):
        pass

    def text(self, text):
        pass

    def img(self, textBlockList, imgInfo, numData, textDebug):
        '''输出图片结果'''
        # 收集ocr文字
        ocrText = ''
        for tb in textBlockList:
            ocrText += tb['text'] + '\n'
        # 输出到图片同名txt文件
        path = os.path.splitext(imgInfo['path'])[0]+'.txt'
        try:
            with open(path, 'w', encoding='utf-8') as f:  # 写入本地文件
                f.write(ocrText)
        except FileNotFoundError:
            raise Exception(f'创建txt文件失败。请检查以下地址是否正确。\n{path}')
        except Exception as e:
            raise Exception(
                f'创建txt文件失败。文件地址：\n{path}\n\n错误信息：\n{e}')
