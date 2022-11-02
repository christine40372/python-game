# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:40:26 2021

@author: christine
"""




import os


'''圖片路徑'''
IMAGEPATHS = {
    'carddirs': [
        os.path.join(os.getcwd(), 'resources/images/series1'),
        os.path.join(os.getcwd(), 'resources/images/series2'),
    ],
}
'''音樂路徑'''
AUDIOPATHS = {
    'score': os.path.join(os.getcwd(), 'resources/audios/score.wav'),
}
