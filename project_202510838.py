import random
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ReactionTime:
    def __init__(self):
        self.win = tk.Tk()
        self.style = ttk.Style()
        self.win.geometry('1800x800')
        self.win.configure(background='LightSkyBlue')
        self.win.title('반응 속도 테스트')
        self.result = []
        self.score_list = []
        self.buildGUI()

    def buildGUI(self):
        self.label = ttk.Label(self.win, text = '준비되면 횟수를 입력하고 시작 버튼을 누르세요.',
                               font = ('맑은고딕', 40),
                               background='LightSkyBlue')
        self.label.pack(pady=100)

        self.count_label = ttk.Label(self.win, text = '횟수 입력 및 랭킹모드 여부 선택',font=('맑은고딕', 20), background='LightSkyBlue')
        self.count_label.pack()

        # 횟수, 랭킹모드, 순위표
        self.frame_mode = ttk.Frame(self.win)
        self.lavbel_count=ttk.Label(self.frame_mode, text='횟수:', font=('맑은고딕', 15))
        self.lavbel_count.grid(row=0, column=0)
        self.count = tk.IntVar()
        self.input_count = ttk.Entry(self.frame_mode, textvariable = self.count, width=10)
        self.input_count.grid(row=0, column=1, padx=10)
        self.check_ranking = tk.IntVar()
        self.c1 = ttk.Checkbutton(self.frame_mode, text='랭킹모드', variable=self.check_ranking)
        self.c1.grid(row=0, column=2, padx=30, sticky='e')
        self.btn_ranking = ttk.Button(self.frame_mode, text='순위표보기', command=self.show_scores)
        self.btn_ranking.grid(row=0, column=3, padx=10)
        self.frame_mode.pack(pady = 10)

        self.btn_start = ttk.Button(self.win, text='시작', command=self.start_test,
                                    width = 100)
        self.btn_start.pack(pady = 40, ipady = 80)

        self.btn_quit = ttk.Button(self.win, text='종료', command=self.quit,
                                   width = 100)
        self.btn_quit.pack(ipady = 20)

        

    def start_test(self):
        if self.count.get() > 0:
            self.delay = random.uniform(2, 5) * 1000
            self.label.config(text='초록색을 기다리세요...', background='salmon', font=('맑은고딕', 40))
            self.win.configure(background='salmon')
            self.btn_start.config(text='배경이 초록색으로 바뀌면 여기를 클릭하세요!')
            self.btn_start.config(command=self.too_fast)
            self.new_after = self.win.after(int(self.delay), self.signal)
            self.count_label.pack_forget()
            self.input_count.pack_forget()
            self.frame_mode.pack_forget()
        else:
            messagebox.showwarning('경고', '횟수를 1회 이상 입력하세요!')

    def too_fast(self):
        self.win.after_cancel(self.new_after)
        self.label.config(text='너무 빨리 클릭했습니다! 다시 시도하세요.', background='LightSkyBlue')
        self.win.configure(background='LightSkyBlue')
        self.btn_start.config(command=self.start_test, text='시작')


    def signal(self):
        self.win.configure(background='lime')
        self.label.config(text='지금 클릭하세요!', background='lime')
        self.change_time = time.time()
        self.btn_start.config(command=self.record_reaction, text = '클릭')
    
    def record_reaction(self):
        self.click_time = time.time()
        reaction_time = self.click_time - self.change_time
        self.label.config(text=f'반응속도: {reaction_time:.3f}초', background='LightSkyBlue', font = ('맑은고딕', 40))
        self.win.configure(background='LightSkyBlue')
        self.count.set(self.count.get()-1)
        self.result.append(reaction_time)

        if self.count.get() > 0:
            self.btn_start.config(command=self.start_test, text='시작')
            self.btn_start.pack_forget()
            self.btn_quit.pack_forget()

            self.countdown_label = ttk.Label(self.win)
            self.countdown_label.pack()
            for i in range(3):
                self.countdown_label.config(text=f'{3-i}', font=('맑은고딕', 50)
                                            , background='LightSkyBlue')
                self.win.update()
                time.sleep(1)
                
            self.countdown_label.pack_forget()
            self.btn_start.pack(pady = 40, ipady = 80)
            self.btn_quit.pack(ipady = 20)
            self.start_test()
        
        else:
            self.btn_start.pack_forget()
            self.btn_quit.pack_forget()
            self.label1 = ttk.Label(text='평균 반응 속도 계산 중...', font=('맑은고딕', 40), background='LightSkyBlue')
            self.label1.pack()
            self.win.update()
            time.sleep(3)
            self.label1.pack_forget()
            self.label.config(text=f'평균 반응 속도: {(sum(self.result)/len(self.result)):.3f}초'
                              , font = ('맑은고딕', 60)
                              , background='LightSkyBlue')
            
            if self.check_ranking.get() == 1:
                messagebox.showinfo('랭킹모드', '순위표에 저장할 이름을 입력하세요')

                self.frame = ttk.Frame(self.win)
                self.label_save = ttk.Label(self.frame, text='이름 입력 :', font=('맑은고딕', 20))
                self.label_save.grid(row=0, column=0, padx=10)
                self.name = tk.StringVar()
                self.entry_name = ttk.Entry(self.frame, textvariable=self.name, width=40)
                self.entry_name.grid(row=0, column=1, padx=10)
                self.btn_save = ttk.Button(self.frame, text='저장', command=self.save)
                self.btn_save.grid(row=0, column=2, padx=10)
                self.btn_ranking1 = ttk.Button(self.frame, text='순위표보기', command=self.show_scores)
                self.btn_ranking1.grid(row=0, column=3, padx=10)
                self.frame.pack(pady=20)
            
            
            self.btn_quit.pack(ipady = 40, pady = 60)
    
    def save(self):
        messagebox.showinfo('랭킹모드', '순위표에 점수가 저장되었습니다')
        with open('score.txt', 'a', encoding='utf-8') as file:
            file.write(f'{self.name.get()}: {(sum(self.result)/len(self.result)):.3f}초\n')
    
    def load(self):
        self.score_list.clear()
        try:
            with open('score.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    self.score_list.append(line.strip())
        except:
            messagebox.showinfo('랭킹모드', '저장된 점수가 없습니다.')
        
        for i in range(len(self.score_list)-1,0,-1):
            for j in range(0,i,1):
                a = self.score_list[j].find(':')+1
                b = self.score_list[j+1].find(':')+1
                if float(self.score_list[j][a:-2]) > float(self.score_list[j+1][b:-2]):
                    self.score_list[j], self.score_list[j+1] = self.score_list[j+1], self.score_list[j]

    def show_scores(self):
        self.load()
        self.win2 = tk.Tk()
        self.win2.geometry('400x600')
        self.win2.configure(background='LightYellow')
        self.win2.title('순위표')
        label_title = ttk.Label(self.win2, text='순위표', font=('맑은고딕', 30), background='LightYellow')
        label_title.pack(pady=20)
        for i in range(len(self.score_list)):
            score_label = ttk.Label(self.win2, text=f'{i+1}. {self.score_list[i]}', font=('맑은고딕', 20),
                                    background='LightYellow')
            score_label.pack()
        self.btn_quit2 = ttk.Button(self.win2, text='순위표 나가기', command=self.win2.destroy, width=20)
        self.btn_quit2.pack(pady=20)
        self.win2.mainloop()
        
    
    def quit(self):
        self.win.destroy()
    


game_test = ReactionTime()
game_test.win.mainloop()
