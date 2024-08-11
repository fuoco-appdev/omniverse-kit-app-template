from omni.ui import color as cl
from omni.ui import constant as fl
from omni.ui import url
import omni.kit.app
import omni.ui as ui
import pathlib

EXTENSION_FOLDER_PATH = pathlib.Path(
    omni.kit.app.get_app().get_extension_manager().get_extension_path_by_module(__name__)
)

# Pre-defined constants. It's possible to change them runtime.
cl.window_attribute_bg = cl("#1f2124")
cl.window_attribute_fg = cl("#0f1115")
cl.window_hovered = cl("#FFFFFF")
cl.window_text = cl("#CCCCCC")
fl.window_attr_hspacing = 10
fl.window_attr_spacing = 1
fl.window_group_spacing = 2
url.window_icon_closed = f"{EXTENSION_FOLDER_PATH}/data/closed.svg"
url.window_icon_opened = f"{EXTENSION_FOLDER_PATH}/data/opened.svg"

# The main style dict
window_style = {
    "Label::attribute_name": {
        "alignment": ui.Alignment.RIGHT_CENTER,
        "margin_height": fl.window_attr_spacing,
        "margin_width": fl.window_attr_hspacing,
    },
    "Label::attribute_name:hovered": {"color": cl.window_hovered},
    "Label::collapsable_name": {"alignment": ui.Alignment.LEFT_CENTER},
    "Slider::attribute_int:hovered": {"color": cl.window_hovered},
    "Slider": {
        "background_color": cl.window_attribute_bg,
        "draw_mode": ui.SliderDrawMode.HANDLE,
    },
    "Slider::attribute_float": {
        "draw_mode": ui.SliderDrawMode.FILLED,
        "secondary_color": cl.window_attribute_fg,
    },
    "Slider::attribute_float:hovered": {"color": cl.window_hovered},
    "Slider::attribute_vector:hovered": {"color": cl.window_hovered},
    "Slider::attribute_color:hovered": {"color": cl.window_hovered},
    "CollapsableFrame::group": {"margin_height": fl.window_group_spacing},
    "Image::collapsable_opened": {"color": cl.window_text, "image_url": url.window_icon_opened},
    "Image::collapsable_closed": {"color": cl.window_text, "image_url": url.window_icon_closed},
}