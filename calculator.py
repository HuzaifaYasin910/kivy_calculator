from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button  
from kivy.lang import Builder
from kivy.core.window import Window

Window.size=(460,660)
Builder.load_string('''

#:import utils kivy.utils
<MyLayout>

    BoxLayout:
		orientation: "vertical"
		size: root.width, root.height
		
		TextInput:
			id: calc_input
			text: "0"
			halign: "right"
			font_size: 80
			size_hint: (1, .30)
            foreground_color: utils.get_color_from_hex('#faf9f7')
            background_normal:""
		    background_color: utils.get_color_from_hex('#0d0d0c')

		GridLayout:
			cols: 4
			rows: 5

			# Row
			Button:
				size_hint: (.2, .2)
				font_size: 55
			
				text: "AC"
                foreground_color: utils.get_color_from_hex('#faf9f7')
                background_normal:""
                
		        background_color: utils.get_color_from_hex('#b0aca7')

                on_press: root.clear()


			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "+/-"
                background_normal:""
                foreground_color: utils.get_color_from_hex('#faf9f7')
		        background_color: utils.get_color_from_hex('#b0aca7')


				on_press: root.pos_neg()

			Button:
				id: clear
				size_hint: (.2, .2)
				font_size: 55
				text: "%"
                background_normal:""
                foreground_color: utils.get_color_from_hex('#faf9f7')
		        background_color: utils.get_color_from_hex('#b0aca7')

				on_press: root.opp_mod("/")
				
			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "÷"
                background_normal:""
		        background_color: utils.get_color_from_hex('#f69906')

				on_press: root.opp_sign("/")

			# Row
			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "7"
                background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(7)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "8"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(8)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "9"
			    background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(9)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: 'x'
                background_normal:""
		        background_color: utils.get_color_from_hex('#f69906')
				on_press: root.opp_sign("*")

			# Row
			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "4"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(4)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "5"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(5)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "6"
                background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
                on_press: root.button_press(6)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "-"
                background_normal:""
		        background_color: utils.get_color_from_hex('#f69906')
				on_press: root.opp_sign("-")

			# Row
			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "1"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(1)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "2"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.button_press(2)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "3"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')       
				on_press: root.button_press(3)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "+"
                background_normal:""
		        background_color: utils.get_color_from_hex('#f69906')
                on_press: root.opp_sign("+")

			# Row
			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "0"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')         
				on_press: root.button_press(0)

			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "c"
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.remove()
			Button:
				size_hint: (.2, .2)
				font_size: 55
				text: "."
				background_normal:""
		        background_color: utils.get_color_from_hex('#313131')
				on_press: root.dot()

			Button:
				size_hint:(.2, .2)
				font_size: 55
				text: "="
                background_normal: ''
				background_color: utils.get_color_from_hex('#f69906')
                on_press: root.equals()

''')
class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # Create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was in the text box already
        global prev
        prev = self.ids.calc_input.text
        
        # Test for error first
        if "Syntax Error" in prev:
            prev = ''

        # determine if 0 is sitting there
        if prev == "0":
                self.ids.calc_input.text = ''
                self.ids.calc_input.text = f'{button}'
        else: 
            self.ids.calc_input.text = f'{prev}{button}'
    z
    def remove(self):
        prev = self.ids.calc_input.text
        # Remove The last item in the textbox 
        prev = prev[:-1]
        # Output back to the textbox.
        self.ids.calc_input.text = prev
        if prev == "":
            self.ids.calc_input.text = '0'
        else:
            self.ids.calc_input.text = prev
    # Create function to make text box positive or negative
    def pos_neg(self):
        prev = self.ids.calc_input.text
        # Test to see if there's a - sign already
        if "-" in prev:
             self.ids.calc_input.text = f'{prev.replace("-", "")}'			 
        else:
            self.ids.calc_input.text = f'-{prev}'
    # Create decimal function
    def dot(self):
        prev = self.ids.calc_input.text
        if prev == 'Syntax Error':
            prev=''
        # Split out text box by +
        num_list = prev.split("+")

       
        
        if "+" in prev and "." not in num_list[-1]:
            # Add a decimal to the end of the text
            prev = f'{prev}.'
            # O utput back to the text box
            self.ids.calc_input.text = prev

        elif "." in prev:
            pass
        else:
            # Add a decimal to the end of the text
            prev = f'{prev}.'
            # Output back to the text box
            self.ids.calc_input.text = prev

    # create addition function
    def opp_sign(self, sign):
        # create a variable that contains whatever was in the text box already
        prev = self.ids.calc_input.text
        
        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prev}{sign}'

    
    # create equals to function
    def equals(self):
        prev = self.ids.calc_input.text
         # Error Handling
        try:
             # Evaluate the math from the text box
            answer = eval(prev)
            # Output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Syntax Error"

    
    
    def neg_opp(self,opp):
        prev = self.ids.calc_input.text
        # Test to see if there's a - sign already
        if "-" in prev:
             self.ids.calc_input.text = f'{prev.replace("-", "")}'
    # %
    def opp_mod(self,mod):
            bg=100
            prev = self.ids.calc_input.text
            if prev == 'Syntax Error':
                prev=''

            elif prev == str :
                self.ids.calc_input.text = "Syntax Error"
            else:
                prev=  f'{prev}{mod}{100}'               
                self.ids.calc_input.text= prev
                answer = eval(prev)
                self.ids.calc_input.text = str(answer)
                
        

class calculatorApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,1)
        return MyLayout()


if __name__ == '__main__':
    calculatorApp().run()
