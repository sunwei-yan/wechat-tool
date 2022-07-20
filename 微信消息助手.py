import tkinter as tk
from typing import KeysView

import pyautogui as py
import pyperclip as pc
import time
def fs():
    x=0
    while x<999:
        n=0
        mc=t1.get('0.0','end')
        nr=t2.get('0.0','end')
        cs=t3.get('0.0','end')
        py.hotkey('ctrl','alt','w')
        time.sleep(1)
        py.hotkey('ctrl','f')
        pc.copy(mc)
        py.hotkey('ctrl', 'v')
        time.sleep(1)
        py.hotkey('enter')
        time.sleep(1)
        while n<int(cs):
            
            pc.copy(nr)
            py.hotkey('ctrl', 'v')
            py.hotkey('enter')
            n=n+1
        time.sleep(5)
        # py.hotkey('ctrl','alt','w')
        sr=input("输入退出或按回车键继续")
        if sr=="退出":
            x=1000

jm=tk.Tk()
jm.title("信息发送")
jm.geometry("500x500")

an=tk.Button(text="开始",width=10,height=1,command=fs).place(x=180,y=350)

t1=tk.Text(width=35,height=2);t1.place(x=167,y=50)
t1.get('0.0','end')
t2=tk.Text(width=35,height=2);t2.place(x=167,y=125)
t2.get('0.0','end')
t3=tk.Text(width=35,height=2);t3.place(x=167,y=200)
t3.get('0.0','end')
l1=tk.Label(text="用户名");l1.place(x=70,y=55)
l2=tk.Label(text="内容");l2.place(x=70,y=130)
l3=tk.Label(text="次数");l3.place(x=70,y=205)

jm.mainloop()
