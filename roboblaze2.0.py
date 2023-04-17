import datetime
import random
import tkinter as tk


def prever_cores():
    seq = int(seq_var.get())

    data_e_hora_atuais = datetime.datetime.now()
    datahora = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

    lista = ['vermelho', 'preto', 'branco/preto', 'branco/vermelho']
    probs = [0.4, 0.4, 0.1, 0.1]
    esc = random.choices(range(4), weights=probs)[0]

    if seq == 1:
        resultado = 'Com a sequencia de vermelho, vermelho as {} \nO proximo sera {}'.format(datahora, lista[esc])
    elif seq == 2:
        resultado = 'Com a sequencia de preto, preto as {} \nO proximo sera {}'.format(datahora, lista[esc])
    elif seq == 3:
        resultado = 'Com a sequencia de vermelho, preto as {} \nO proximo sera {}'.format(datahora, lista[esc])
    elif seq == 4:
        resultado = 'Com a sequencia de preto, vermelho as {} \nO proximo sera {}'.format(datahora, lista[esc])
    else:
        resultado = 'Como apareceu branco até {} \nO proximo sera {}'.format(datahora, lista[esc])

    resultado_label.config(text=resultado)


# Criando a janela principal
janela = tk.Tk()
janela.title('ROBO DA BLAZE')

# Criando os widgets da interface
titulo_label = tk.Label(janela, text='ROBO DA BLAZE', font=('Arial', 16, 'bold'))
titulo_label.pack(pady=20)
titulo_label.config(fg='red')

seq_label = tk.Label(janela, text='Qual foi a ultima sequencia de cores?', font=('Arial', 12))
seq_label.pack(pady=10)

seq_var = tk.IntVar()
vermelho_vermelho_radio = tk.Radiobutton(janela, text='Vermelho, Vermelho', variable=seq_var, value=1)
vermelho_vermelho_radio.pack()
preto_preto_radio = tk.Radiobutton(janela, text='Preto, Preto', variable=seq_var, value=2)
preto_preto_radio.pack()
vermelho_preto_radio = tk.Radiobutton(janela, text='Vermelho, Preto', variable=seq_var, value=3)
vermelho_preto_radio.pack()
preto_vermelho_radio = tk.Radiobutton(janela, text='Preto, Vermelho', variable=seq_var, value=4)
preto_vermelho_radio.pack()
branco_radio = tk.Radiobutton(janela, text='Apareceu Branco', variable=seq_var, value=5)
branco_radio.pack()

prever_button = tk.Button(janela, text='Prever', font=('Arial', 12), command=prever_cores)
prever_button.pack(pady=20)

resultado_label = tk.Label(janela, text='', font=('Arial', 20))
resultado_label.pack()
resultado_label.config(fg='green')

# Iniciando a interface
janela.mainloop()
