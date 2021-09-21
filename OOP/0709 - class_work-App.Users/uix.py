from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
import functools
import class_UserList

from kivy.uix.textinput import TextInput


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
        # self._self._list.append({'a': 'a'})

        for index, data in enumerate(self._self._list):
            self.label = Label(text=str(data))

            self.add_widget(self.label)

            first = Button(text="List")
            first.bind(on_press=functools.partial(self.user_click, index=index,
                                                  data=data))

            self.add_widget(first)

    def change(self, button):
        self.clear_widgets()
        print(self._self._list)
        self.label = Label(text='1')
        self.add_widget(self.label)

    def on_text(self, _, value, data, key):
        data[key] = value

    def _create_user_widget(self, key, user_data):
        box_h = BoxLayout(orientation='horizontal')

        label = Label(text=f'{key.upper()} : ', size_hint=(.3, 1))
        box_h.add_widget(label)

        textinput = TextInput(text=user_data[key])
        textinput.bind(
            text=functools.partial(self.on_text, data=user_data, key=key))

        box_h.add_widget(textinput)
        return box_h

    def user_click(self, *args, **kwargs):
        self.clear_widgets()

        user_data = kwargs.get('data')
        box = BoxLayout(orientation='vertical')

        el_id = self._create_user_widget(key='user_id', user_data=user_data)
        box.add_widget(el_id)
        el_name = self._create_user_widget(key='name', user_data=user_data)
        box.add_widget(el_name)
        el_lastname = self._create_user_widget(key='lastname', user_data=user_data)
        box.add_widget(el_lastname)
        el_age = self._create_user_widget(key='age', user_data=user_data)
        box.add_widget(el_age)
        el_city = self._create_user_widget(key='city', user_data=user_data)
        box.add_widget(el_city)

        # textinput = TextInput(text=user_data['name'])
        # textinput.bind(text=self.on_text)
        #
        # box.add_widget(textinput)

        self.add_widget(box)


class MyApp(App):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self._list = class_UserList.users_list

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
