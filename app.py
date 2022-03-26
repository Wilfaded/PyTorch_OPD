import eel

import main

eel.init("web")

@eel.expose
def recv_data(calculation):
    calculation = main.pp(calculation)
    return calculation


@eel.expose
def func(a='1'):
    a = main.answer
    return a


eel.start("GUI.html", size=(386, 576))
