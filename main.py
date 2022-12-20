from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from pathlib import Path
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivy.uix.tabbedpanel import TabbedPanel

Window.size = (490,800)

kv = ('''
<MenuScreen>:
    
    canvas.before:
        Rectangle:
    
            pos: self.pos
            size: self.size
            source: 'img/bluel.jpg'
    GridLayout:
        rows:2
        do_default_tab: False
        pos_hint: {'center_x': .5, 'center_y': .5}

        Label:
            font_size: 78
            font_name: 'fonts/blocky'
            color: (3,2,0)
            text:
                """Grade This!"""
                
        GridLayout:
            rows: 3
            padding:dp(100) # padding: [dp(20),dp(10),dp(20),dp(10)]
            size_hint: 1,.51
            Button:
                text: 'Grade calculator'
                on_press: root.manager.current = 'add_grade'
            
            Button:
                text: 'How to use'
                on_press: root.manager.current = 'howto'
            
            Button:
                text: 'About'
                on_press: root.manager.current = 'about'
            
<MyTextInput@TextInput>:
    hint_text: '0'
    text: '0'
<MyLabel@Label>:
    text: 'Grade Group'


<text>:
    color: (255,255,255,1)
    background_color: (0, 30, 55, 255)
<Label@Label>:
    color: (1,1,1)
    background_color: (1,2,2,1)
<Grade_check>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'img/words.jpg'
    grade: g1,g2,g3,g4,g5,g6,g7,g8
    weight: w1,w2,w3,w4,w5,w6,w7,w8
    GridLayout:
        rows: 2
        GridLayout:
            cols: 4
            MyLabel:
            MyTextInput:
                id: g1
            Label:
                text: 'Weight'
            MyTextInput:
                id: w1
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g2
            Label:
                text: 'Weight'
            MyTextInput:
                id: w2
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g3
            Label:
                text: 'Weight'
            MyTextInput:
                id: w3
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g4
            Label:
                text: 'Weight'
            MyTextInput:
                id: w4
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g5
            Label:
                text: 'Weight'
            MyTextInput:
                id: w5
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g6
            Label:
                text: 'Weight'
            MyTextInput:
                id: w6
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g7
            Label:
                text: 'Weight'
            MyTextInput:
                id: w7
        #----------------------------------------------
            MyLabel:
            MyTextInput:
                id: g8
            Label:
                text: 'Weight'
            MyTextInput: 
                id: w8
        #----------------------------------------------
            Label:
                text: 'Output'
            Label:
                
                text: 'here'
                id: output1
        GridLayout:
            cols:3
            size_hint: .1,.1
            Button:
    
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
            Button:
                id: avg
                text: 'calculate'
                on_press: app.save(g1,g2,g3,g4,g5,g6,g7,g8,w1,w2,w3,w4,w5,w6,w7,w8)
            
        
        
            
<How_to_use>:
    
    canvas.before:
        Rectangle:
    
            pos: self.pos
            size: self.size
            source: 'img/words.jpg'
    GridLayout:
        rows: 2
        AsyncImage:
            
            source: 'img/ex.png'
            size_hint: 1.5,1.5
        GridLayout:
            rows: 2
            Label:
                id: howt
                text:
                    """Each row a has place for your assignment group grade\n
                    and how much its worth for that class\n
                    -\n
                    one row could have the grade for your tests\n
                    and another could be homeworks"""
            Button:
                size_hint: .4,.2
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
            
            
<About>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'img/words.jpg'

    GridLayout:
        rows:2
        AsyncImage:
            
            source: 'img/me.jpg'
            size_hint: .5,.2
        GridLayout:
            rows:2
            Label:
                text:
                    """Created - May 31,2022\n
                    -\n
                    -\n
                    Links:\n
                    https://github.com/AhmedMurshid \n
                    -\n
                    hwww.linkedin.com/in/ahmed001a"""
    
            Button:
                size_hint: .1,.1
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'
            
        
''')


class MenuScreen(Screen):
    pass

class Grade_check(Screen):
    pass

class How_to_use(Screen):
    pass
class About(Screen):
    pass



#df = pd.DataFrame(index=['row 1','row 2']col_names = ['Names', 'weights'])

class MyApp(App):
    #avg_num = StringProperty()
    
    def build(self):
        
        Builder.load_string(kv)
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Grade_check(name='add_grade'))
        sm.add_widget(How_to_use(name='howto'))
        sm.add_widget(About(name='about'))
    
        return sm
    def save(self, g1,g2,g3,g4,g5,g6,g7,g8,w1,w2,w3,w4,w5,w6,w7,w8):
        o1 = self.root.get_screen('add_grade').ids.output1
        Dict = {1: float(g1.text) * float((w1.text.strip('%')))/100,
                2: float(g2.text) * float((w2.text.strip('%')))/100,
                3: float(g3.text) * float((w3.text.strip('%')))/100,
                4: float(g4.text) * float((w4.text.strip('%')))/100,
                5: float(g5.text) * float((w5.text.strip('%')))/100,
                6: float(g6.text) * float((w6.text.strip('%')))/100,
                7: float(g7.text) * float((w7.text.strip('%')))/100,
                8: float(g8.text) * float((w8.text.strip('%')))/100}
        
        values = Dict.values()
        total = sum(values)
        print(total)
        o1.text = str(total)
        
        return total
        
    
        
    

if __name__ == '__main__':
    MyApp().run()
