from tkinter import *
import test_module

print(test_module.testAdd(1,2))
# def printHello():
#     print('HI')
#
# root = Tk()
#
# w = Label(root, text="Pthon Test")
# b = Button(root, text="hello python",command=printHello)
# c = Button(root, text="Quit",command=root.quit)
#
# w.pack()
# b.pack()
# c.pack()
#
# root.mainloop()
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
class MyError(Exception):
    pass
    
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")
