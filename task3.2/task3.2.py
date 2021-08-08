import sys
import wx
import time
import pygame
import random
from pygame.locals import *


is_start = False
running = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (201,151,124)
BIGBROWN=(138,86,57)
CHOCOLATE=(210,105,30)
PURPLE=(162,32,240)
TURKEY=(0,199,140)
ORANGE=(255,69,0)
BERRY=(221,160,221)
RICE=(163,148,128)
SKY=(185,255,255)
FOREST=(34,139,34)
GREY=(192,192,192)
color=0
col=BLACK
width=9
w=23
class FrameUI(wx.Frame):

    def __init__(self, parent, title):
        super(FrameUI, self).__init__(parent, title=title, size=(300, 200))

        # function for in-frame components
        self.InitUI()

    def InitUI(self):
        # parent panel for radio box
        pnl = wx.Panel(self)

        # list of choices
        lblList = ['BLACK','RED','GREEN','BLUE','BROWN','BIGBROWN','CHOCOLATE','PURPLE','TURKEY','ORANGE','BERRY','RICE','SKY','FOREST','GREY']

        # create radio boc containing above list
        self.rbox = wx.RadioBox(pnl, label='RadioBox', pos=(10, 10), choices=lblList,
                                majorDimension=5, style=wx.RA_SPECIFY_ROWS)
        # c
        self.rbox.SetItemToolTip(0, "Item One")

        # print the index of the selected item
        # set frame in centre
        self.Centre()
        # set size of frame
        self.SetSize((400, 250))
        # show output frame
        self.Show(True)
        self.Bind(wx.EVT_RADIOBOX, self.EvtCheckBox, self.rbox)
    def EvtCheckBox(self, event):
        global color
        global col
        color=(self.rbox.GetSelection())
        if color==0:
            col=BLACK
        if color==1:
            col=RED
        if color==2:
            col=GREEN
        if color==3:
            col=BLUE
        if color==4:
            col=BROWN
        if color==5:
            col=BIGBROWN
        if color==6:
            col=CHOCOLATE
        if color==7:
            col=PURPLE
        if color==8:
            col=TURKEY
        if color==9:
            col=ORANGE
        if color==10:
            col=BERRY
        if color==11:
            col=RICE
        if color==12:
            col=SKY
        if color==13:
            col=FOREST
        if color==14:
            col=GREY
        screen.fill(WHITE)
        screen.blit(eraser, (10,100))
        screen.blit(painter, (10,10))
        screen.blit(ClearImage, (10, 360))
        pygame.draw.rect(screen, BLACK, (10, 200,80 ,80), 2)
        pygame.draw.circle(screen,col,[50,240],width,width)
        #添加加和减按钮#
        screen.blit(plus, (15,285))
        screen.blit(minus, (55,285))
        pygame.draw.circle(screen,BLACK,[25,420],w,w)
        pygame.draw.circle(screen,RED,[80,420],w,w)
        pygame.draw.circle(screen,GREEN,[25,470],w,w)
        pygame.draw.circle(screen,BLUE,[80,470],w,w)
        pygame.draw.circle(screen,BROWN,[25,520],w,w)
        pygame.draw.circle(screen,BIGBROWN,[80,520],w,w)
        pygame.draw.circle(screen,CHOCOLATE,[25,570],w,w)
        pygame.draw.circle(screen,PURPLE,[80,570],w,w)
        pygame.draw.circle(screen,TURKEY,[25,620],w,w)
        pygame.draw.circle(screen,ORANGE,[80,620],w,w)
        pygame.draw.circle(screen,BERRY,[25,670],w,w)
        pygame.draw.circle(screen,RICE,[80,670],w,w)
        pygame.draw.circle(screen,SKY,[25,720],w,w)
        pygame.draw.circle(screen,FOREST,[80,720],w,w)
        pygame.draw.circle(screen,GREY,[25,770],w,w)
        pygame.display.update()
            
ex = wx.App()
t = FrameUI(None, 'RadioButton and RadioBox')




pygame.init()
pygame.mixer.init()
# 创建窗口
screen = pygame.display.set_mode((800, 800))
# 设置窗口名称
pygame.display.set_caption("My Game")
myfont = pygame.font.Font(None,45)
# 加载所需的图像资源
painter = pygame.image.load('../task3.2/painter.png').convert_alpha()
eraser = pygame.image.load('../task3.2/eraser.png').convert()
plus = pygame.image.load('../task3.2/plus.png').convert_alpha()
minus = pygame.image.load('../task3.2/minus.png').convert_alpha()
ClearImage = myfont.render("Clear", True, RED)   
screen.fill(WHITE)
screen.blit(eraser, (10,100))
screen.blit(painter, (10,10))
screen.blit(ClearImage, (10, 360))
pygame.draw.rect(screen, BLACK, (10, 200,80 ,80), 2)
pygame.draw.circle(screen,col,[50,240],width,width)
screen.blit(plus, (15,285))
screen.blit(minus, (55,285))    
pygame.draw.circle(screen,BLACK,[25,420],w,w)
pygame.draw.circle(screen,RED,[80,420],w,w)
pygame.draw.circle(screen,GREEN,[25,470],w,w)
pygame.draw.circle(screen,BLUE,[80,470],w,w)
pygame.draw.circle(screen,BROWN,[25,520],w,w)
pygame.draw.circle(screen,BIGBROWN,[80,520],w,w)
pygame.draw.circle(screen,CHOCOLATE,[25,570],w,w)
pygame.draw.circle(screen,PURPLE,[80,570],w,w)
pygame.draw.circle(screen,TURKEY,[25,620],w,w)
pygame.draw.circle(screen,ORANGE,[80,620],w,w)
pygame.draw.circle(screen,BERRY,[25,670],w,w)
pygame.draw.circle(screen,RICE,[80,670],w,w)
pygame.draw.circle(screen,SKY,[25,720],w,w)
pygame.draw.circle(screen,FOREST,[80,720],w,w)
pygame.draw.circle(screen,GREY,[25,770],w,w)
pygame.display.update()



