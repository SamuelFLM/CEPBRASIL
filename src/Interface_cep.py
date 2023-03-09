import PySimpleGUI as sg
import re
import requests
def interface_cep(home):
    sg.theme_background_color("white")
    cabecalho = [sg.Image(filename="img\cep\Group 15 (4).png", background_color="white",pad=(0,(10,30)), enable_events=True, key="voltar")]
    cep = [
        [sg.Image(filename="img\cep\CEP Remetente.png", background_color="white", pad=(0,(0,20)), k="img_cep")],
        [sg.Input("", background_color="white", border_width=0, k="cep", font="Inter 14 bold",justification='c', s=(15,0), pad=(10,(0,0)))],
        [sg.HSep(color="#5C5C5C", pad=(30,(0,40)), k="barra_cep")]
    ]
    endereco = [
        [sg.Image(filename="img\cep\Endereço.png", background_color="white", pad=(0,(0,5)))],
        [sg.Input("",disabled=True, background_color="white", disabled_readonly_background_color="white",border_width=0, k="endereco", font="Inter 11 bold",justification='l', s=(15,0), pad=(10,(0,0)))],
        [sg.HSep(color="#5C5C5C", pad=(30,(0,20)), k="barra_cep")]]
    estado = [
        [sg.Image(filename="img\cep\Estado.png", background_color="white", pad=(0,(0,5)))],
        [sg.Input("",disabled=True, background_color="white", disabled_readonly_background_color="white",border_width=0, k="estado", font="Inter 11 bold",justification='c', s=(15,0), pad=(10,(0,0)))],
        [sg.HSep(color="#5C5C5C", pad=(30,(0,20)), k="barra_cep")]]
    
    distrito = [[sg.Image(filename="img\cep\Distrito.png", background_color="white", pad=(0,(0,5)))],
        [sg.Input("",disabled=True, background_color="white", disabled_readonly_background_color="white",border_width=0, k="distrito", font="Inter 11 bold",justification='c', s=(15,0), pad=(10,(0,0)))],
        [sg.HSep(color="#5C5C5C", pad=(30,(0,20)), k="barra_cep")]]
    
    cidade = [[sg.Image(filename="img\cep\Cidade.png", background_color="white", pad=(0,(0,5)))],
        [sg.Input("",disabled=True, background_color="white", disabled_readonly_background_color="white",border_width=0, k="cidade", font="Inter 11 bold",justification='c', s=(15,0), pad=(10,(0,0)))],
        [sg.HSep(color="#5C5C5C", pad=(30,(0,20)), k="barra_cep")]]
    
    ddd = [[sg.Image(filename="img\cep\DDD.png", background_color="white", pad=(0,(0,5)))],
        [sg.Input("",disabled=True, background_color="white", disabled_readonly_background_color="white",border_width=0, k="ddd", font="Inter 11 bold",justification='c', s=(15,0), pad=(10,(0,0)))],
        [sg.HSep(color="#5C5C5C", pad=(30,(0,20)), k="barra_cep")]]
    
    rodape = [[sg.Image(filename="img\cep\Group 4.png", background_color="white", pad=(0,(20,0)))],]
    
    layout = [cabecalho,cep,endereco, estado,distrito,cidade,ddd,rodape]
    window = sg.Window("CEP", layout=layout, size=(328,548), margins=(0,0),element_justification='c', grab_anywhere=True,titlebar_background_color="#FECA26", icon="img\logo-correios-2048-3.ico")
    
    while True:
        event , values = window.read(timeout=10)
        
        if event == sg.WIN_CLOSED:
            break
        if event == "voltar":
            window.close()
            home()
            break
        try:
            if bool(values["cep"]):
                cep = str(values["cep"])
                validacao = re.search(r'^[0-9]+$', cep)
                if validacao:
                    window["img_cep"].update(filename="img\cep\CEP Remetente.png")
                    if len(values["cep"]) == 8:
                        window["img_cep"].update(filename="img\cep\CEP Remetente.png")
                        req_cep = requests.get("https://cep.awesomeapi.com.br/json/$$CEP$$".replace("$$CEP$$", cep))
                        valores_cep = req_cep.json()
                        endereco = valores_cep["address"]
                        estado = valores_cep["state"]
                        distrito = valores_cep["district"]
                        cidade = valores_cep["city"]
                        ddd = valores_cep["ddd"]
                        window["endereco"].update(f"{endereco}")
                        window["estado"].update(f"{estado}")
                        window["distrito"].update(f"{distrito}")
                        window["cidade"].update(f"{cidade}")
                        window["ddd"].update(f"{ddd}")
                    else:
                        window["img_cep"].update(filename="img\cep\Erro.png")
                        window["endereco"].update("")
                        window["estado"].update("")
                        window["distrito"].update("")
                        window["cidade"].update("")
                        window["ddd"].update("")
                else:
                    window["img_cep"].update(filename="img\cep\Erro.png")
                    window["endereco"].update("")
                    window["estado"].update("")
                    window["distrito"].update("")
                    window["cidade"].update("")
                    window["ddd"].update("")
                    
            if bool(values["cep"]) == False:
                window["img_cep"].update(filename="img\cep\CEP Remetente.png")
                window["endereco"].update("")
                window["estado"].update("")
                window["distrito"].update("")
                window["cidade"].update("")
                window["ddd"].update("")
        except:
            pass
if __name__ == "__main__":
    interface_cep(home="")