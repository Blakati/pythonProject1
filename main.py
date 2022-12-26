from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
#from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.window import WindowBase
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.uix.popup import Popup
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.properties import ObjectProperty
from kivy.metrics import MetricsBase
from kivy.config import Config
#from kivy.uix.anchorlayout import AnchorLayout

# Window.minimum_height = 600
# Window.minimum_width = 400
Window.size = (400, 600)
Window.minimum_width, Window.minimum_height = Window.size

# Config.set('graphis', 'width', 400)
# Config.set('graphis', 'height', 600)

class Pop2(Popup):
    s = open('popup2.txt', 'r')
    contents = StringProperty(s.read())
    s.close()

def exmple1(message):
    if message == "50":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple2(message):
    if message == "80":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple3(message):
    if message == "90":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple4(message):
    if message == "70":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple5(message):
    if message == "60":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple6(message):
    if message == "40":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple7(message):
    if message == "40":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple8(message):
    if message == "0":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple9(message):
    if message == "38":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple10(message):
    if message == "59":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple11(message):
    if message == "98":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple12(message):
    if message == "14":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple13(message):
    if message == "4":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

def exmple14(message):
    if message == "62":
        btn00=Button(text='Дальше')
        pop1=Popup(content=btn00,title ='Молодец! Все верно!',  size_hint = (0.6, 0.2))
        pop1.open()
        btn00.bind(on_press=pop1.dismiss)

    else:
        btn00=Button(text='Заново')
        pop=Popup(content=btn00, title = 'Неверно, попробуй еще раз.',  size_hint = (0.6, 0.2))
        pop.open()
        btn00.bind(on_press=pop.dismiss)

class Page0(Screen):
    pass

class Page1(Screen):
    pass

class Page2(Screen):
    pass

class Page3(Screen):

    s = open('label1.txt', 'r')

    contents = StringProperty(s.read())
    s.close()


class Page4(Screen):
    pass

