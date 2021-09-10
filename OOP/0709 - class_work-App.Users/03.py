from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import functools

class InterfaceManager(BoxLayout):

    def __init__(self, **kwargs):
        _self = kwargs.pop('_self')

        super(InterfaceManager, self).__init__(**kwargs)

        self._self = _self

        self.label = Label(text='Конвертер')
        # self._self.second.bind(on_press=self.show_final)
        # self._self.first.bind(on_press=self.show_second)

        self.add_widget(self.label)

    def append(self, button):
        self.clear_widgets()
        self._self._list.append({'a': 'a'})
        for index, data in enumerate(self._self._list):
            self.label = Label(text=str(data))

            self.add_widget(self.label)
            first = Button(text="List")
            first.bind(on_press=functools.partial(self.user_click, index=index, data=data))
            self.add_widget(first)

    def change(self, button):
        self.clear_widgets()
        print(self._self._list)
        self.label = Label(text='1')
        self.add_widget(self.label)

    def user_click(self, button, *args, **kwargs):
        print('asd')
        print(args)
        print(kwargs)


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

        self._list = [{'name': 'asd'}]

    def build(self):
        box = BoxLayout(orientation='vertical')
        box_v = BoxLayout(orientation='horizontal', size_hint=(1, .4))
        box_v.height = 1
        self.first = Button(text="List")
        self.second = Button(text="Create")

        box_v.add_widget(self.second)
        box_v.add_widget(self.first)

        box.add_widget(box_v)

        self.interface = InterfaceManager(orientation='vertical', _self=self)

        self.first.bind(on_press=self.interface.append)
        self.second.bind(on_press=self.interface.change)

        box.add_widget(self.interface)

        return box


if __name__ == '__main__':
    MyApp().run()
