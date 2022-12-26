#:import Factory kivy.factory.Factory

<Pop1@Popup>:
    auto_dismiss: False
    size_hint: 0.6, 0.2
    pos_hint:{"x": 0.2, "top":0.5}
    title:'Образец выполнения:'
    BoxLayout:
        orientation: 'vertical'
        size: root. width, root.height
        Label:
            text: 'теория'
            font_size: 24
            canvas.before:
                Rectangle:
                    source: 'popup1.png'
        Button:
            text: 'Понятно'
            font_size: 24
            on_release: root.dismiss()

<Pop2@Popup>:
    auto_dismiss: False
    size_hint: 0.8, 0.8
    pos_hint:{"x": 0.1, "top":1}
    title:'Образец выполнения:'
    BoxLayout:
        orientation: 'vertical'
        size: root. width, root.height
        Label:
            text: root.contents
            #text: 'Если в задаче сказано НА сколько-то БОЛЬШЕ,\n то в краткой записи мы ставим знак больше (>),\n а в решении используем знак сложения (+).\n Если в задаче сказано НА сколько-то МЕНЬШЕ,\n то в краткой записи мы ставим знак меньше (<),\n а в решении используем знак вычитания (-).'
            font_size: self.width/23
        Button:
            text: 'Понятно'
            size_hint: 0.6, 0.2
            font_size: 24
            on_release: root.dismiss()




<Page0>:
    BoxLayout:
        #cols: 1
        #size_hint:(0.90, 0.90)
        #pos_hint: {"center_x": 0.5, "center_y": 0.55}
        padding: 150
        #spacing: 10
        orientation: 'vertical'
        size: root. width, root.height


        Label:
            text:"Учебное пособие\n  по математике."
            font_size: int(40)
            color:(0, 0, 0, 1)


        MDRaisedButton:
            text: "Начать"
            line_color:"black"
            md_bg_color: 191/255, 194/255, 202/255, 1
            text_color:(0, 0, 0, 1)
            #background_normal: ''
            #background_color: 191/255, 194/255, 202/255, 1
            font_size: int(50)
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            #padding: 10
            #pos:(0.5, 0.5)
            #os_hint: None, None
            #spasing: 50
            #size: cm(10), cm(10)
            #size_hint: 0.5, None
            on_press:
                root.manager.current = "Page1"
<Page1>:
    GridLayout:
        cols: 1
        #orientation: 'vertical'
        size: root. width, root.height
        #size_hint:(0.90, 0.90)
        #pos_hint: {"center_x": 0.6, "center_y": 0.45}
        padding: 50
        spacing: 10

        Label:
            text: "Выберите тему\n для изучения."
            font_size: int(35)
            color:(0, 0, 0, 1)

        Button:
            text: "Сложение,\nвычитание"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(1), cm(2)
            size_hint: 0.7, None
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            on_press:
                root.manager.current = "Page2"
        Button:
            text: "Умножение,\n    деление "
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(1), cm(2)
            size_hint: 0.7, None
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            on_press:
                root.manager.current = "Page0"
        Button:
            text: "Время"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(1), cm(2)
            size_hint: 0.7, None
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            on_press:
                root.manager.current = "Page0"
        Button:
            text: "Величины"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(1), cm(2)
            size_hint: 0.7, None
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            on_press:
                root.manager.current = "Page0"
        Button:
            text: "Фигуры"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(1), cm(2)
            size_hint: 0.7, None
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            on_press:
                root.manager.current = "Page0"

<Page2>:
    GridLayout:
        cols: 1
        size_hint:(0.90, 0.90)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        padding: 50
        spacing: 10

        Button:
            text: "Сложение и вычитание без\n     перехода через разряд"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: self.width/14
            #text_size: (200, None)
            # size: cm(3), cm(3)
            # size_hint: 0.5, None
            on_press:
                root.manager.current = "Page3"

        Button:
            text: "Сложение с переходом\n          через разряд"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: self.width/14
            #font_size: int(30)
            # size: cm(3), cm(3)
            # size_hint: 0.5, None
            on_press:
                root.manager.current = "Page0"

        Button:
            text: "Вычитание с переходом\n          через разряд"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: self.width/14
            #font_size: int(30)
            # size: cm(3), cm(3)
            # size_hint: 0.5, None
            on_press:
                root.manager.current = "Page0"

<Page3>:
    BoxLayout:
        #cols: 1
        orientation: 'vertical'
        #size_hint:(0.90, 0.90)
        size: root. width, root.height
        #pos_hint: {"center_x": 0.5, "center_y": 0.5}
        padding: 50
        spacing: 10

        Label:
            text: root.contents
            #text: "Тема: Сложение и вычитание без\n     перехода через разряд"
            #pos_hint: {'x':0, "top": 1}
            font_size: self.width/18
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.01, "y": 0.13}

        # Label:
        #     text: "Чтобы сложить два числа без\n перехода через разряд надо сначала\n сложить единицы, а потом десятки.\n Например,"
        #     #text_size: window.width -
        #     #font_size: int(30)
        #    #size_hint: 0.5, 0.5
        #     font_size: self.width/16
        #     color:(0, 0, 0, 1)
        #     pos_hint: {'x': 0.028, 'y': 0.1}
            #canvas.before:
        Image:
            #Rectangle:
            source: 'popup1.png'
            size: self.texture_size
            #texture: False

        Button:
            text: "Практическая часть"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            #size: cm(3), cm(3)
            #size_hint: 0.8, 0.2
            #pos_hint: {'x': 0.1, 'y': 0.1}
            on_press:
                root.manager.current = "Page4"