while True: # 死循环不断检查
    
    for event in pygame.event.get():  #遍历事件列表中的事件
        x,y = pygame.mouse.get_pos()
        print(x,y)
        if event.type == QUIT:
            pygame.display.quit()
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            #清空画板
            if (10<x and x<95) and (360<y and y<390):
                screen.fill(WHITE)
                screen.blit(eraser, (10,100))
                screen.blit(painter, (10,10))
                screen.blit(ClearImage, (10, 360))
                pygame.draw.rect(screen, BLACK, (10, 200,80 ,80), 2)
                pygame.draw.circle(screen,col,[50,240],width,width)
                #添加加和减按钮#
                screen.blit(plus, (15,285))
                screen.blit(minus, (55,285))
                pygame.draw.circle(screen,BLACK,[25,420],w,w)
                pygame.draw.circle(screen,RED,[80,420],w,w)
                pygame.draw.circle(screen,GREEN,[25,470],w,w)
                pygame.draw.circle(screen,BLUE,[80,470],w,w)
                pygame.draw.circle(screen,BROWN,[25,520],w,w)
                pygame.draw.circle(screen,BIGBROWN,[80,520],w,w)
                pygame.draw.circle(screen,CHOCOLATE,[25,570],w,w)
                pygame.draw.circle(screen,PURPLE,[80,570],w,w)
                pygame.draw.circle(screen,TURKEY,[25,620],w,w)
                pygame.draw.circle(screen,ORANGE,[80,620],w,w)
                pygame.draw.circle(screen,BERRY,[25,670],w,w)
                pygame.draw.circle(screen,RICE,[80,670],w,w)
                pygame.draw.circle(screen,SKY,[25,720],w,w)
                pygame.draw.circle(screen,FOREST,[80,720],w,w)
                pygame.draw.circle(screen,GREY,[25,770],w,w)
                pygame.display.update()
                
            #调整笔的粗细#
            elif (15<x and x<50) and (285<y and y<320):
                width = width + 3
                # 笔的粗细，最大为35
                if width>35:
                    width=35
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()

            elif (55<x and x<92) and (285<y and y<320):
                width = width - 3
                # 笔的粗细，最小为1
                if width<1:
                    width=1
                pygame.draw.circle(screen,WHITE,[50,240],35,35)
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif(13<x<94) and (109<y<179):
                col=WHITE
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif(10<x<89) and (13<y<94):
                col=BLACK
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()

            
            
            #更换颜色#
            elif (2<x<48) and (400<y<440):
                col=BLACK
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (400<y<440):
                col=RED
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (447<y<490):
                col=GREEN
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (447<y<490):
                col=BLUE
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (497<y<544):
                col=BROWN
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (497<y<544):
                col=BIGBROWN
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (547<y<593):
                col=CHOCOLATE
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (547<y<593):
                col=PURPLE
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (597<y<643):
                col=TURKEY
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (597<y<643):
                col=ORANGE
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (649<y<694):
                col=BERRY
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (649<y<694):
                col=RICE
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (697<y<743):
                col=SKY
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (57<x<103) and (697<y<743):
                col=FOREST
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            elif (2<x<48) and (749<y<793):
                col=GREY
                pygame.draw.circle(screen,col,[50,240],width,width)
                pygame.display.update()
            
            else:
                # 实现在屏幕上点击就画圆点的功能。
                if x>113:
                    pygame.draw.circle(screen, col, (x,y), width-2)
                    a,b = pygame.mouse.get_pos()
                    pygame.draw.line(screen,col, (x,y), (a,b), width*2)         #绘制线条
                    pygame.display.update()
                    # 设置是否开始画线为True
                    is_start = True
        elif event.type==MOUSEMOTION:
            if (is_start==True) and x>113: 
                pygame.draw.circle(screen, col, (x,y), width-2)
                pygame.draw.line(screen,col, (x,y), (a,b), width*2)         #绘制线条
                a,b = pygame.mouse.get_pos()
                pygame.display.update()
                
        elif event.type==MOUSEBUTTONUP:
            # 设置是否开始画线为False,即停止画线
            is_start=False
        
ex.MainLoop()
