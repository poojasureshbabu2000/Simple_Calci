from tkinter import*
#lambda
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
#clearfunction
def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")
#equals
def btnEqualsInputs():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""


cal = Tk()
cal.title("simple calculator")
operator=""
text_Input=StringVar()
#addition
txtDisplay = Entry(cal,fg='yellow',font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg='black', justify='right').grid(columnspan=4)
btn7=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='7',bg='black',command=lambda:btnClick('7')).grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8 , fg='yellow', font=('arial',20,'bold'),text='8',bg='black',command=lambda:btnClick('8')).grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='9',bg='black',command=lambda:btnClick('9')).grid(row=1,column=2)
addition=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='+',bg='black',command=lambda:btnClick('+')).grid(row=1,column=3)

#subtraction

btn4=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='4',bg='black',command=lambda:btnClick('4')).grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='5',bg='black',command=lambda:btnClick('5')).grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='6',bg='black',command=lambda:btnClick('6')).grid(row=2,column=2)
subtraction=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='-',bg='black',command=lambda:btnClick('-')).grid(row=2,column=3)

#multiplication

btn1=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='1',bg='black',command=lambda:btnClick('1')).grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='2',bg='black',command=lambda:btnClick('2')).grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='3',bg='black',command=lambda:btnClick('3')).grid(row=3,column=2)
multiplication=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='*',bg='black',command=lambda:btnClick('*')).grid(row=3,column=3)

#division
btn0=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='0',bg='black',command=lambda:btnClick('0')).grid(row=4,column=0)
btnclear=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='C',bg='black',command=lambda:btnClearDisplay()).grid(row=4,column=1)
btnequal=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='=',bg='black',command=lambda:btnEqualsInputs()).grid(row=4,column=2)
division=Button(cal,padx=16,bd=8, fg='yellow', font=('arial',20,'bold'),text='/',bg='black',command=lambda:btnClick('/')).grid(row=4,column=3)
cal.mainloop()