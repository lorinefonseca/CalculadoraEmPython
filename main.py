#aqui importei a biblioteca tkinter 
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Calculadora") # título da window do programa
window.geometry("335x575") # largura e altura
window.resizable(False, False) # não deixar redimensionavel
window.configure(bg="#2b232e") # configurando a cor do fundo da janela principal


# criando as divisões da tela - display de resultado e janela com os botões

display_result = Frame(window, width=340, height=100, bg="#bcacc2")
display_result.grid(row=0, column=0)

window_buttons = Frame(window, width=340, height=500, bg="#2e1d36")
window_buttons.grid(row=1, column=0)

equation = ""

def show(value):
    global equation
    equation+=value
    display_label.config(text=equation)

def clear():
    global equation
    equation = ""
    display_label.config(text=equation)

def calculate():
    global equation
    result =""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    display_label.config(text=result)

# criando a label de resultado

display_label = Label(display_result, text="", width=14, height=2, relief=FLAT, padx=12, font=("Consolas", 30, "bold"), anchor="e", justify=RIGHT, bg="#3b2745", fg="#fff")
# anchor, define o ponto âncora, e no caso E, significa East // fg muda a cor do texto e significa foreground = primeiro plano
display_label.place(x=0, y=0)
display_label.pack()

#primeira linha de botoes

button_C = Button(window, text="C", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#a1328a", relief=FLAT, command=lambda: clear()).place(x=10, y=120)
button_division = Button(window, text="/", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#805276", relief=FLAT, command=lambda: show("/")).place(x=90, y=120)
button_percent = Button(window, text="%", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#805276", relief=FLAT, command=lambda: show("%")).place(x=170, y=120)
button_multiplication = Button(window, text="x", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#805276", relief=FLAT, command=lambda: show("*")).place(x=250, y=120)

#segunda linha de botoes

button_7 = Button(window, text="7", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("7")).place(x=10, y=210)
button_8 = Button(window, text="8", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("8")).place(x=90, y=210)
button_9 = Button(window, text="9", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("9")).place(x=170, y=210)
button_minus = Button(window, text="-", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#805276", relief=FLAT, command=lambda: show("-")).place(x=250, y=210)

#terceira linha de botoes

button_4 = Button(window, text="4", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("4")).place(x=10, y=300)
button_5 = Button(window, text="5", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("5")).place(x=90, y=300)
button_6 = Button(window, text="6", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("6")).place(x=170, y=300)
button_add = Button(window, text="+", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#805276", relief=FLAT, command=lambda: show("+")).place(x=250, y=300)

#quarta linha de botoes

button_1 = Button(window, text="1", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("1")).place(x=10, y=390)
button_2 = Button(window, text="2", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("2")).place(x=90, y=390)
button_3 = Button(window, text="3", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("3")).place(x=170, y=390)

#botao de igual -> exibir os resultados -> recebe a função calculate
button_equal = Button(window, text="=", width=3, height=3, font=("Consolas", 29, "bold"), bd=1, fg="#fff", bg="#85c7b8", relief=FLAT, command=lambda: calculate()).place(x=250, y=390)

#botoes restantes
button_0 = Button(window, text="0", width=7, height=1, font=("Consolas", 29, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show("0")).place(x=10, y=480)
button_dot = Button(window, text=".", width=3, height=1, font=("Consolas", 30, "bold"), bd=1, fg="#fff", bg="#695473", relief=FLAT, command=lambda: show(".")).place(x=170, y=480)


window.mainloop()