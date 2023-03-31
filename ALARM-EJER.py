from tkinter import  messagebox , Label,Tk,ttk
from time import   strftime
from pygame import mixer

ventana = Tk()
ventana.config(bg='BLACK')
ventana.geometry('500x250')
ventana.title('Alarma')
ventana.minsize(width=500, height=250)
mixer.init()

lista_horas = []
lista_minutos = []
lista_segundos = []

for  i in range(0,24):
	lista_horas.append(i)
for  i in range(0,60):
	lista_minutos.append(i)
for  i in range(0,60):
	lista_segundos.append(i)

Hora = Label(ventana, text= 'Hora', bg= 'BLACK', fg= 'BLUE', font= ('Arial',12, 'bold'))
Hora.grid(row=1, column=0, padx =5, pady=5)
Minu = Label(ventana, text= 'Minutos', bg= 'BLACK', fg= 'BLUE', font= ('Arial',12, 'bold'))
Minu.grid(row=1, column=1, padx =5, pady=5)
Seg = Label(ventana, text= 'Segundos', bg= 'BLACK', fg= 'BLUE', font= ('Arial',12, 'bold'))
Seg.grid(row=1, column=2, padx =5, pady=5)

HORAPRO = ttk.Combobox(ventana, values = lista_horas , style = "TCombobox", justify='center',width='12', font='Arial')
HORAPRO.grid(row=2, column=0, padx =15, pady=5)
HORAPRO.current(0)
MINPRO = ttk.Combobox(ventana, values = lista_minutos , style = "TCombobox", justify='center',width='12', font='Arial')
MINPRO.grid(row=2, column=1, padx =15, pady=5)
MINPRO.current(0)
SEGPRO = ttk.Combobox(ventana, values = lista_segundos , style = "TCombobox", justify='center',width='12', font='Arial')
SEGPRO.grid(row=2, column=2, padx =15, pady=5)
SEGPRO.current(0)

style = ttk.Style()
style.theme_create('combostyle', parent='alt',settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'red',
                                       'fieldbackground': '#00FFE3',
                                       'background': 'blue'
                                       }}})
style.theme_use('combostyle')

ventana.option_add('*TCombobox*Listbox*Background', 'white')
ventana.option_add('*TCombobox*Listbox*Foreground', 'BLACK')
ventana.option_add('*TCombobox*Listbox*selectBackground', 'WHITE')
ventana.option_add('*TCombobox*Listbox*selectForeground', 'BLACK')

alarma = Label(ventana,  fg = 'WHITE', bg='BLACK', font = ('Radioland', 20))
alarma.grid(column=0, row=3, sticky="nsew", ipadx=5, ipady=20)
repetir = Label(ventana,  fg = 'white', bg='BLACK', text = 'Repetir', font='Arial')
repetir.grid(column=1, row=3, ipadx=5, ipady=20)
cantidad = ttk.Combobox(ventana, values = (1,2,3,4,5), justify='center',width='8', font='Arial')
cantidad.grid(row=3, column=2, padx =5, pady=5)
cantidad.current(0)

def HORA():
	x_hora = HORAPRO.get()
	x_minutos = MINPRO.get()
	x_segundos = SEGPRO.get()

	hora =  strftime('%H')
	minutos = strftime('%M')
	segundos = strftime('%S')

	hora_total = (hora + ' : '+ minutos+ ' : '+ segundos)
	texto_hora.config(text=hora_total, font = ('Radioland', 25))

	hora_alarma = x_hora +' : '+ x_minutos +' : '+ x_segundos
	alarma['text']= hora_alarma
	#condicion:
	if int(hora) == int(x_hora):
		if int(minutos) == int(x_minutos):
			if int(segundos) == int(x_segundos):								
				mixer.music.load("alarm-clock.mp3")
				mixer.music.play(loops= int(cantidad.get()))
				messagebox.showinfo(message=hora_alarma, title="Alarma")

	texto_hora.after(100, HORA)
texto_hora = Label(ventana,  fg = 'WHITE', bg='BLACK')
texto_hora.grid(columnspan=3, row=0,sticky="nsew", ipadx=5, ipady=20)
HORA()

ventana.mainloop()