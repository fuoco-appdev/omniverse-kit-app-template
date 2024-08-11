from ..view import View
from ..controllers import WindowController, TerrainController
from ..models import TerrainModel
import omni.ui as ui
from typing import List

class TerrainView(View):
    def __init__(self, window_controller: WindowController):
        super().__init__()

        self._window_controller = window_controller
        self._terrain_controller = TerrainController(self)

    def on_model_update(self, id: str, model: TerrainModel):
        pass

    def build(self):
        self._root_collapsable_frame = ui.CollapsableFrame(title="Terrain")
        self._root_collapsable_frame.visible = False
        with self._root_collapsable_frame:
            with ui.VStack():
                pass

    def on_data_loaded(self, bounding_box: List[tuple]) -> None:
        self._terrain_controller.load_terrain(bounding_box)
