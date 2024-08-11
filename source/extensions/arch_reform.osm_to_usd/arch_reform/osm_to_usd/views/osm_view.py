from ..view import View
import omni.ui as ui
from typing import Any
from ..controllers import WindowController

class OSMView(View):
    def __init__(self, window_controller: WindowController):
        super().__init__()

        self._window_controller = window_controller

    @property
    def root_collapsable_frame(self):
        return self._root_collapsable_frame

    def build(self) -> None:
        self._root_collapsable_frame = ui.CollapsableFrame(title="Open Street Maps")
        with self._root_collapsable_frame:
            with ui.VStack():
                with ui.HStack(alignment=ui.Alignment.CENTER):
                    ui.Spacer(width=ui.Pixel(10))
                    ui.Label("Area name: ", height=20, tooltip="TODO")

                    self._area_name_field = ui.StringField(height=20)
                    self._area_name_field.model.set_value("")
                    ui.Spacer(width=ui.Pixel(8))

                with ui.HStack(alignment=ui.Alignment.CENTER):
                    with ui.HStack(alignment=ui.Alignment.V_CENTER):
                        ui.Spacer(width=ui.Percent(8))
                        self._load_button = ui.Button(
                            "Load Data",
                            clicked_fn=lambda: self._on_load_osm_clicked_fn(),
                            tooltip="TODO",
                            height=ui.Pixel(25),
                            style={'border_radius':6}
                        )
                        ui.Spacer(width=ui.Percent(8))

    def add_load_callback(self, callback):
        self._load_callbacks.append(callback)

    def _on_load_osm_clicked_fn(self) -> None:
        area_name = self._area_name_field.model.get_value_as_string()
        self._window_controller.load_osm_data(area_name)