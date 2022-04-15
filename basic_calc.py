from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from button_press import on_button_press


class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_was_equal = False
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        h_layout = BoxLayout()
        equals_button = Button(
            text="=", size_hint=(3.0, 1.0), pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        backspace_button = Button(
            text="Backspace", size_hint=(1.0, 1.0), pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        backspace_button.bind(on_press=self.on_backspace)
        h_layout.add_widget(equals_button)
        h_layout.add_widget(backspace_button)

        main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        print(self.last_button,self.last_was_equal)
        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            if not '/0' in text:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
                self.last_was_equal == True
            else:
                solution = ""
                self.solution.text = solution
                self.last_button = "C"
    
    def on_backspace(self, instance):
        text = self.solution.text
        if text:
            solution = text[:-1]
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()

