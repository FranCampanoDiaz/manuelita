from firebase import firebase
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
import datetime
from kivy.uix.boxlayout import BoxLayout

#iniciar base de datos

'''firebase = firebase.FirebaseApplication('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/',None)

data = {
    'Email': 'ejemplo@ejemplo.com',
    'Password': '12345'
}

#Post   para mandar datos a la base de datos
#firebase.post('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/Users', data)

#Get
result = firebase.get('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/Users', '')

for i in result.keys():
    print(result[i]['Email'])'''





'''from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (500,700)

class manuelita(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return
    def send_data(self, email, password):
        from firebase import firebase

        # inicializar firebase
        firebase = firebase.FirebaseApplication('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/', None)

        # importar data
        data = {
            'Email': email,
            'Password': password
        }
        # postear data
        # nombre db/nombre tabla
        firebase.post('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/Users', data)


manuelita().run()'''


from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (500, 700)

class SignUpScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class CalculatorScreen(Screen):
    pass

class login(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        self.sm = ScreenManager()

        self.sm.add_widget(LoginScreen(name='Login'))
        self.sm.add_widget(SignUpScreen(name='SignUpScreen'))
        self.sm.add_widget(CalculatorScreen(name='Calculator'))

        return self.sm


    def send_data(self, email, password):
        from firebase import firebase
        # inicializar firebase
        firebase = firebase.FirebaseApplication('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/', None)
        # importar data
        data = {
            'Email': email,
            'Password': password
        }
        # postear data
        # nombre db/nombre tabla
        firebase.post('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/Users', data)

    def get_data(self, email, password):

        from firebase import firebase
        # inicializar firebase
        firebase = firebase.FirebaseApplication('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/', None)

        # Get data
        result = firebase.get('https://pythondb-d60ae-default-rtdb.europe-west1.firebasedatabase.app/Users', '')
        # print(result)

        # verificar email y contraseña
        for i in result.keys():
            if result[i]['Email'] == email:
                if result[i]['Password'] == password:
                    self.sm.get_screen('Calculator')
                    self.sm.current = 'Calculator'
                else:
                    print("Wrong data")

    def clear(self):
        self.sm.get_screen('Calculator').ids['cal_input'].text = '0'

    def button_press(self, button):
        prior = self.sm.get_screen('Calculator').ids['cal_input'].text

        if "ERROR" in prior:
            prior = ""

        if prior == "0":
            self.sm.get_screen('Calculator').ids['cal_input'].text = ''
            self.sm.get_screen('Calculator').ids['cal_input'].text = f'{button}'
        else:
            self.sm.get_screen('Calculator').ids['cal_input'].text = f'{prior}{button}'

    def dot(self):
        prior = self.sm.get_screen('Calculator').ids['cal_input'].text
        if "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.sm.get_screen('Calculator').ids['cal_input'].text = prior

    def remove(self):
        prior = self.sm.get_screen('Calculator').ids['cal_input'].text
        prior = prior[:-1]
        self.sm.get_screen('Calculator').ids['cal_input'].text = prior

    def pos_neg(self):
        prior = self.sm.get_screen('Calculator').ids['cal_input'].text
        if "-" in prior:
            self.sm.get_screen('Calculator').ids['cal_input'].text = f'{prior.replace("-","")}'
        else:
            self.sm.get_screen('Calculator').ids['cal_input'].text = f'-{prior}'

    def math_sign(self, sign):
        prior = self.sm.get_screen('Calculator').ids['cal_input'].text
        self.sm.get_screen('Calculator').ids['cal_input'].text = f'{prior}{sign}'

    def equals(self):
        prior = self.sm.get_screen('Calculator').ids['cal_input'].text
        #ERROR
        try:
            answer = eval(prior)
            self.sm.get_screen('Calculator').ids['cal_input'].text = str(answer)
        except:
            self.sm.get_screen('Calculator').ids['cal_input'].text = "ERROR"


if __name__ == '__main__':
    login().run()



    '''canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            source:'img.png'
            size: root.width, root.height
            pos: self.pos
            para poner foto'''