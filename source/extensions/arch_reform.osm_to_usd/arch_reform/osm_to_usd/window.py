import omni.ui as ui
import omni.usd
import os.path
from .style import window_style
from .views import GeoJsonView, OSMView, TerrainView
from .controllers import WindowController
from .models import WindowModel

class Window(ui.Window):
    def __init__(self, title: str, delegate=None, **kwargs) -> None:
        super(
        ).__init__(
            title,
            **kwargs
        )

        self._controller = WindowController(self)
        self._label_width = 120
        self._osm_view = OSMView(self._controller)
        self._terrain_view = TerrainView(self._controller)
        self._usd_context = omni.usd.get_context()
        self.frame.style = window_style

    def destroy(self) -> None:
        super().destroy()

    def on_model_update(self, id: str, model: WindowModel):
        if id == "bounding_box":
            self._osm_view.root_collapsable_frame.visible = False
            self._terrain_view._root_collapsable_frame = True
            self._terrain_view.on_data_loaded(model.bounding_box)

    def build(self) -> None:
        with self.frame:
            with ui.ScrollingFrame(
                width=ui.Percent(100),
                height=ui.Percent(100),
                horizontal_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_OFF,
                vertical_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_ON
            ):
                with ui.VStack(height=0):
                    self._osm_view.build()
                    self._terrain_view.build()
