import pandas as pd
import pyautogui
import time
import pyperclip
from tkinter import *
from functools import partial

def AbreThunderbird():
    time.sleep(3)
    pyautogui.press("winleft")
    pyautogui.write("Thunderbird")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(3)

def _workaround_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy('')

pyautogui.PAUSE = 0.5

time.sleep(5)

def enviar():
    AbreThunderbird()
    tabela = pd.read_excel(caixatexto.get())
    for i, marcador in enumerate(tabela["marcador"]):
        cia = tabela.loc[i, "cia"]
        empresa = tabela.loc[i, "empresa"]
        data = tabela.loc[i, "data"]
        mes = tabela.loc[i, "mes"]
        email = tabela.loc[i, "email"]
        copia = tabela.loc[i, "copia"]

        time.sleep(5)
        pyautogui.hotkey("ctrlleft", "n")
        pyautogui.write(email)
        time.sleep(5)
        pyautogui.press("tab")
        time.sleep(5)
        if copia != "no":
            pyautogui.hotkey("ctrlleft", "shift", "c")
            pyautogui.write(copia)
            pyautogui.press("tab")
        time.sleep(3)
        pyautogui.press("tab")
        assunto_caractere = ("Título no assunto" + " " + "-" + " " + cia + " " + "-" + " " + empresa )
        _workaround_write(assunto_caractere)
        pyautogui.press("tab")
        text_with_special_chars = (
                    "Texto que vai no corpo do e-mail" )

        _workaround_write(text_with_special_chars)
        pyautogui.hotkey("ctrlleft", "enter")
        time.sleep(5)

janela = Tk()
janela.title("Robo")
janela.geometry("280x380")
janela.resizable(False, False)

caixatexto = Entry(janela)
caixatexto.pack(padx=10, pady=50)

divi = Button(janela, text="ENVIAR", pady=14, padx=14, bd=4, command= enviar)
divi.place(x=100, y=150)

janela.mainloop()