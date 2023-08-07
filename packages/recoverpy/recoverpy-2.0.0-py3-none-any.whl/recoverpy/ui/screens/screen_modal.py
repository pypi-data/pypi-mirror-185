"""Screen used to display a modal dialog."""
from typing import Callable, Optional

from textual.app import ComposeResult
from textual.containers import Grid, Horizontal
from textual.screen import Screen
from textual.widgets import Button, Label


class ModalScreen(Screen):
    _message_label = Label("", id="modal-message")
    _callback: Callable

    def set(self, message: str, callback: Optional[Callable] = None) -> None:
        self._message_label.update(message)
        if callback:
            self._callback = callback
        else:
            self._callback = self.app.pop_screen

    def compose(self) -> ComposeResult:
        yield Grid(
            self._message_label,
            Horizontal(
                Button("OK", id="ok-button"),
                id="modal-button-container",
            ),
            id="modal-container",
        )

    def on_button_pressed(self) -> None:
        self._callback()
