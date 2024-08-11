from typing import Any

class Model():
    def __init__(self, view: Any) -> None:
        self._view = view

    def notify_update(self, id: str) -> None:
        self._view.on_model_update(id, self)