import omni.ui as ui

class Window(ui.Window):
    def __init__(self, title: str, delegate=None, **kwargs):
        super().__init__(title, **kwargs)

        self._label_width = 120

    def destroy(self):
        super().destroy()
