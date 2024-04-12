import PySimpleGUI as sg
import math

def create_window(theme="neongreen1"):
    sg.theme(theme)
    sg.set_options(font="franklin 35")
    layout = [
        [sg.Text(
            "...",
            font="franklin 30",
            justification = "right",
            expand_x = True,
            right_click_menu=theme_menu,
            key="-TEXT-")
        ],
        [sg.Button("AC", size = (4, 1)), sg.Button("=", size = (3, 1)), sg.Button("√", expand_x = True)],
        [sg.Button(7), sg.Button(8), sg.Button(9), sg.Button("*", expand_x = True)],
        [sg.Button(4), sg.Button(5), sg.Button(6), sg.Button("/", expand_x = True)],
        [sg.Button(1), sg.Button(2), sg.Button(3), sg.Button("-", expand_x = True)],
        [sg.Button(0), sg.Button(".", size = (2, 1)), sg.Button("+"), sg.Button("x²")],
    ]

    return sg.Window("Calculator", layout)

original = "neongreen1"
theme_menu = ["menu", ["Random", "Purple", "DarkBrown4", "Darkpurple2", original]]
window = create_window()

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)
    
    if event == "x²":
        if current_num:
            num = float("".join(current_num))
            squared_num = num ** 2
            window["-TEXT-"].update(squared_num)
            current_num = [str(squared_num)]

    if event == "√":
        if current_num:
            num = float("".join(current_num))
            sqrt_num = math.sqrt(num)
            window["-TEXT-"].update(sqrt_num)
            current_num = [str(sqrt_num)]
    
    if event in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        current_num.append(event)
        num_string = "".join(current_num)
        window["-TEXT-"].update(num_string)

    if event in ["+", "-", "/", "*"]:
        full_operation.append("".join(current_num))
        current_num = []
        full_operation.append(event)
        window["-TEXT-"].update("")

    if event == "=":
        full_operation.append("".join(current_num))
        result = eval(" ".join(full_operation))
        window["-TEXT-"].update(result)
        full_operation = []

    if event == "AC":
        current_num = []
        full_operation = []
        window["-TEXT-"].update("")

window.close()