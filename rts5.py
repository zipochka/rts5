import kivy.app
import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button
import math

class SimpleApp(kivy.app.App):
    def build(self):
        self.textInput = kivy.uix.textinput.TextInput()
        self.label = kivy.uix.label.Label(text="Enter your number above.")
        self.button = kivy.uix.button.Button(text="Factorize.")
        self.button.bind(on_press=self.displayMessage)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(self.textInput)
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)

        return self.boxLayout

    def displayMessage(self, btn):
        text = self.textInput.text
        if text.isdigit():
            n = int(text)
            f, s = self.factorization(n)
            self.label.text = "For n = {}.\nFirst term = {}.\nSecond term = {}.".format(n, f, s)
        else:
            self.label.text = "Your input should be an integer."

    def factorization(self, n):
        s = math.ceil(math.sqrt(n))
        k = 0
        while True:
            x = s + k
            y_2 = x**2 - n
            y = int(math.sqrt(y_2))

            if y*y == y_2:
                break
            elif x > (n+1) / 2:
                x, y = 0, 0
                break
            
            k += 1
        
        p = x + y
        q = x - y
        return p, q


if __name__ == "__main__":
    app = SimpleApp()
    app.run()
