import tkinter as tk
import random
import os


def generate_and_check_random():
    random_number = random.randint(1, 6)

    if random_number !=6:
        result_label.config(text="很幸运逃过一劫！")

    if random_number == 6:
        result_label.config(text="恭喜你！中奖了！")

        delay_seconds = 1

        os.system(f'shutdown /s /t {delay_seconds}')


root = tk.Tk()
root.title("俄罗斯转盘")
root.geometry("300x200")

header_label = tk.Label(root, text="请扣动扳机！试试你的运气吧！")
header_label.pack()

result_label = tk.Label(root, text="")
result_label.place(relx=0.5, rely=0.4, anchor='center')

generate_button = tk.Button(root, text="扣动扳机", command=generate_and_check_random)
generate_button.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()
