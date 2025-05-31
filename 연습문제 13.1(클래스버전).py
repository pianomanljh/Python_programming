import tkinter as tk
from tkinter import ttk

class change_ondo:
    def __init__(self):
        self.win = tk.Tk()
        self.buildGUI()

    def buildGUI(self):
        self.btn_group1 = ttk.Frame(self.win)
        self.text1 = ttk.Label(self.btn_group1, text='화씨')
    
        self.F = tk.IntVar()
        input_entry1 = ttk.Entry(self.btn_group1, textvariable=self.F, width=11, justify='right')
        self.text2 = ttk.Label(self.btn_group1, text='섭씨')
    
        self.C = tk.DoubleVar()
        input_entry2 = ttk.Entry(self.btn_group1, textvariable=self.C, width=11, justify='right')
    
        self.btn_group3 = ttk.Frame(self.win)
        btn1 = ttk.Button(self.btn_group3,
                          text='화씨->섭씨', command=self.btn_handler1)
        btn2 = ttk.Button(self.btn_group3,
                          text='섭씨->화씨', command=self.btn_handler2)
        btn3 = ttk.Button(self.btn_group3,
                          text='초기화', command=self.btn_reset)
        btn4 = ttk.Button(self.btn_group3,
                          text='종료', command=self.btn_quit)

       

        self.text1.pack(side=tk.LEFT)
        input_entry1.pack(padx=0, ipadx=0, side=tk.LEFT)
        self.text2.pack(side=tk.LEFT)
        input_entry2.pack(side=tk.LEFT)
        self.btn_group1.grid(row=0, column=1)
    
        btn1.pack(side=tk.LEFT)
        btn2.pack(side=tk.LEFT)
        btn3.pack(side=tk.LEFT)
        btn4.pack(side=tk.LEFT)
        self.btn_group3.grid(row=1, column=1)

    def btn_handler1(self):
        self.C.set((self.F.get()-32)/1.8)
    
    def btn_handler2(self):
        self.F.set(self.C.get()*1.8+32)

    def btn_reset(self):
        self.C.set(0.0)
        self.F.set(0.0)

    def btn_quit():
        self.win.destroy()

change = change_ondo()
change.win.mainloop()
