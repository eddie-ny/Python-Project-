import io
import qrcode
import PySimpleGUI as sg


class MainWindow(sg.Window):
    def __init__(self) -> None:
        sg.theme('Topanga')
        self.layout = [
            [sg.Input()],     
            [sg.Button('Create')],  
            [sg.Column([[sg.Image(key='QR')]], size=(300, 300), justification='center')],  
            [sg.Text('Fill Color: '), sg.Combo(['Black', 'White', 'Red', 'Green', 'Blue'], key='Fill', default_value='Black')],  
            [sg.Text('Background Color: '),sg.Combo(['White', 'Black', 'Red', 'Green', 'Blue'], key='Back', default_value='White')], 
            [sg.Text('Border Size: '), sg.Combo(['1', '2', '3', '4', '5', '6'], key='Border', default_value='4')],  
            [sg.Text('Box Size: '), sg.Combo(['5', '6', '7', '8', '9','10'], key='Box', default_value='6')], 

        ]
     
        super().__init__('QR Code Generator', self.layout)

    def genCode(self, data, fill_color, back_color, border_size, box_size):
        "Generates the QR code with the specified parameters"
        qr = qrcode.QRCode(version=1, box_size=int(box_size), border=int(border_size))
        qr.add_data(data)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color=fill_color, back_color=back_color)

        
        self.img = self.img.resize((300, 300))
        self.img = self.img.convert('RGB')

       
        self.showCode()

    def showCode(self):
        
        with io.BytesIO() as buffer:
       
            self.img.save(buffer, format='PNG')
            img_bytes = buffer.getvalue()
            self['QR'].update(data=img_bytes)

    def removeCode(self):
      
        self['QR'].update(data=b'')


if __name__ == '__main__':
    
    window = MainWindow()
    while True:
       
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
         
            window.close()
            
            break
        elif values[0]:
           
            window.genCode(values[0], values['Fill'], values['Back'], values['Border'], values['Box'])
        else: 
            
            popup("Error", "Textfield cannot be left empty") 
            window.removeCode()
