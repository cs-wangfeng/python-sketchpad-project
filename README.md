# python画板程序

#### 简介
使用wxpython的控件以及pygame进行制作的画板程序，其中wxpython函数库产生控件窗口用于选择画笔颜色，而pygame函数库产生画板界面，在界面上也设置了按钮，诸如：选择画笔、选择橡皮、选择画笔的粗细、选择画笔的颜色，在画板界面上也显示了当前画笔的颜色以及粗细。  
  
以下为画板的显示界面：  
![画板显示界面](https://images.gitee.com/uploads/images/2021/0808/164206_b6f14cc7_9490403.png "屏幕截图 2021-08-08 164148.png")
  
以下为画笔颜色控件GUI界面的图片：  
![画笔颜色GUI控件](https://images.gitee.com/uploads/images/2021/0808/164413_0fca8328_9490403.png "屏幕截图 2021-08-08 164359.png")  
  
以下为画板绘制的效果图：  
![画板绘制效果图](https://images.gitee.com/uploads/images/2021/0808/164717_15308bb3_9490403.png "屏幕截图 2021-08-08 164623.png")  


#### 目录
|-task3.2  
         |-eraser.png      
         |-painter.png    
         |-plus.png  
         |-minus.png  
         |-task3.2.py  
         |-task3.2.pyproj  
         |-task3.2.sln  
         |-画板程序文件夹概述.txt  


#### 约束

1.  该文件夹中的.py文件需要在python编译器环境下运行（VS可以使用.sln文件运行）  
2.  该文件需要在电脑中安装pygame、wxpython库（方法：在cmd中输入‘pip install pygame’、‘pip install wxpython’）  


#### 编译构建

下载文件夹之后，在有python编译器环境前提下打开task3.2.py文件即可运行  

#### 说明

- 组件说明  
 
1.图片文件   
  
eraser.png -> 橡皮图片  
painter.png -> 画笔图片  
plus.png -> 加号图片  
minus.png -> 减号图片  
  
2.Python File (.py)  
  
task3.2.py
  
3.Python Project (.pyproj)  

task3.2.pyproj  
  
4.Visual Studio Solution (.sln)  

task3.2.sln  
  
  
- 使用说明  
  
下载文件夹之后，在有python编译器环境前提下打开task3.2.py文件即可运行  



#### 整体的架构思想

1.  使用pygame建立画板界面，定义画笔的颜色以及粗细，定义画板的大小，定义换班左侧控件区域的大小，定义一系列的按钮区域
2.  使用pygame函数监测鼠标位置以及鼠标的单击、移动的动作，从而在绘制过程中确保画笔在画板上留下痕迹。
3.  使用wxpython函数库建立新窗口，该GUI窗口包含对于画笔颜色的选择，选择某种颜色即可改变画在屏幕上的画笔痕迹的颜色
4.  通过画板窗口上实现设置的区域上的按钮，通过捕捉鼠标位置，也可实现画笔颜色的切换，并且也可以实现画笔粗细以及画笔与橡皮之间的切换
