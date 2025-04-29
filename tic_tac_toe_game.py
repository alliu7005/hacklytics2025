from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("1000x800")
lbl = Label(window, text= "TIC-TAC-TOE", font=('Algerian', '30'))
lbl.grid(row=0, column=0)
lbl = Label(window, text= "Player 1: X", font= ('Arial', '15'))
lbl.grid(row=1, column=0)
lbl = Label(window, text= "Player 2: O", font= ('Arial', '15'))
lbl.grid(row=2, column=0)



turn = "X"
def button_clicked(button):
    global turn
    if button["text"] == " ":
        button["text"] = turn
        turn = "O" if turn == "X" else "X"
        check()


counter = 1
def check():
    global counter
    b1, b2, b3, b4, b5, b6, b7, b8, b9 = [btn["text"] for btn in [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]]
    counter+=1


    if b1 == b2 and b1 == b3 and b1 == "O" or b1==b2 and b1==b3 and b1== "X": #row 1
        win(btn1["text"])
    elif b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X": #row 2
        win(btn4["text"])
    elif b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X": #row 3
        win(btn7["text"])
    elif b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X": #col 1
        win(btn1["text"])
    elif b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X": #col 2
        win(btn2["text"])
    elif b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X": #col 3
        win(btn3["text"])
    elif b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X": #diagonal 1
        win(btn1["text"])
    elif b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X": #diagonal 2
        win(btn7["text"])
    elif counter == 10:
        messagebox.showinfo("Tie", "Match Tied!!!")

        window.destroy()



def win(player):
    ans = (f"Game Complete! {player} is the winner")
    messagebox.showinfo("Congratulations, ", ans)
    window.destroy()




#creating buttons
btn1 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn1) )
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn2) )
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn3) )
btn3.grid(column=3, row=1)

btn4 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn4) )
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn5) )
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn6) )
btn6.grid(column=3, row=2)

btn7 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn7) )
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn8) )
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ",width=8,height=4,font=('Times Now','30'),command=lambda: button_clicked(btn9) )
btn9.grid(column=3, row=3)

window.mainloop()