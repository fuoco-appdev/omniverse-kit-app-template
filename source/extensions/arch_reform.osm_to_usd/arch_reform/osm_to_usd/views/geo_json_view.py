from ..view import View
import omni.ui as ui
import omni.usd
import os.path
from ..callback_list import CallbackList

class GeoJsonView(View):
    def __init__(self):
        super().__init__()

        self._load_callbacks = CallbackList()

    def build(self) -> None:
        self._root_collapsable_frame = ui.CollapsableFrame(title="GeoJSON")
        with self._root_collapsable_frame:
            with ui.VStack():
                with ui.HStack(alignment=ui.Alignment.CENTER):
                    ui.Spacer(width=ui.Pixel(8))
                    ui.Label("File location(s): ", height=20, tooltip="TODO")

                    self._geojson_folder_path = ui.StringField(height=20)
                    self._geojson_folder_path.model.set_value("./")
                    ui.Spacer(width=ui.Pixel(8))

                    with ui.HStack(width=20, height=20,alignment=ui.Alignment.CENTER):
                        with ui.ZStack(alignment=ui.Alignment.CENTER):
                            with ui.HStack(alignment=ui.Alignment.CENTER):
                                ui.Spacer(width=ui.Pixel(8))
                                with ui.VStack(width=0, alignment=ui.Alignment.CENTER):
                                    ui.Spacer(height=ui.Pixel(8))
                                    ui.Rectangle(
                                        style={
                                            "background_color": ui.color(81,81,81),
                                            "border_radius" : 6.0
                                        },
                                        width=ui.Pixel(5),
                                        height=ui.Pixel(5),
                                        name="reset_invalid",
                                        alignment=ui.Alignment.CENTER
                                    )
                                    ui.Spacer(height=ui.Pixel(8))
                                ui.Spacer(width=ui.Pixel(8))
                            with ui.HStack(alignment=ui.Alignment.CENTER):
                                #ui.Spacer(width=ui.Pixel(0))
                                with ui.VStack(width=0, alignment=ui.Alignment.CENTER):
                                    ui.Spacer(height=ui.Pixel(2))
                                    self._geojson_folder_path_default = ui.Rectangle(
                                        style={
                                                "background_color": ui.color(80,124,153),
                                                "border_radius" : 6.0
                                        },
                                        width=18,
                                        height=18,
                                        name="reset",
                                        tooltip="Click to reset value"
                                    )
                                    ui.Spacer(height=ui.Pixel(2))
                                #ui.Spacer(width=ui.Pixel(0))

                            self._geojson_folder_path_default.visible = False

                        self._geojson_folder_path_default.set_mouse_pressed_fn(
                            lambda x,
                            y,
                            m,
                            w: self._reset_button(
                                self._geojson_folder_path.model,
                                "./",
                                self._geojson_folder_path_default
                            )
                        )
                        self._geojson_folder_path.model.add_end_edit_fn(
                            lambda x: self._string_field_changed(
                                self._geojson_folder_path,
                                "./",
                                self._geojson_folder_path_default
                            )
                        )

                    ui.Spacer(width=ui.Pixel(10))

                with ui.HStack(width=ui.Percent(10), alignment=ui.Alignment.CENTER):
                    ui.Spacer(width=ui.Pixel(10))

                    with ui.HStack(alignment=ui.Alignment.LEFT_CENTER):
                        self._is_recursive_check_box = ui.CheckBox(alignment=ui.Alignment.CENTER)
                        ui.Spacer(width=ui.Pixel(8))
                        ui.Label(
                            "Recursively check for GeoJSON files?",
                            height=20,
                            tooltip="Recursively check for GeoJSON files given the passed file directory?"
                        )

                    ui.Spacer(width=ui.Pixel(10))

                    #ui.Spacer(height=ui.Pixel(5))
                with ui.HStack(alignment=ui.Alignment.CENTER): # 3 nested HStack below
                    with ui.HStack(alignment=ui.Alignment.V_CENTER): # Load button
                        ui.Spacer(width=ui.Percent(5))
                        self._load_button = ui.Button(
                            "Load GeoJSON File(s)",
                            clicked_fn=lambda: self._on_load_geojson_clicked_fn(),
                            tooltip="TODO",
                            height=ui.Pixel(25),
                            style={'border_radius':5}
                        )
                        ui.Spacer(width=ui.Percent(5))

    @property
    def root_collapsable_frame(self):
        return self._root_collapsable_frame

    def add_load_callback(self, callback):
        self._load_callbacks.append(callback)

    def _reset_button(self, model : ui._ui.AbstractItemModel, default_value, rectangle : ui._ui.Rectangle):
        model.set_value(default_value)
        rectangle.visible = False

    def _string_field_changed (self, string_field : ui._ui.StringField, default_value : float, rectangle : ui._ui.Rectangle):
        if (string_field.model.get_value_as_string() != default_value):
            rectangle.visible = True
        else:
            rectangle.visible = False

    def _on_load_geojson_clicked_fn(self) -> None:
        print ("Button clicked to convert GeoJSON files")
        stage_url = self._usd_context.get_stage_url()
        geojson_folder_path = self._geojson_folder_path.model.get_value_as_string()
        recursive = self._is_recursive_check_box.model.get_value_as_bool()
        if (geojson_folder_path != ""):
            if (os.path.exists(geojson_folder_path)):
                geojson_folder_path = os.path.abspath(geojson_folder_path)
                print("Folder path to GeoJSON file(s) is: " + geojson_folder_path)
                self._load_callbacks.call()
                #if (os.access(geojson_folder_path, os.R_OK)):
                    #if (self._geojson_helper.convert_geojson_python(
                            #stage_url = str(stage_url),
                            #download_url = str(geojson_folder_path),
                            #recursive = bool(recursive)
                        #) != 0
                    #):
                       #print("GeoJSON Conversion failed.")
                #else:
                   # print("User does not have read permissions for this folder.")
            else:
                print("Folder path to GeoJSON file(s) does not exist.")
        else:
            print("Folder path to GeoJSON file(s) is empty.")