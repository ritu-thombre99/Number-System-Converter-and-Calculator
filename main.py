from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard
from functools import partial


from helper import *
from base10ops import *
from base2ops import *
from base8ops import *
from base16ops import *

history = []
# red (1,0,0,1))
class MainApp(App):
    def build(self):
        self.ids = {}
        self.main_layout = BoxLayout(orientation="vertical")
        self.operators = ["+","-","/","*"]
        self.numbers = []
        for i in range(10):
            self.numbers.append(str(i))
        self.numbers.append("A")
        self.numbers.append("B")
        self.numbers.append("C")
        self.numbers.append("D")
        self.numbers.append("E")
        self.numbers.append("F")
        
        self.was_last_equal = False

        # selection
        self.input_type = BoxLayout(orientation="vertical",size_hint=(1.,0.6))

        # binary
        h_layout = BoxLayout(orientation="horizontal")
        button1 = Button(text='Bin',size_hint=(1.0, 1.0))
        button1.bind(on_press=self.on_selection)
        self.ids['Bin'] = button1
        h_layout.add_widget(button1)

        self.binary = TextInput(
            multiline=True,hint_text="Binary Output", readonly=True, halign="right", font_size="15sp",size_hint=(5.0, 1.0), use_bubble = False
        )
        h_layout.add_widget(self.binary)
        self.input_type.add_widget(h_layout)

        # octal
        h_layout = BoxLayout(orientation="horizontal")
        button1 = Button(text='Oct', size_hint=(1.0, 1.0))
        button1.bind(on_press=self.on_selection)
        self.ids['Oct'] = button1
        h_layout.add_widget(button1)

        self.octal = TextInput(
            multiline=True,hint_text="Octal Output", readonly=True, halign="right", font_size="15sp",size_hint=(5.0, 1.0), use_bubble = False
        )
        h_layout.add_widget(self.octal)
        self.input_type.add_widget(h_layout)

        # decimal
        h_layout = BoxLayout(orientation="horizontal")
        button1 = Button(text='Dec', size_hint=(1.0, 1.0))
        button1.bind(on_press=self.on_selection)
        self.ids['Dec'] = button1
        h_layout.add_widget(button1)

        self.decimal = TextInput(
            multiline=True,hint_text="Decimal Output", readonly=True, halign="right", font_size="15sp",size_hint=(5.0, 1.0), use_bubble = False
        )
        h_layout.add_widget(self.decimal)
        self.input_type.add_widget(h_layout)

        # hexadecimal
        h_layout = BoxLayout(orientation="horizontal")
        button1 = Button(text='Hex', size_hint=(1.0, 1.0))
        button1.bind(on_press=self.on_selection)
        self.ids['Hex'] = button1
        h_layout.add_widget(button1)

        self.hex = TextInput(
            multiline=True,hint_text="Hexadecimal Output", readonly=True, halign="right", font_size="15sp",size_hint=(5.0, 1.0), use_bubble = False
        )
        h_layout.add_widget(self.hex)
        self.input_type.add_widget(h_layout)


        self.main_layout.add_widget(self.input_type)

        # input layouts
        self.binary_layout = None
        self.octal_layout = None
        self.decimal_layout = None
        self.hex_layout = None        


        return self.main_layout


    def on_button_press(self, instance):
        return
    

    def on_selection(self, instance):
        if instance.background_color == [1,1,1,1]:
            self.ids["Bin"].background_color = (1,1,1,1)
            self.ids["Dec"].background_color = (1,1,1,1)
            self.ids["Oct"].background_color = (1,1,1,1)
            self.ids["Hex"].background_color = (1,1,1,1)

            if self.binary_layout:
                self.main_layout.remove_widget(self.binary_layout)
            if self.octal_layout:
                self.main_layout.remove_widget(self.octal_layout)
            if self.decimal_layout:
                self.main_layout.remove_widget(self.decimal_layout)
            if self.hex_layout:
                self.main_layout.remove_widget(self.hex_layout)

            instance.background_color = (0,1,0,1)
            self.binary.text = ""
            self.octal.text = ""
            self.decimal.text = ""
            self.hex.text = ""
            self.was_last_equal = False

            button_text = instance.text

            if button_text == "Bin":
                self.binary_operations()
            if button_text == "Oct":
                self.octal_operations()
            if button_text == "Dec":
                self.decimal_operations()
            if button_text == "Hex":
                self.hex_operations()
        
        
    def binary_operations(self):
        buttons = [["0","1"],
                   ["+","-"],
                   ["*","/"],
                   [".","="],
                   ["DEL","AC"]]
        self.binary_layout = BoxLayout(orientation="vertical")
        for row in buttons:
            h_layout = BoxLayout(orientation="horizontal")
            for label in row:
                button = Button(text=label,font_size="30sp")
                button.bind(on_press=self.on_binary_buttons)
                h_layout.add_widget(button)
            self.binary_layout.add_widget(h_layout)

        # history button
        h_layout = BoxLayout(orientation="horizontal")

        hist_button = Button(text="HISTORY",font_size="30sp",)
        hist_button.bind(on_press=self.on_history)

        copy_button = Button(text="COPY",font_size="30sp",)
        copy_button.bind(on_press=self.on_binary_buttons)

        h_layout.add_widget(hist_button)
        h_layout.add_widget(copy_button)
        self.binary_layout.add_widget(h_layout)
        #self.binary_layout.add_widget(hist_button)

        self.main_layout.add_widget(self.binary_layout)

    def octal_operations(self):
        buttons = [["0","1","2","+"],
                   ["3","4","5","-"],
                   ["6","7","*","/"],
                   [".","=","DEL","AC"]]
        self.octal_layout = BoxLayout(orientation="vertical")
        for row in buttons:
            h_layout = BoxLayout(orientation="horizontal")
            for label in row:
                button = Button(text=label,font_size="30sp",)
                button.bind(on_press=self.on_octal_buttons)
                h_layout.add_widget(button)
            self.octal_layout.add_widget(h_layout)
        # history button
        h_layout = BoxLayout(orientation="horizontal")

        hist_button = Button(text="HISTORY",font_size="30sp",)
        hist_button.bind(on_press=self.on_history)

        copy_button = Button(text="COPY",font_size="30sp",)
        copy_button.bind(on_press=self.on_octal_buttons)

        h_layout.add_widget(hist_button)
        h_layout.add_widget(copy_button)
        self.octal_layout.add_widget(h_layout)
        #self.octal_layout.add_widget(hist_button)

        self.main_layout.add_widget(self.octal_layout)

    def decimal_operations(self):
        buttons = [["1","2","3","+"],
                   ["4","5","6","-"],
                   ["7","8","9","*"],
                   [".","0","=","/"],
                   ["DEL","AC"]]
        self.decimal_layout = BoxLayout(orientation="vertical")
        for row in buttons:
            h_layout = BoxLayout(orientation="horizontal")
            for label in row:
                button = Button(text=label,font_size="30sp",)
                button.bind(on_press=self.on_decimal_buttons)
                h_layout.add_widget(button)
            self.decimal_layout.add_widget(h_layout)

        # history button
        h_layout = BoxLayout(orientation="horizontal")

        hist_button = Button(text="HISTORY",font_size="30sp",)
        hist_button.bind(on_press=self.on_history)

        copy_button = Button(text="COPY",font_size="30sp",)
        copy_button.bind(on_press=self.on_decimal_buttons)

        h_layout.add_widget(hist_button)
        h_layout.add_widget(copy_button)
        self.decimal_layout.add_widget(h_layout)
        #self.decimal_layout.add_widget(hist_button)

        self.main_layout.add_widget(self.decimal_layout)
    
    def hex_operations(self):
        buttons = [["0","1","2","+"],
                   ["3","4","5","-"],
                   ["6","7","8","*"],
                   ["9","A","B","/"],
                   ["C","D","E","="],
                   [".","F","AC","DEL"]]
        self.hex_layout = BoxLayout(orientation="vertical")
        for row in buttons:
            h_layout = BoxLayout(orientation="horizontal")
            for label in row:
                button = Button(text=label,font_size="30sp",)
                button.bind(on_press=self.on_hex_buttons)
                h_layout.add_widget(button)
            self.hex_layout.add_widget(h_layout)
        
        # history button
        h_layout = BoxLayout(orientation="horizontal")

        hist_button = Button(text="HISTORY",font_size="30sp",)
        hist_button.bind(on_press=self.on_history)

        copy_button = Button(text="COPY",font_size="30sp",)
        copy_button.bind(on_press=self.on_hex_buttons)

        h_layout.add_widget(hist_button)
        h_layout.add_widget(copy_button)
        self.hex_layout.add_widget(h_layout)
        #self.hex_layout.add_widget(hist_button)

        self.main_layout.add_widget(self.hex_layout)

    def on_copy(self,instance, text_to_copy):
        if text_to_copy:
            Clipboard.copy(text_to_copy)
            popup = Popup(title='',separator_height=0,content=Label(text="Copied",font_size="20sp"),size_hint=(0.5, 0.1))
            popup.open()



    def on_history(self, instance):
        display_h = ''
        for h in history:
            display_h = display_h + h + "\n"

        box = BoxLayout(orientation = 'vertical',size_hint=(0.9,0.9))
        #box.add_widget(Label(text = "Copy history"))

        show_history = TextInput(
            multiline=True,hint_text=display_h, readonly=True, font_size="20sp", use_bubble = False, size_hint=(1.0,4.0)
        )
        box.add_widget(show_history)

        h_layout = BoxLayout(orientation = 'horizontal', size_hint=(1.0,1.0))
        copy_button = Button(text="Copy",font_size="20sp",size_hint=(0.5,0.4))
        copy_button.bind(on_press = partial(self.on_copy,  text_to_copy = display_h))


        h_layout.add_widget(copy_button)
        
        #popup = Popup(title='Test Exception',content=Label(text= display_h),size_hint=(None, None), size=(400, 400))
        popup = Popup(title='History',content=box,size_hint=(0.9,0.9))

        close_button = Button(text="Close", font_size="20sp", size_hint=(0.5,0.4))
        close_button.bind(on_press = popup.dismiss)
        h_layout.add_widget(close_button)
        box.add_widget(h_layout)
        popup.open()
        #Clipboard.copy(popup.content.text)

    def on_decimal_buttons(self, instance):
        button_text = instance.text

        if button_text == "COPY" and self.decimal.text:
            Clipboard.copy(self.decimal.text)
            popup = Popup(title='',separator_height=0,content=Label(text="Copied Decimal", pos_hint={'center_y': 0, 'center_y': .5}),size_hint=(0.6, 0.1))
            popup.open()

        if button_text == "AC":
            # Clear the solution widget
            self.decimal.text = ""
            self.binary.text = ""
            self.octal.text = ""
            self.hex.text = ""
            self.was_last_equal = False
        

        elif button_text == "DEL":
            if self.decimal.text:
                self.decimal.text = (self.decimal.text)[:-1]
                self.binary.text = parse_decimal_backspace(self.binary.text, self.decimal.text,2)
                self.octal.text = parse_decimal_backspace(self.octal.text, self.decimal.text,8)
                self.hex.text = parse_decimal_backspace(self.hex.text, self.decimal.text,16)
                self.was_last_equal = False
        
        elif button_text in self.numbers:
            if self.was_last_equal == True:
                self.decimal.text = button_text
                self.binary.text = decimal_conversions(button_text,2)
                self.octal.text = decimal_conversions(button_text,8)
                self.hex.text = decimal_conversions(button_text,16)
                self.was_last_equal = False
            else:
                if check_length(self.decimal.text, 10):
                    self.binary.text = parse_decimal_string(self.binary.text,self.decimal.text,button_text,2)
                    self.octal.text = parse_decimal_string(self.octal.text,self.decimal.text, button_text, 8)
                    self.hex.text = parse_decimal_string(self.hex.text,self.decimal.text, button_text, 16)
                    self.decimal.text = self.decimal.text + button_text
                else:
                    popup = Popup(title='',separator_height=0,content=Label(text="Cannot enter more than\n14 digit in Decimal mode"),size_hint=(None, None), size=(400, 400))
                    popup.open()

        elif button_text in self.operators:
            self.was_last_equal = False
            if self.decimal.text == "":
                return
            elif self.decimal.text[-1] in self.operators:
                self.decimal.text = self.decimal.text.replace(self.decimal.text[-1], button_text)
                self.binary.text = self.binary.text.replace(self.binary.text[-1], button_text)
                self.octal.text = self.octal.text.replace(self.octal.text[-1], button_text)
                self.hex.text = self.hex.text.replace(self.hex.text[-1], button_text)
            else:
                self.decimal.text = self.decimal.text + button_text
                self.binary.text = self.binary.text + button_text
                self.octal.text = self.octal.text + button_text
                self.hex.text = self.hex.text + button_text

        elif button_text == "=":
            if self.decimal.text == "":
                return
            if self.decimal.text[-1] in self.operators:
                return
            if self.was_last_equal:
                return
            if check_sanity(self.decimal.text) == False:
                self.decimal.text = ''
                self.binary.text = ''
                self.octal.text = ''
                self.hex.text = ''
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()
                return
            try:
                self.decimal.text = check_leading_zeros(self.decimal.text)
                answer = convert_scientific_notation(str(eval(self.decimal.text)))
                history.append("Base 10: "+self.decimal.text+"="+answer)
                self.decimal.text = answer
                self.binary.text = decimal_conversions(answer,2)
                self.octal.text = decimal_conversions(answer,8)
                self.hex.text = decimal_conversions(answer,16)
                self.was_last_equal = True
            except Exception as e:
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()

        elif button_text == ".":
            if not self.decimal.text:
                self.decimal.text = "0."
                self.binary.text = "0."
                self.octal.text = "0."
                self.hex.text = "0."
                self.was_last_equal = False
            else:
                if self.decimal.text[-1] in self.operators:
                    self.decimal.text = self.decimal.text + "0" + button_text
                    self.binary.text = self.binary.text + "0" + button_text
                    self.octal.text = self.octal.text + "0" + button_text
                    self.hex.text = self.hex.text + "0" + button_text
                    self.was_last_equal = False
                elif is_decimal_valid(self.decimal.text) and self.decimal.text[-1] in self.numbers:
                    self.decimal.text = self.decimal.text + button_text
                    self.binary.text = self.binary.text + button_text
                    self.octal.text = self.octal.text + button_text
                    self.hex.text = self.hex.text + button_text
                    self.was_last_equal = False


    def on_binary_buttons(self, instance):
        button_text = instance.text

        if button_text == "COPY" and self.binary.text:
            Clipboard.copy(self.binary.text)
            popup = Popup(title='',separator_height=0,content=Label(text="Copied Binary", pos_hint={'center_y': 0, 'center_y': .5}),size_hint=(0.6, 0.1))
            popup.open()
        if button_text == "AC":
            # Clear the solution widget
            self.decimal.text = ""
            self.binary.text = ""
            self.octal.text = ""
            self.hex.text = ""
            self.was_last_equal = False
        

        elif button_text == "DEL":
            if self.binary.text:
                self.binary.text = (self.binary.text)[:-1]
                self.decimal.text = parse_binary_backspace(self.decimal.text, self.binary.text,10)
                self.octal.text = parse_binary_backspace(self.octal.text, self.binary.text,8)
                self.hex.text = parse_binary_backspace(self.hex.text, self.binary.text,16)
                self.was_last_equal = False
        
        elif button_text in self.numbers:
            if self.was_last_equal == True:
                self.binary.text = button_text
                self.decimal.text = binary_conversions(button_text,10)
                self.octal.text = binary_conversions(button_text,8)
                self.hex.text = binary_conversions(button_text,16)
                self.was_last_equal = False
            else:
                if check_length(self.binary.text, 2):
                    self.decimal.text = parse_binary_string(self.decimal.text,self.binary.text,button_text,10)
                    self.octal.text = parse_binary_string(self.octal.text,self.binary.text, button_text, 8)
                    self.hex.text = parse_binary_string(self.hex.text,self.binary.text, button_text, 16)
                    self.binary.text = self.binary.text + button_text
                else:
                    popup = Popup(title='',separator_height=0,content=Label(text="Cannot enter more than\n52 digit in Binary mode"),size_hint=(None, None), size=(400, 400))
                    popup.open()

        elif button_text in self.operators:
            self.was_last_equal = False
            if self.binary.text == "":
                return
            elif self.binary.text[-1] in self.operators:
                self.decimal.text = self.decimal.text.replace(self.decimal.text[-1], button_text)
                self.binary.text = self.binary.text.replace(self.binary.text[-1], button_text)
                self.octal.text = self.octal.text.replace(self.octal.text[-1], button_text)
                self.hex.text = self.hex.text.replace(self.hex.text[-1], button_text)
            else:
                self.decimal.text = self.decimal.text + button_text
                self.binary.text = self.binary.text + button_text
                self.octal.text = self.octal.text + button_text
                self.hex.text = self.hex.text + button_text

        elif button_text == "=":
            if self.binary.text == "":
                return
            if self.binary.text[-1] in self.operators:
                return
            if self.was_last_equal:
                return 
            if check_sanity(self.decimal.text) == False:
                self.decimal.text = ''
                self.binary.text = ''
                self.octal.text = ''
                self.hex.text = ''
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()
                return
            try:
                self.decimal.text = check_leading_zeros(self.decimal.text)
                answer = convert_scientific_notation(str(eval(self.decimal.text)))
                history.append("Base 2: "+self.binary.text+"="+decimal_conversions(answer,2))
                self.decimal.text = answer
                self.binary.text = decimal_conversions(answer,2)
                self.octal.text = decimal_conversions(answer,8)
                self.hex.text = decimal_conversions(answer,16)
                self.was_last_equal = True
            except Exception as e:
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()

        elif button_text == ".":
            if not self.binary.text:
                self.decimal.text = "0."
                self.binary.text = "0."
                self.octal.text = "0."
                self.hex.text = "0."
                self.was_last_equal = False
            else:
                if self.binary.text[-1] in self.operators:
                    self.decimal.text = self.decimal.text + "0" + button_text
                    self.binary.text = self.binary.text + "0" + button_text
                    self.octal.text = self.octal.text + "0" + button_text
                    self.hex.text = self.hex.text + "0" + button_text
                    self.was_last_equal = False
                elif is_decimal_valid(self.binary.text) and self.binary.text[-1] in self.numbers:
                    self.decimal.text = self.decimal.text + button_text
                    self.binary.text = self.binary.text + button_text
                    self.octal.text = self.octal.text + button_text
                    self.hex.text = self.hex.text + button_text
                    self.was_last_equal = False

    def on_octal_buttons(self, instance):
        button_text = instance.text

        if button_text == "COPY" and self.octal.text:
            Clipboard.copy(self.octal.text)
            popup = Popup(title='',separator_height=0,content=Label(text="Copied Octal", pos_hint={'center_y': 0, 'center_y': .5}),size_hint=(0.6, 0.1))
            popup.open()

        if button_text == "AC":
            # Clear the solution widget
            self.decimal.text = ""
            self.binary.text = ""
            self.octal.text = ""
            self.hex.text = ""
            self.was_last_equal = False
        

        elif button_text == "DEL":
            if self.octal.text:  
                self.octal.text = (self.octal.text)[:-1]
                self.decimal.text = parse_octal_backspace(self.decimal.text, self.octal.text,10)
                self.binary.text = parse_octal_backspace(self.binary.text, self.octal.text,2)
                self.hex.text = parse_octal_backspace(self.hex.text, self.octal.text,16)
                self.was_last_equal = False
        
        elif button_text in self.numbers:
            if self.was_last_equal == True:
                self.octal.text = button_text
                self.decimal.text = octal_conversions(button_text,10)
                self.binary.text = octal_conversions(button_text,2)
                self.hex.text = octal_conversions(button_text,16)
                self.was_last_equal = False
            else:
                if check_length(self.octal.text, 8):
                    self.decimal.text = parse_octal_string(self.decimal.text,self.octal.text,button_text,10)
                    self.binary.text = parse_octal_string(self.binary.text,self.octal.text, button_text, 2)
                    self.hex.text = parse_octal_string(self.hex.text,self.octal.text, button_text, 16)
                    self.octal.text = self.octal.text + button_text
                else:
                    popup = Popup(title='',separator_height=0,content=Label(text="Cannot enter more than\n16 digit in Octal mode"),size_hint=(None, None), size=(400, 400))
                    popup.open()

        elif button_text in self.operators:
            self.was_last_equal = False
            if self.octal.text == "":
                return
            elif self.octal.text[-1] in self.operators:
                self.decimal.text = self.decimal.text.replace(self.decimal.text[-1], button_text)
                self.binary.text = self.binary.text.replace(self.binary.text[-1], button_text)
                self.octal.text = self.octal.text.replace(self.octal.text[-1], button_text)
                self.hex.text = self.hex.text.replace(self.hex.text[-1], button_text)
            else:
                self.decimal.text = self.decimal.text + button_text
                self.binary.text = self.binary.text + button_text
                self.octal.text = self.octal.text + button_text
                self.hex.text = self.hex.text + button_text

        elif button_text == "=":
            if self.octal.text == "":
                return
            if self.octal.text[-1] in self.operators:
                return
            if self.was_last_equal:
                return
            if check_sanity(self.decimal.text) == False:
                self.decimal.text = ''
                self.binary.text = ''
                self.octal.text = ''
                self.hex.text = ''
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()
                return
            try:
                self.decimal.text = check_leading_zeros(self.decimal.text)
                answer = convert_scientific_notation(str(eval(self.decimal.text)))
                history.append("Base 8: "+self.octal.text+"="+decimal_conversions(answer,8))
                self.decimal.text = answer
                self.binary.text = decimal_conversions(answer,2)
                self.octal.text = decimal_conversions(answer,8)
                self.hex.text = decimal_conversions(answer,16)
                self.was_last_equal = True
            except Exception as e:
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()

        elif button_text == ".":
            if not self.octal.text:
                self.decimal.text = "0."
                self.binary.text = "0."
                self.octal.text = "0."
                self.hex.text = "0."
                self.was_last_equal = False
            else:
                if self.octal.text[-1] in self.operators:
                    self.decimal.text = self.decimal.text + "0" + button_text
                    self.binary.text = self.binary.text + "0" + button_text
                    self.octal.text = self.octal.text + "0" + button_text
                    self.hex.text = self.hex.text + "0" + button_text
                    self.was_last_equal = False
                elif is_decimal_valid(self.octal.text) and self.octal.text[-1] in self.numbers:
                    self.decimal.text = self.decimal.text + button_text
                    self.binary.text = self.binary.text + button_text
                    self.octal.text = self.octal.text + button_text
                    self.hex.text = self.hex.text + button_text
                    self.was_last_equal = False
            
    def on_hex_buttons(self, instance):
        button_text = instance.text

        if button_text == "COPY" and self.hex.text:
            Clipboard.copy(self.hex.text)
            popup = Popup(title='',separator_height=0,content=Label(text="Copied Hexadecimal", pos_hint={'center_y': 0, 'center_y': .5}),size_hint=(0.6, 0.1))
            popup.open()


        if button_text == "AC":
            # Clear the solution widget
            self.decimal.text = ""
            self.binary.text = ""
            self.octal.text = ""
            self.hex.text = ""
            self.was_last_equal = False
        

        elif button_text == "DEL":
            if self.hex.text:  
                self.hex.text = (self.hex.text)[:-1]
                self.decimal.text = parse_hex_backspace(self.decimal.text, self.hex.text,10)
                self.binary.text = parse_hex_backspace(self.binary.text, self.hex.text,2)
                self.octal.text = parse_hex_backspace(self.octal.text, self.hex.text,8)
                self.was_last_equal = False
        
        elif button_text in self.numbers:
            if self.was_last_equal == True:
                self.hex.text = button_text
                self.decimal.text = hex_conversions(button_text,10)
                self.binary.text = hex_conversions(button_text,2)
                self.octal.text = hex_conversions(button_text,8)
                self.was_last_equal = False
            else:  
                if check_length(self.hex.text, 16):
                    self.decimal.text = parse_hex_string(self.decimal.text,self.hex.text,button_text,10)
                    self.binary.text = parse_hex_string(self.binary.text,self.hex.text, button_text, 2)
                    self.octal.text = parse_hex_string(self.octal.text,self.hex.text, button_text, 8)
                    self.hex.text = self.hex.text + button_text
                else:
                    popup = Popup(title='',separator_height=0,content=Label(text='Cannot enter more than\n13 digit in Hexadecimal mode'),size_hint=(None, None), size=(400, 400))
                    popup.open()

        elif button_text in self.operators:
            self.was_last_equal = False
            if self.hex.text == "":
                return
            elif self.hex.text[-1] in self.operators:
                self.decimal.text = self.decimal.text.replace(self.decimal.text[-1], button_text)
                self.binary.text = self.binary.text.replace(self.binary.text[-1], button_text)
                self.octal.text = self.octal.text.replace(self.octal.text[-1], button_text)
                self.hex.text = self.hex.text.replace(self.hex.text[-1], button_text)
            else:
                self.decimal.text = self.decimal.text + button_text
                self.binary.text = self.binary.text + button_text
                self.octal.text = self.octal.text + button_text
                self.hex.text = self.hex.text + button_text

        elif button_text == "=":
            if self.hex.text == "":
                return
            if self.hex.text[-1] in self.operators:
                return
            if self.was_last_equal:
                return
            if check_sanity(self.decimal.text) == False:
                self.decimal.text = ''
                self.binary.text = ''
                self.octal.text = ''
                self.hex.text = ''
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()
                return
            try:
                self.decimal.text = check_leading_zeros(self.decimal.text)
                answer = convert_scientific_notation(str(eval(self.decimal.text)))
                history.append("Base 16: "+self.hex.text+"="+decimal_conversions(answer,16))
                self.decimal.text = answer
                self.binary.text = decimal_conversions(answer,2)
                self.octal.text = decimal_conversions(answer,8)
                self.hex.text = decimal_conversions(answer,16)
                self.was_last_equal = True
            except Exception as e:
                popup = Popup(title='',separator_height=0,content=Label(text="Invalid format"),size_hint=(None, None), size=(400, 400))
                popup.open()

        elif button_text == ".":
            if not self.hex.text:
                self.decimal.text = "0."
                self.binary.text = "0."
                self.octal.text = "0."
                self.hex.text = "0."
                self.was_last_equal = False
            else:
                if self.hex.text[-1] in self.operators:
                    self.decimal.text = self.decimal.text + "0" + button_text
                    self.binary.text = self.binary.text + "0" + button_text
                    self.octal.text = self.octal.text + "0" + button_text
                    self.hex.text = self.hex.text + "0" + button_text
                    self.was_last_equal = False
                elif is_decimal_valid(self.hex.text) and self.hex.text[-1] in self.numbers:
                    self.decimal.text = self.decimal.text + button_text
                    self.binary.text = self.binary.text + button_text
                    self.octal.text = self.octal.text + button_text
                    self.hex.text = self.hex.text + button_text
                    self.was_last_equal = False
            
if __name__ == "__main__":
    app = MainApp()
    app.run()

