import PySimpleGUI as sg
import webbrowser
from Interface_cep import *
def interface_home():
    sg.theme_background_color("#FECA26")
    cabecalho = [sg.Image(filename="img\home\Group 14.png", background_color="#FECA26",pad=(0,(0,45)))]
    consultar = [sg.Image(filename="img\home\Group 2.png", background_color="#FECA26", pad=(0,(0,0)), enable_events=True, k="consultar")]
    precisa_de_ajuda = [sg.Image(filename="img\home\Group 1.png", background_color="#FECA26", pad=(0,(0,0)), enable_events=True, k="ajudar")]
    
    layout = [cabecalho, consultar, precisa_de_ajuda]
    window = sg.Window("Home", layout=layout, size=(328,548), margins=(0,0), element_justification='c', titlebar_background_color="#FECA26", icon="img\logo-correios-2048-3.ico")
    
    while True:
        event , values = window.read(timeout=10)
        
        if event == sg.WIN_CLOSED:
            break
        if event == "consultar":
            window.close()
            interface_cep(home=interface_home)
            break
        if event == 'ajudar':
            webbrowser.open_new_tab("https://github.com/SamuelFLM/Cadastro_usuario_CEP")
if __name__ == "__main__":
    interface_home()