from tkinter import *
global scvalor 
global tela

def click(event):
    global scvalor
    
    texto = event.widget.cget("text")
    if texto == '=':
        if scvalor.get().isdigit():
            valor = int(scvalor.get())
        else: 
            valor = eval(tela.get())
            #scvalor = eval(tela.get())
            print(f"{type(valor)}")
        scvalor.set(valor)
        tela.update()

    elif texto == "C":
        scvalor.set("")
        tela.update()

    else:
        scvalor.set(scvalor.get() + texto)
        tela.update()


window = Tk()
window.geometry("320x490")
window.minsize(320, 490)
window.maxsize(320, 490)
window.config(background="#ccc")
window.title("Calculadora Básica - HILL-0xFF")
icone = PhotoImage(file = 'icon.png')
window.iconphoto(False, icone)

scvalor = StringVar()
scvalor.set("")
frm = Frame(window, padx= 20, pady= 20)
tela = Entry(frm, textvariable= scvalor, font= "Lucida 25 bold", background= "light blue")
tela.pack(fill= X, padx= 10, pady= 10)
frm.pack()

opcoes1 = ['7', '8', '9', ' + ']
opcoes2 = ['4', '5', '6', ' - ']
opcoes3 = ['1', '2', '3', ' * ']
opcoes4 = ['0', 'C', '=', ' / ']

frm = Frame(window, background="gray", padx= 30,pady=10)
for opcao in opcoes1:
    btn = Button(frm, text= opcao, padx= 10, pady= 10, font= "lucida 15 bold")
    btn.pack(side=LEFT, padx= 10, pady= 10)
    btn.bind("<Button-1>", click)
frm.pack()

frm = Frame(window, background= "gray", padx= 30, pady= 10)
for opcao in opcoes2:
    btn = Button(frm, text= opcao, padx= 10, pady= 10, font= "lucida 15 bold")
    btn.pack(side= LEFT, padx= 10, pady= 10)
    btn.bind("<Button-1>", click)
frm.pack()

frm = Frame(window, background="gray", padx= 30, pady= 10)
for opcao in opcoes3:
    btn = Button(frm, text= opcao, padx = 10, pady= 10, font = "lucida 15 bold")
    btn.pack(side= LEFT, padx= 10, pady = 10)
    btn.bind("<Button-1>", click)
frm.pack()

frm = Frame(window, background= "gray", padx = 30, pady = 10)
for opcao in opcoes4:
    btn = Button(frm , text= opcao, padx = 10, pady = 10, font = "lucida 15 bold")
    btn.pack(side = LEFT, padx = 10 , pady = 10)
    btn.bind("<Button-1>", click)
frm.pack()

window.mainloop()