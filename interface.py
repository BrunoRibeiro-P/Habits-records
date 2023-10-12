import PySimpleGUI as sg

# Defina o layout da interface

layout = [
    [sg.Text('Hábito: X'), sg.InputText(3, size=(5, 1),key='habito_1_day'), sg.Button('Ok1')],
    [sg.Text('Maior record:',key='record_1_day'), sg.Text('10')],
    [sg.Button('Zerar')]]

# Crie a janela
janela = sg.Window('Exemplo de Interface', layout)

# Loop para interagir com a interface
while True:
    evento, valores = janela.read()

    if evento in (sg.WIN_CLOSED, 'Cancelar'):
        break
    if evento == 'Ok1':
        pass
    if evento == 'Zerar':
        janela['habito_1_day'].update('0')
        sg.popup(f'recontagem do hábito com sucesso.')

# Feche a janela
janela.close()
