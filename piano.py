from tkinter import*
import time
import datetime
import pygame

pygame.init()
root = Tk()
root.title("Music Box")
root.geometry('1500x800+0+0')
root.configure(background='#40E0D0')

ABC = Frame(root, bg="#00FFFF", bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(ABC, bg="#00FFFF", bd=20, relief=RIDGE)
ABC1.grid()
ABC2 = Frame(ABC, bg="#00FFFF",  relief=RIDGE)
ABC2.grid()
ABC3 = Frame(ABC, bg="#00FFFF",  relief=RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Just Like Music")
Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
# =======================Music==============================================


def value_Cs():
    str1.set("C#")
    sound = pygame.mixer.Sound(
        "C:My_New_Resources\Python_work\Workspace\Workspace\Resources\C_s.wav")
    sound . play()


# =======================Label with Title==============================================


Label(ABC1, text="Piano Music Keys", font=('arial', 25, 'bold'), padx=565, pady=8,
      bd=4, bg="#DE3163", fg='#DFFF00', justify=CENTER).grid(row=0, column=0, columnspan=11)
# =======================Label with Title==============================================
txtDate = Entry(ABC1, textvariable=Date1, font=('arial', 18, 'bold'),
                bd=34, bg="#00008B", width=31, fg='#FFBF00', justify=CENTER).grid(row=1, column=0, pady=1)

txtDisplay = Entry(ABC1, textvariable=str1, font=('arial', 18, 'bold'),
                   bd=34, bg="#00008B", width=31, fg='#FFBF00', justify=CENTER).grid(row=1, column=1, pady=1)

txtTime = Entry(ABC1, textvariable=Time1, font=('arial', 18, 'bold'),
                bd=34, bg="#00008B", width=31, fg='#FFBF00', justify=CENTER).grid(row=1, column=2, pady=1)
# =======================Label with Title==============================================
btnCs = Button(ABC2, height=7, width=6, bd=4, text="C#", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnCs.grid(row=0, column=0, padx=5, pady=5)

btnDs = Button(ABC2, height=7, width=6, bd=4, text="D#", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnDs.grid(row=0, column=1, padx=5, pady=5)

btnSpace2 = Button(ABC2, state=DISABLED, height=6,
                   width=2, bg="#00FFFF", relief=FLAT)
btnSpace2.grid(row=0, column=3, padx=0, pady=0)

btnFs = Button(ABC2, height=7, width=6, bd=4, text="F#", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnFs.grid(row=0, column=4, padx=5, pady=5)

btnGs = Button(ABC2, height=7, width=6, bd=4, text="G#", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnGs.grid(row=0, column=6, padx=5, pady=5)

btnBb = Button(ABC2, height=7, width=6, bd=4, text="Bb", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnBb.grid(row=0, column=8, padx=5, pady=5)

btnSpace5 = Button(ABC2, state=DISABLED, height=6,
                   width=2, bg="#00FFFF", relief=FLAT)
btnSpace5.grid(row=0, column=7, padx=0, pady=0)

btnCs1 = Button(ABC2, height=7, width=6, bd=4, text="C#1", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnCs1.grid(row=0, column=10, padx=5, pady=5)

btnDs1 = Button(ABC2, height=7, width=6, bd=4, text="D#1", font=(
    'arial', 18, 'bold'), bg="#00008B", fg='white')
btnDs1.grid(row=0, column=12, padx=5, pady=5)
# =======================Label with Title==============================================
btnC = Button(ABC3, height=10, width=6, bd=4, text="C", bg="white", fg='black', font=(
    'arial', 18, 'bold'), command=value_Cs)
btnC.grid(row=0, column=0, padx=5, pady=5)

btnD = Button(ABC3, height=10, width=6, bd=4, text="D", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnD.grid(row=0, column=1, padx=5, pady=5)

btnE = Button(ABC3, height=10, width=6, bd=4, text="E", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnE.grid(row=0, column=2, padx=5, pady=5)

btnF = Button(ABC3, height=10, width=6, bd=4, text="F", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(ABC3, height=10, width=6, bd=4, text="G", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnG.grid(row=0, column=4, padx=5, pady=5)

btnA = Button(ABC3, height=10, width=6, bd=4, text="A", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnA.grid(row=0, column=5, padx=5, pady=5)

btnB = Button(ABC3, height=10, width=6, bd=4, text="B", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnB.grid(row=0, column=6, padx=5, pady=5)

btnC1 = Button(ABC3, height=10, width=6, bd=4, text="C1", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(ABC3, height=10, width=6, bd=4, text="D1", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnD1.grid(row=0, column=8, padx=5, pady=5)

btnE1 = Button(ABC3, height=10, width=6, bd=4, text="E1", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnE1.grid(row=0, column=9, padx=5, pady=5)

btnF1 = Button(ABC3, height=10, width=6, bd=4, text="F1", bg="white", fg='black', font=(
    'arial', 18, 'bold'))
btnF1.grid(row=0, column=10, padx=5, pady=5)


# =======================Label with Title==============================================


root.mainloop()
