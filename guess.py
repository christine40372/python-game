# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 00:31:02 2021

@author: christine
"""
import os
import cfg
import pygame
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


'''記憶翻牌小遊戲'''
class FlipCardByMemory():
    def __init__(self):
        # 載入得分後響起的音樂
        pygame.init()
        self.score_sound = pygame.mixer.Sound(cfg.AUDIOPATHS['score'])
        self.score_sound.set_volume(1)
        # 卡片圖片路徑
        self.card_dir = random.choice(cfg.IMAGEPATHS['carddirs'])
        # 主介面標題
        self.root =Tk()
        self.root.wm_title('蠟筆小新卡牌記憶小遊戲')
        # 卡片字典
        self.game_matrix = {}
        # 背景圖像
        self.blank_image =  ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(),'blank.png')))
        # 卡片背面
        self.cards_back_image =  ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(),'back.png')))
        # 所有卡片的索引
        cards_list = list(range(8)) + list(range(8))
        random.shuffle(cards_list)
        # 在界面上顯示所有卡片的背面
        for r in range(4):
            for c in range(4):
                position = f'{r}_{c}'
                self.game_matrix[position] = Label(self.root, image=self.cards_back_image)
                self.game_matrix[position].back_image = self.cards_back_image
                self.game_matrix[position].file = str(cards_list[r * 4 + c])
                self.game_matrix[position].show = False
                #按一下滑鼠左鍵就自動連結到clickcallback函數
                self.game_matrix[position].bind('<Button-1>', self.clickcallback)
                self.game_matrix[position].grid(row=r, column=c)
        # 已經顯示正面的卡片
        self.shown_cards = []
        # 場上存在的卡片數量
        self.num_existing_cards = len(cards_list)
        # 顯示遊戲剩餘時間
        self.num_seconds = 30
        self.time = Label(self.root, text=f'Time Left: {self.num_seconds}')
        self.time.grid(row=6, column=3, columnspan=2)
        # 置中顯示
        self.root.withdraw()
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry(None)
        self.root.deiconify()
        # 計時
        self.tick()
        # 主頁面顯示
        self.root.mainloop()
    
    def clickcallback(self, event):
        card = event.widget #抓取鼠標點擊位置
        if card.show: return  
        # 之前没有卡片被翻開
        if len(self.shown_cards) == 0:
            self.shown_cards.append(card)
            image = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir, card.file+'.png')))
            card.configure(image=image)
            card.show_image = image
            card.show = True
        # 之前只有一張卡片被翻開
        elif len(self.shown_cards) == 1:
            # --之前翻開的卡片和現在的卡片一樣
            if self.shown_cards[0].file == card.file:
                def delaycallback():
                    self.shown_cards[0].configure(image=self.blank_image)
                    self.shown_cards[0].blank_image = self.blank_image
                    card.configure(image=self.blank_image)
                    card.blank_image = self.blank_image
                    self.shown_cards.pop(0)#刪除在shown_cards list中的順序1
                    self.score_sound.play()
                self.num_existing_cards -= 2
                image = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir, card.file+'.png')))
                card.configure(image=image)
                card.show_image = image
                card.show = True
                card.after(300, delaycallback)
            # --之前翻開的卡片和現在的卡片不一樣
            else:
                self.shown_cards.append(card)
                image = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir, card.file+'.png')))
                card.configure(image=image)
                card.show_image = image
                card.show = True
        # 之前有兩張卡片被翻開
        elif len(self.shown_cards) == 2:
            # --之前翻開的第一張卡片和現在的卡片一樣
            if self.shown_cards[0].file == card.file:
                def delaycallback():
                    self.shown_cards[0].configure(image=self.blank_image)
                    self.shown_cards[0].blank_image = self.blank_image
                    card.configure(image=self.blank_image)
                    card.blank_image = self.blank_image
                    self.shown_cards.pop(0)#刪除在shown_cards list中的順序1
                    self.score_sound.play()
                self.num_existing_cards -= 2
                image = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir, card.file+'.png')))
                card.configure(image=image)
                card.show_image = image
                card.show = True
                card.after(300, delaycallback)
            # --之前翻開的第二張卡片和現在的卡片一樣
            elif self.shown_cards[1].file == card.file:
                def delaycallback():
                    self.shown_cards[1].configure(image=self.blank_image)
                    self.shown_cards[1].blank_image = self.blank_image
                    card.configure(image=self.blank_image)
                    card.blank_image = self.blank_image
                    self.shown_cards.pop(1)#刪除在shown_cards list中的順序2
                    self.score_sound.play()
                self.num_existing_cards -= 2
                image = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir, card.file+'.png')))
                card.configure(image=image)
                card.show_image = image
                card.show = True
                card.after(300, delaycallback)
            # --之前翻開的卡片和現在的卡片都不一樣
            else:
                self.shown_cards.append(card)
                #把翻開的第一張卡片蓋起來
                self.shown_cards[0].configure(image=self.cards_back_image)
                self.shown_cards[0].show = False
                self.shown_cards.pop(0) #把第一張卡片從shown_cards list刪除
                image = ImageTk.PhotoImage(Image.open(os.path.join(self.card_dir, card.file+'.png')))
                self.shown_cards[-1].configure(image=image) # 讀取倒數第一個元素(剛點選的那張卡片)
                self.shown_cards[-1].show_image = image
                self.shown_cards[-1].show = True
        # 判斷遊戲是否勝利
        if self.num_existing_cards == 0:
            is_restart = messagebox.askyesno('遊戲結束', '恭喜你！你贏了！要再玩一次嗎？')
            if is_restart: self.restart() #重新開始遊戲
            else: self.root.destroy() #關掉遊戲視窗
    '''計時'''
    def tick(self):
        if self.num_existing_cards == 0: return
        if self.num_seconds != 0:
            self.num_seconds -= 1
            self.time['text'] = f'Time Left: {self.num_seconds}'
            self.time.after(1000, self.tick)
        else:
            is_restart = messagebox.askyesno('遊戲結束', '嗚嗚嗚~你輸了，要再玩一次嗎？')
            if is_restart: self.restart()
            else: self.root.destroy()
    '''重新開始遊戲'''
    def restart(self):
        self.root.destroy()
        client = FlipCardByMemory()


'''run'''
if __name__ == '__main__':
    client = FlipCardByMemory()
