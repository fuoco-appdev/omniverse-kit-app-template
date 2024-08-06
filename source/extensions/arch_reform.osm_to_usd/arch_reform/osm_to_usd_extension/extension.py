# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: LicenseRef-NvidiaProprietary
#
# NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
# property and proprietary rights in and to this material, related
# documentation and any modifications thereto. Any use, reproduction,
# disclosure or distribution of this material and related documentation
# without an express license agreement from NVIDIA CORPORATION or
# its affiliates is strictly prohibited.

import omni.ext
import omni.ui as ui
import omni.kit.ui
from .window import Window
from functools import partial
import asyncio


# Functions and vars are available to other extensions as usual in python: `arch_reform.osm_to_usd.some_public_function(x)`
def some_public_function(x: int):
    print(f"[arch_reform.osm_to_usd] some_public_function was called with {x}")
    return x ** x


# Any class derived from `omni.ext.IExt` in the top level module (defined in `python.modules` of `extension.toml`) will
# be instantiated when the extension gets enabled, and `on_startup(ext_id)` will be called.
# Later when the extension gets disabled on_shutdown() is called.
class OsmToUsdExtension(omni.ext.IExt):
    # ext_id is the current extension id. It can be used with the extension manager to query additional information,
    # like where this extension is located on the filesystem.
    def __init__(self) -> None:
        super().__init__()

        self._window_name = "OSM to USD"
        self._menu_path = f"Window/{self._window_name}"

    def on_startup(self, ext_id):
        self._count = 0
        ui.Workspace.set_show_window_fn(self._window_name, partial(self._show_window, None))

        editor_menu = omni.kit.ui.get_editor_menu()
        if editor_menu:
            self._menu = editor_menu.add_item(
                self._menu_path,
                self._show_window,
                toggle=True,
                value=True
            )

        ui.Workspace.show_window(self._window_name)

    def on_shutdown(self):
        if self._window:
            self._window.destroy()
            self._window = None

        # Deregister the function that shows the window from omni.ui
        ui.Workspace.set_show_window_fn(self._window_name, None)

    def _show_window(self, menu, value):
        if value:
            self._window = Window(self._window_name, width=300, height=365)
            self._window.set_visibility_changed_fn(self._visiblity_changed_fn)
        elif self._window:
            self._window.visible = False

    def _visiblity_changed_fn(self, visible):
        # Called when the user pressed "X"
        self._set_menu(visible)
        if not visible:
            # Destroy the window, since we are creating new window
            # in show_window
            asyncio.ensure_future(self._destroy_window_async())

    def _set_menu(self, value):
        editor_menu = omni.kit.ui.get_editor_menu()
        if editor_menu:
            editor_menu.set_value(self._menu_path, value)

    async def _destroy_window_async(self):
        # wait one frame, this is due to the one frame defer
        # in Window::_moveToMainOSWindow()
        await omni.kit.app.get_app().next_update_async()
        if self._window:
            self._window.destroy()
            self._window = None
