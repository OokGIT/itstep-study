class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)

        self._list = []

    def build(self):
        box = BoxLayout(orientation='vertical')
        box_v = BoxLayout(orientation='horizontal')

        self.first = Buttton(text="List")
        self.second = Button(text="Create")

        box_v.add_widget(self.second)
        box_v.add_widget(self.first)
        box.add_widget(self.first)

        # self.interface = InterfaceManager(orientation='vertical', self=self)

        box_v = add_widget(orientation='vertical')

        return box