<Page4>:
    GridLayout:
        cols: 1
        size_hint:(0.90, 0.90)
        pos_hint: {"center_x": 0.5, "center_y": 0.55}
        padding: 50
        spacing: 10
        Label:
            text: "Тип заданий."
            font_size: int(35)
            color:(0, 0, 0, 1)
        Button:
            text: "примеры"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(3), cm(3)
            size_hint: 0.5, None
            on_press:
                root.manager.current = "Page5"
        Button:
            text: "задачи"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            size: cm(3), cm(3)
            size_hint: 0.5, None
            on_press:
                root.manager.current = "Page19"

<Page5>:
    FloatLayout:
        size: root.width, root.height
        #cols: 1
        #size_hint:(0.90, 0.90)
        #pos_hint: {"center_x": 0.5, "center_y": 0.55}
        #padding: 40
        #spacing: 0
        # canvas.before:
        #     Rectangle:
        #         source: 'ty.png'

        Label:
            #text: root.contents
            text: '30 + 20 ='
            font_size: int(40)
            color:(0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}
            # pos_hint: None, None
        # TextInput:
        #     id: txt1
        #     multiline: False
        #     #padding_y: (1,1)
        #     size_hint: (0.2, 0.4)
        #     font_size: int(35)
        #     pos: 0.5, 0.5
        #     pos_hint: None, None
        # Button:
        #     text: '1'
        #     size: cm(1), cm(1)
        #     size_hint: 0.5, None
        #     #pos: 0.2, 0.3
        #     pos_hint: {"center_x": 0.2, "center_y": 0.3}
            #on_press:
                #root.button_press(1)

        # Button:
        #     id: clear
        #     text: 'C'
        #     size: cm(1), cm(1)
        #     size_hint: 0.5, None
        #     #pos: 0.2, 0.3
        #     pos_hint: {"center_x": 0.2, "center_y": 0.3}
        #     on_press: root.clear()

        MDFloatingActionButton:
            icon:"send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующий пример"
            color:(0, 0, 0, 1)
            background_normal: ''
            background_color: 191/255, 194/255, 202/255, 1
            font_size: int(30)
            #size: cm(3), cm(3)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page6"

        # Button:
        #
        #     text: "отправить"
        #     color:(0, 0, 0, 1)
        #     background_normal: ''
        #     background_color: 191/255, 194/255, 202/255, 1
        #     font_size: int(30)
        #     size: cm(5), cm(3)
        #     size_hint: None, None
        #     pos: 0.9, 0.2
        #     pos_hint: None, None

<Page6>:
    FloatLayout:

        size: root.width, root.height

        Label:
            # text: root.contents
            text: '70+10='
            font_size: int(40)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page7"

<Page7>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '60+30='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page8"

<Page8>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '30+40='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page9"

<Page9>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '90-30='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page10"

<Page10>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '50-10='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page11"

<Page11>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '70-30='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page12"

<Page12>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '50-50='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page13"

<Page13>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '27+11='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page14"

<Page14>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '34+25='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page15"

<Page15>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '61+37='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page16"

<Page16>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '77-63='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page17"

<Page17>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '48-44='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page18"

<Page18>:
    FloatLayout:
        size: root.width, root.height

        Label:
            # text: root.contents
            text: '86-24='
            font_size: int(35)
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop1().open()

        Button:
            text: "Следующему примеру"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page4"

<Page19>:
    FloatLayout:
        size: root.width, root.height

        Label:
            text: root.contents
            #text: 'У одной из хозяек вылупилось 26 цыплят, а у второй вылупилось на 3 цыплёнка больше.\n Сколько цыплят вылупилось у второй хозяйки?'
            #font_size: int(20)
            #font_size: Window.width - dp(15), None
            font_size: self.width/25
            color: (0, 0, 0, 1)
            pos_hint: {"x": 0.005, "y": 0.13}

        MDFloatingActionButton:
            icon: "send"
            md_bg_color: "red"
            pos_hint: {"x": .9, "top": 1}
            on_release: Factory.Pop2().open()

        Button:
            text: "Следующей задачи"
            color: (0, 0, 0, 1)
            background_normal: ''
            background_color: 191 / 255, 194 / 255, 202 / 255, 1
            font_size: int(30)
            size_hint: 0.5, 0.2
            pos_hint: {"x": 0.5, "bottom": 0.8}
            on_press:
                root.manager.current = "Page4"
