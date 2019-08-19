import tkinter as tk
import xlrd
import xlwt
import matplotlib.pyplot as plt
import numpy as np
def huatu(result):
    plt.figure(figsize=(500,500))
    plt.plot(x,result,'b',label='Data')
    plt.show
    plt.savefig("result.png")

def excel(result):
    new_workbook = xlwt.Workbook()  #‘W’必须大写
    worksheet = new_workbook.add_sheet('1')
    for i in range(0,np.length(result)):
        worksheet.write(0,0,'test')
    new_workbook.save('atdesk/wttest.xlsx')

def main():
    visual()


def visual():
    window = tk.Tk()
    window.title('my window')
    window.geometry('400x200')
    e = tk.Entry(window)
    e.pack()
    t = tk.Text(window,height=2)
    t.pack()
    def insert():
        var = e.get()
        num = int(var)    
        t.insert('end','计算完成')

    b = tk.Button(window,text='输入',width = 15,
    height=2,command=insert)
    b.pack()
    window.mainloop()

def cal(num):
    q1 = np.array([0.5,0.55,0.6,0.65,0.7])
    k1 = np.array([0.95,0.96,0.97,0.98])
    k2 = np.array([0.97,0.98,0.99])
    a = num







if __name__ == "__main__":
    main()




