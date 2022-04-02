import PySimpleGUI as sg

menu_def = [['File', ['Open', 'Save', 'Exit']],
            ['Edit', ['Paste', ['Special', 'Normal'], 'Undo']],
            ['Help', 'About...']]

button_menu_def = ['File', ['&Open', ['1','2','3'], 'Save', 'Properties', 'Exit']]

layout = [
    [sg.Menu(menu_def,text_color='black', font="SYSTEM_DEFAULT", pad=(10,10))],
    [sg.ButtonMenu('Button Menu', [['nf', 'op','om','---','rf','cl'],['New File', 'Open','Open Module','---','Recent Files','Close']], key='-B_MENU-', tooltip="Button Menu", visible=True)],
    [sg.Multiline(size=(80,10),tooltip='Write your Text here')],
    [sg.Text('File Name'),sg.Input(),sg.OptionMenu(values=['.txt','.pdf','.gif', '.jpg','.mp4','.gif','.dat','.sql'],size=(4,8), default_value='.doc',key='-DATA_TYPE-')],
    [sg.Button('SAVE'),sg.Button('CANCEL')]
]

window =sg.Window('Menu Example',layout)

while True:
    event,values=window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
            break
    elif event=='Open':
            print('Clicked Open button')
    elif event=='SAVE':
        print(values['-DATA_TYPE-'])

    if values['-B_MENU-'] == "Recent Files":
        print("Selected Recent Files")


window.close()