import pyautogui
import time




#进入红包


def HongBaoTest():
    xy = pyautogui.locateOnScreen('.\pic\hbfm.png')
    xy2= pyautogui.locateOnScreen('.\pic\yiling.png')
    try:
        if xy.left<960 or xy2.left<960:
            return True
    except:
        return False
    
    

def HongBao():
    xy = pyautogui.locateOnScreen('.\pic\hbfm.png')  
    center = pyautogui.center(xy)
    pyautogui.click(center)
    pyautogui.click(center)
    xy2 = pyautogui.locateOnScreen('.\pic\yiling.png')  
    center = pyautogui.center(xy2)
    pyautogui.click(center)
    pyautogui.click(center)
    print('进入红包')
    

#领取红包

def KaiTest():
    xy=pyautogui.locateOnScreen('.\pic\kai.png')
    try:
        if xy.left:
            return True
    except:
        return False
def Kai():
    xy = pyautogui.locateOnScreen('.\pic\kai.png')  # 寻找刚才保存点赞手势图片
    center = pyautogui.center(xy) # 寻找图片的中心 
    pyautogui.click(center)
    pyautogui.click(center)
    print('领取红包')


def Guan():
    xy = pyautogui.locateOnScreen('.\pic\fanhui.png')  # 寻找刚才保存点赞手势图片
    center = pyautogui.center(xy) # 寻找图片的中心 
    pyautogui.click(center)
    print('已返回')

def YouJian():
    xy = pyautogui.locateOnScreen('.\pic\hbfm.png')
    center = pyautogui.center(xy)
    pyautogui.rightClick(center)
    print('右键红包')

def ShanChu():
    xy = pyautogui.locateOnScreen('.\pic\scbutton.png')  
    center = pyautogui.center(xy)
    pyautogui.click(center)
    print('删除红包')
def QueRenSC():
    xy = pyautogui.locateOnScreen('.\pic\redsc.png')  
    center = pyautogui.center(xy)
    pyautogui.click(center)
    print('确认删除')
while True:
    if HongBaoTest():
        HongBao()
        print("打开红包")
        time.sleep(0.3)
        if KaiTest():
            Kai()
            print("领取成功！")
            time.sleep(1.7)
        Guan()
        time.sleep(1)
        YouJian()
        time.sleep(1)
        ShanChu()
        time.sleep(1)
        QueRenSC()
    if KaiTest():
        Kai()
        print("领取成功！")
    time.sleep(0.3)
    

