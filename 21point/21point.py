import tkinter as tk 
import random as ra
import time
import tkinter.messagebox

class poke(object):
    __Type__=0
    __Number__=0

    def __init__(self,types,numbers):
        self.__Type__=types
        self.__Number__=numbers
#初始桌面
win=tk.Tk()
win.geometry('800x600')
win.title('21点')
image_back=tk.PhotoImage(file='./images/rear.gif')
canvas=tk.Canvas(win,bg='green',width=800,height=600)
canvas.create_image(390,250,image=image_back)#充当牌组显示一个牌的背面
canvas.pack()
#初始牌组
types=[1,2,3,4]
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13]
player=[]
computer=[]
cards=[]
image_pock=[]
image_pockback=[]
#p=numbers
point=0
for t in types:
    for n in numbers:
        po=poke(t,n)
        cards.append(po)
#随机打乱
ra.shuffle(cards)
#求和
def countNum(l):
    count=0
    for b in l:
        if b.__Number__>10:
            b.__Number__=10
        count=count+b.__Number__
    return count

#抽牌
def getpock():
    
    #玩家抽牌
    global point
    i=0
    player.append(cards[point])
    global image_pock
    image_pock=[0]*len(player)
    point=point+1
    for p_p in player:
        imagefile='./images/{0}-{1}.gif'.format(p_p.__Type__,p_p.__Number__)
        image_pock[i]=tk.PhotoImage(file=imagefile)
        canvas.create_image((300+i*20,400),image=image_pock[i])
        canvas.pack()
        i=i+1
    win.update()
    #判断是否爆牌
    count=countNum(player)
    if count >= 21:
        tk.messagebox.showinfo('提示','player牌炸了')
        win.destroy()
        return
    #电脑判断其牌组是否应该抽牌

    if 21-countNum(computer)<=5:
        stop()
        return

    #电脑抽牌
    i=0 
    computer.append(cards[point])
    global image_pockback
    image_pockback=[0]*len(computer)
    for c_p in computer:
        imagefile='./images/rear.gif'
        image_pockback[i]=tk.PhotoImage(file=imagefile)
        canvas.create_image((300+i*20,100),image=image_pockback[i])
        canvas.pack()
        i=i+1
    win.update()
    point=point+1
    print(countNum(computer))
    #判断是否爆牌
    count=countNum(computer)
    if count >= 21:
        tk.messagebox.showinfo('提示','电脑牌炸了')
        win.destroy()
    
def stop():
    count_player=countNum(player)
    count_computer=countNum(computer)
    if count_computer > count_player:
        tk.messagebox.showinfo('提示','电脑赢了')
        win.destroy()
    if count_computer < count_player:
        tk.messagebox.showinfo('提示','你赢了')
        win.destroy()
    if count_computer == count_player:
        tk.messagebox.showinfo('提示','平局')
        win.destroy()



#放置按钮
#image=tk.PhotoImage(file='./images/2-1.gif')
button=tk.Button(canvas,text='抽牌',width=10,command=getpock)
button.place(x=310,y=500,anchor='nw')
button1=tk.Button(canvas,width=10,text='停牌',command=stop)
button1.place(x=410,y=500,anchor='nw')
win.mainloop()