class Page5(Screen):
    # s = open('xc.txt', 'r')
    #
    # contents = StringProperty(s.read())
    # s.close()

    def __init__(self, **kwargs):

        super(Page5, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True )
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple1(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page6(Screen):
    def __init__(self, **kwargs):

        super(Page6, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple2(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page7(Screen):
    def __init__(self, **kwargs):

        super(Page7, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple3(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page8(Screen):
    def __init__(self, **kwargs):

        super(Page8, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple4(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page9(Screen):
    def __init__(self, **kwargs):

        super(Page9, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple5(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page10(Screen):
    def __init__(self, **kwargs):

        super(Page10, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple6(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page11(Screen):
    def __init__(self, **kwargs):

        super(Page11, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple7(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page12(Screen):
    def __init__(self, **kwargs):

        super(Page12, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple8(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page13(Screen):
    def __init__(self, **kwargs):

        super(Page13, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple9(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page14(Screen):
    def __init__(self, **kwargs):

        super(Page14, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple10(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page15(Screen):
    def __init__(self, **kwargs):

        super(Page15, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple11(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page16(Screen):
    def __init__(self, **kwargs):

        super(Page16, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple12(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page17(Screen):
    def __init__(self, **kwargs):

        super(Page17, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple13(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page18(Screen):
    def __init__(self, **kwargs):

        super(Page18, self).__init__(**kwargs)

        self.solution = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.5, "center_y": 0.53}, focus = True)
        btn = Button(text="проверить", size_hint=(0.1, 0.1))
        btn.bind(on_press=lambda *a: exmple14(self.solution.text))

        btn1 = Button(text='1', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.4})
        btn1.bind(on_press=self.on_button_press)

        btn2 = Button(text='2', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.4})
        btn2.bind(on_press=self.on_button_press)

        btn3 = Button(text='3', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
        btn3.bind(on_press=self.on_button_press)

        btn4 = Button(text='4', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.4})
        btn4.bind(on_press=self.on_button_press)

        btn5 = Button(text='5', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.4})
        btn5.bind(on_press=self.on_button_press)

        btn6 = Button(text='6', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.3, "center_y": 0.3})
        btn6.bind(on_press=self.on_button_press)

        btn7 = Button(text='7', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.4, "center_y": 0.3})
        btn7.bind(on_press=self.on_button_press)

        btn8 = Button(text='8', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.3})
        btn8.bind(on_press=self.on_button_press)

        btn9 = Button(text='9', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.6, "center_y": 0.3})
        btn9.bind(on_press=self.on_button_press)

        btn0 = Button(text='0', size_hint=(0.1, 0.1), pos_hint={"center_x": 0.7, "center_y": 0.3})
        btn0.bind(on_press=self.on_button_press)

        btn11 = Button(text="C", size_hint=(0.1, 0.1), pos_hint={"center_x": 0.8, "center_y": 0.3})
        btn11.bind(on_press=self.on_button_press)

        self.add_widget(btn)
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)
        self.add_widget(btn4)
        self.add_widget(btn5)
        self.add_widget(btn6)
        self.add_widget(btn7)
        self.add_widget(btn8)
        self.add_widget(btn9)
        self.add_widget(btn0)
        self.add_widget(btn11)
        self.add_widget(self.solution)

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":

            self.solution.text = ""
        else:
            new_text = current + button_text
            self.solution.text = new_text

class Page19(Screen):
    s = open('zadaca1.txt', 'r')
    contents = StringProperty(s.read())
    s.close()

    def __init__(self, **kwargs):

        super(Page19, self).__init__(**kwargs)

        self.txt = TextInput(multiline=False, font_size=50, size_hint=(0.4, 0.1),
                                  pos_hint={"center_x": 0.4, "center_y": 0.4}, focus = True)
        self.btn = Button(text='Ответ', size_hint=(.2, .05), pos_hint={"center_x": 0.1, "center_y": 0.5}, on_press=self.show_bubble)

        #btn = Button(text="проверить", size_hint=(0.1, 0.1))
        #btn.bind(on_press=lambda *a: exmple14(self.solution.text))

        self.add_widget(self.txt)
        self.add_widget(self.btn)

    def show_bubble(self, obj):
        bubble = Bubble(orientation='horizontal', size_hint=(None, None), size=(160, 120),
                            pos_hint={'center_x': .5, 'center_y': .5}, arrow_pos='top_mid')
        btn1 = BubbleButton(text='1', on_press=self.on_button_press)
        btn2 = BubbleButton(text='2', on_press=self.on_button_press)
        btn3 = BubbleButton(text='3', on_press=self.on_button_press)
        btnc = BubbleButton(text='C', on_press=self.on_button_press)

        bubble.add_widget(btn1)
        bubble.add_widget(btn2)
        bubble.add_widget(btn3)
        bubble.add_widget(btnc)

        self.add_widget(bubble)

    def on_button_press(self, instance):
        current = self.txt.text
        bubblebutton_text = instance.text

        if bubblebutton_text == "C":

            self.txt.text = ""
        else:
            new_text = current + bubblebutton_text
            self.txt.text = new_text

class MyApp(MDApp):
    def build(self):
        # Builder.load_file('kv3.py')
        # Window.clearcolor = (233/255, 233/255, 228/255, 1)
        #
        #
        #
        # sm = ScreenManager()
        # sm.add_widget(LoginWindow(name="LoginWindow"))
        # sm.add_widget(PageOne(name="PageOne"))
        # sm.add_widget(PageTwo(name="PageTwo"))
        # sm.add_widget(PageTree(name="PageTree"))
        # sm.add_widget(PageFour(name="PageFour"))
        # sm.add_widget(PageFive(name="PageFive"))
        # sm.add_widget(PageSix(name="PageSix"))
        # return sm


    #     self.root = FloatLayout()
    #     btn87 = Button(text='hh', on_press=self.show_bubble, size_hint=(None, None), size=(160, 160))
    #     self.txt = TextInput(size_hint=(0.5, 0.5), cursor_blink=True, multiline=False,
    #                          pos_hint={'center_x': .5, 'center_y': .5}, focus=True)
    #     self.root.add_widget(btn87)
    #     self.root.add_widget(self.txt)
    #
    #     return self.root
    #
    # def show_bubble(self, obj):
    #     bubble = Bubble(orientation='horizontal', size_hint=(None, None), size=(160, 120),
    #                     pos_hint={'center_x': .5, 'center_y': .5}, arrow_pos='top_mid')
    #     btn1 = BubbleButton(text='1', on_press=self.on_button_press)
    #     button2 = BubbleButton(text='2', on_press=self.on_button_press)
    #     button3 = BubbleButton(text='3', on_press=self.on_button_press)
    #     buttonc = BubbleButton(text='C', on_press=self.on_button_press)
    #
    #     bubble.add_widget(btn1)
    #     bubble.add_widget(button2)
    #     bubble.add_widget(button3)
    #     bubble.add_widget(buttonc)
    #
    #     self.root.add_widget(bubble)
    #
    # def on_button_press(self, instance):
    #     current = self.txt.text
    #     bubblebutton_text = instance.text
    #
    #     if bubblebutton_text == "C":
    #
    #         self.txt.text = ""
    #     else:
    #         new_text = current + bubblebutton_text
    #         self.txt.text = new_text

        Builder.load_file('kv3.py')
        Window.clearcolor = (233 / 255, 233 / 255, 228 / 255, 1)

        sm = ScreenManager()
        sm.add_widget(Page0(name="Page0"))
        sm.add_widget(Page1(name="Page1"))
        sm.add_widget(Page2(name="Page2"))
        sm.add_widget(Page3(name="Page3"))
        sm.add_widget(Page4(name="Page4"))
        sm.add_widget(Page5(name="Page5"))
        sm.add_widget(Page6(name="Page6"))
        sm.add_widget(Page7(name="Page7"))
        sm.add_widget(Page8(name="Page8"))
        sm.add_widget(Page9(name="Page9"))
        sm.add_widget(Page10(name="Page10"))
        sm.add_widget(Page11(name="Page11"))
        sm.add_widget(Page12(name="Page12"))
        sm.add_widget(Page13(name="Page13"))
        sm.add_widget(Page14(name="Page14"))
        sm.add_widget(Page15(name="Page15"))
        sm.add_widget(Page16(name="Page16"))
        sm.add_widget(Page17(name="Page17"))
        sm.add_widget(Page18(name="Page18"))
        sm.add_widget(Page19(name="Page19"))
        return sm

        return Page19

MyApp().run()
