from enum import Enum
from typing import Any, Optional, Callable

from flet.core.constrained_control import ConstrainedControl
from flet.core.control import OptionalNumber

from flet.core.control_event import ControlEvent

import flet as ft

import dataclasses
import time
from enum import Enum
from typing import Any, List, Optional, Union

from flet.core.adaptive_control import AdaptiveControl
from flet.core.animation import AnimationValue
from flet.core.autofill_group import AutofillHint
from flet.core.badge import BadgeValue
from flet.core.box import BoxConstraints
from flet.core.control import Control, OptionalNumber
from flet.core.form_field_control import FormFieldControl, InputBorder
from flet.core.ref import Ref
from flet.core.text_style import StrutStyle, TextStyle
from flet.core.tooltip import TooltipValue
from flet.core.types import (
    BorderRadiusValue,
    Brightness,
    ClipBehavior,
    ColorEnums,
    ColorValue,
    DurationValue,
    IconValueOrControl,
    MouseCursor,
    OffsetValue,
    OptionalControlEventCallable,
    PaddingValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
    TextAlign,
    VerticalAlignment,
)

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

import json

class TextSelection:
    """
    A class to represent a TextSelection object from a JSON dictionary.

    Attributes:
        baseOffset (int): The starting offset of the selection.
        extentOffset (int): The ending offset of the selection.
        isCollapsed (bool): True if the selection is a collapsed cursor.
        isValid (bool): True if the selection is valid.
        start (int): The index of the first character in the selection.
        end (int): The index after the last character in the selection.
    """

    def __init__(self, data: dict):
        """
        Initializes a TextSelection object from a dictionary.

        Args:
            data (dict): A dictionary containing the selection data,
                         typically parsed from a JSON string.
        """
        self.baseOffset = data.get('baseOffset')
        self.extentOffset = data.get('extentOffset')
        self.isCollapsed = data.get('isCollapsed')
        self.isValid = data.get('isValid')

        # The start and end properties are derived from base and extent.
        self.start = min(self.baseOffset, self.extentOffset) if self.baseOffset is not None and self.extentOffset is not None else None
        self.end = max(self.baseOffset, self.extentOffset) if self.baseOffset is not None and self.extentOffset is not None else None

    def __repr__(self):
        """
        Provides a string representation of the TextSelection object.
        """
        return (f"TextSelection(baseOffset={self.baseOffset}, "
                f"extentOffset={self.extentOffset}, "
                f"isCollapsed={self.isCollapsed}, "
                f"isValid={self.isValid}, "
                f"start={self.start}, "
                f"end={self.end})")

    def to_json(self) -> str:
        """
        Converts the TextSelection object to a JSON string.

        Returns:
            str: A JSON string representation of the object.
        """
        # Create a dictionary of the object's attributes
        data_dict = {
            "baseOffset": self.baseOffset,
            "extentOffset": self.extentOffset,
            "isCollapsed": self.isCollapsed,
            "isValid": self.isValid
        }
        return json.dumps(data_dict, indent=4)

class KeyboardType(Enum):
    NONE = "none"
    TEXT = "text"
    MULTILINE = "multiline"
    NUMBER = "number"
    PHONE = "phone"
    DATETIME = "datetime"
    EMAIL = "email"
    URL = "url"
    VISIBLE_PASSWORD = "visiblePassword"
    NAME = "name"
    STREET_ADDRESS = "streetAddress"


class TextCapitalization(Enum):
    CHARACTERS = "characters"
    WORDS = "words"
    SENTENCES = "sentences"


@dataclasses.dataclass
class InputFilter:
    regex_string: str
    allow: bool = True
    replacement_string: str = ""
    multiline: bool = False
    case_sensitive: bool = True
    unicode: bool = False
    dot_all: bool = False


class NumbersOnlyInputFilter(InputFilter):
    def __init__(self):
        super().__init__(regex_string=r"^[0-9]*$", allow=True, replacement_string="")


class TextOnlyInputFilter(InputFilter):
    def __init__(self):
        super().__init__(regex_string=r"^[a-zA-Z]*$", allow=True, replacement_string="")


class FletTextfieldExtras(ft.TextField):
    """
    FletTextfieldExtras Control description.
    """

    def __init__(
            self,
            value: Optional[str] = None,
            keyboard_type: Optional[KeyboardType] = None,
            multiline: Optional[bool] = None,
            min_lines: Optional[int] = None,
            max_lines: Optional[int] = None,
            max_length: Optional[int] = None,
            password: Optional[bool] = None,
            can_reveal_password: Optional[bool] = None,
            read_only: Optional[bool] = None,
            shift_enter: Optional[bool] = None,
            text_align: Optional[TextAlign] = None,
            autofocus: Optional[bool] = None,
            capitalization: Optional[TextCapitalization] = None,
            autocorrect: Optional[bool] = None,
            enable_suggestions: Optional[bool] = None,
            smart_dashes_type: Optional[bool] = None,
            smart_quotes_type: Optional[bool] = None,
            show_cursor: Optional[bool] = None,
            cursor_color: Optional[ColorValue] = None,
            cursor_error_color: Optional[ColorValue] = None,
            cursor_width: OptionalNumber = None,
            cursor_height: OptionalNumber = None,
            cursor_radius: OptionalNumber = None,
            selection_color: Optional[ColorValue] = None,
            input_filter: Optional[InputFilter] = None,
            obscuring_character: Optional[str] = None,
            enable_interactive_selection: Optional[bool] = None,
            enable_ime_personalized_learning: Optional[bool] = None,
            can_request_focus: Optional[bool] = None,
            ignore_pointers: Optional[bool] = None,
            enable_scribble: Optional[bool] = None,
            animate_cursor_opacity: Optional[bool] = None,
            always_call_on_tap: Optional[bool] = None,
            scroll_padding: Optional[PaddingValue] = None,
            clip_behavior: Optional[ClipBehavior] = None,
            keyboard_brightness: Optional[Brightness] = None,
            mouse_cursor: Optional[MouseCursor] = None,
            strut_style: Optional[StrutStyle] = None,
            autofill_hints: Union[None, AutofillHint, List[AutofillHint]] = None,
            on_change: OptionalControlEventCallable = None,
            on_click: OptionalControlEventCallable = None,
            on_submit: OptionalControlEventCallable = None,
            on_focus: OptionalControlEventCallable = None,
            on_blur: OptionalControlEventCallable = None,
            on_tap_outside: OptionalControlEventCallable = None,
            on_selection_change: Callable[[int], None] = None,
            #
            # FormField
            #
            text_size: OptionalNumber = None,
            text_style: Optional[TextStyle] = None,
            text_vertical_align: Union[VerticalAlignment, OptionalNumber] = None,
            label: Optional[Union[str, Control]] = None,
            label_style: Optional[TextStyle] = None,
            icon: Optional[IconValueOrControl] = None,
            border: Optional[InputBorder] = None,
            color: Optional[ColorValue] = None,
            bgcolor: Optional[ColorValue] = None,
            border_radius: Optional[BorderRadiusValue] = None,
            border_width: OptionalNumber = None,
            border_color: Optional[ColorValue] = None,
            focused_color: Optional[ColorValue] = None,
            focused_bgcolor: Optional[ColorValue] = None,
            focused_border_width: OptionalNumber = None,
            focused_border_color: Optional[ColorValue] = None,
            content_padding: Optional[PaddingValue] = None,
            dense: Optional[bool] = None,
            filled: Optional[bool] = None,
            fill_color: Optional[ColorValue] = None,
            hover_color: Optional[ColorValue] = None,
            hint_text: Optional[str] = None,
            hint_style: Optional[TextStyle] = None,
            helper: Optional[Control] = None,
            helper_text: Optional[str] = None,
            helper_style: Optional[TextStyle] = None,
            counter: Optional[Control] = None,
            counter_text: Optional[str] = None,
            counter_style: Optional[TextStyle] = None,
            error: Optional[Control] = None,
            error_text: Optional[str] = None,
            error_style: Optional[TextStyle] = None,
            prefix: Optional[Control] = None,
            prefix_icon: Optional[IconValueOrControl] = None,
            prefix_text: Optional[str] = None,
            prefix_style: Optional[TextStyle] = None,
            suffix: Optional[Control] = None,
            suffix_icon: Optional[IconValueOrControl] = None,
            suffix_text: Optional[str] = None,
            suffix_style: Optional[TextStyle] = None,
            focus_color: Optional[ColorValue] = None,
            align_label_with_hint: Optional[bool] = None,
            hint_fade_duration: Optional[DurationValue] = None,
            hint_max_lines: Optional[int] = None,
            helper_max_lines: Optional[int] = None,
            error_max_lines: Optional[int] = None,
            prefix_icon_size_constraints: Optional[BoxConstraints] = None,
            suffix_icon_size_constraints: Optional[BoxConstraints] = None,
            size_constraints: Optional[BoxConstraints] = None,
            collapsed: Optional[bool] = None,
            fit_parent_size: Optional[bool] = None,
            #
            # ConstrainedControl and AdaptiveControl
            #
            ref: Optional[Ref] = None,
            key: Optional[str] = None,
            width: OptionalNumber = None,
            height: OptionalNumber = None,
            expand: Union[None, bool, int] = None,
            expand_loose: Optional[bool] = None,
            col: Optional[ResponsiveNumber] = None,
            opacity: OptionalNumber = None,
            rotate: Optional[RotateValue] = None,
            scale: Optional[ScaleValue] = None,
            offset: Optional[OffsetValue] = None,
            aspect_ratio: OptionalNumber = None,
            animate_opacity: Optional[AnimationValue] = None,
            animate_size: Optional[AnimationValue] = None,
            animate_position: Optional[AnimationValue] = None,
            animate_rotation: Optional[AnimationValue] = None,
            animate_scale: Optional[AnimationValue] = None,
            animate_offset: Optional[AnimationValue] = None,
            on_animation_end: OptionalControlEventCallable = None,
            tooltip: Optional[TooltipValue] = None,
            badge: Optional[BadgeValue] = None,
            visible: Optional[bool] = None,
            disabled: Optional[bool] = None,
            data: Any = None,
            rtl: Optional[bool] = None,
            adaptive: Optional[bool] = None,
    ):
        super().__init__(value, keyboard_type, multiline, min_lines, max_lines, max_length, password, can_reveal_password, read_only, shift_enter, text_align, autofocus, capitalization, autocorrect, enable_suggestions, smart_dashes_type, smart_quotes_type, show_cursor, cursor_color, cursor_error_color, cursor_width, cursor_height, cursor_radius, selection_color, input_filter, obscuring_character, enable_interactive_selection, enable_ime_personalized_learning, can_request_focus, ignore_pointers, enable_scribble, animate_cursor_opacity, always_call_on_tap, scroll_padding, clip_behavior, keyboard_brightness, mouse_cursor, strut_style, autofill_hints, on_change, on_click, on_submit, on_focus, on_blur, on_tap_outside, text_size, text_style, text_vertical_align, label, label_style, icon, border, color, bgcolor, border_radius, border_width, border_color, focused_color, focused_bgcolor, focused_border_width, focused_border_color, content_padding, dense, filled, fill_color, hover_color, hint_text, hint_style, helper, helper_text, helper_style, counter, counter_text, counter_style, error, error_text, error_style, prefix, prefix_icon, prefix_text, prefix_style, suffix, suffix_icon, suffix_text, suffix_style, focus_color, align_label_with_hint, hint_fade_duration, hint_max_lines, helper_max_lines, error_max_lines, prefix_icon_size_constraints, suffix_icon_size_constraints, size_constraints, collapsed, fit_parent_size, ref, key, width, height, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, badge, visible, disabled, data, rtl, adaptive)

        self.value = value
        self.on_cursor_update = self.update_event
        
        self.on_selection_change = on_selection_change
        #self._add_event_handler("tupdate", lambda e: print("Updated", e.data))
        self.__text_selection: Optional[TextSelection] = None

    def _get_control_name(self):
        return "flet_textfield_extras"

    # value
    @property
    def value(self):
        """
        Value property description.
        """
        return self._get_attr("value")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

    @property
    def text_selection(self) -> TextSelection:
        return self.__text_selection

    @text_selection.setter
    def text_selection(self, value: Optional[TextSelection]):
        self.__text_selection = value

    def set_cursor_position(self, position: int, update: bool = True):
        self.__text_selection = TextSelection({"baseOffset": position, "extentOffset": position})

        if update:
            self._set_attr("selection", self.__text_selection.to_json())
            self.update()

    def get_cursor_position(self):
        return self.__text_selection.baseOffset
    
    def insert_text(self, text: str, position: int):
        self.value = self.value[:position] + text + self.value[position:]
        self.update()
        
    @property
    def on_cursor_update(self):
        return self._get_event_handler("selection_update")

    @on_cursor_update.setter
    def on_cursor_update(self, handler):
        self._add_event_handler("selection_update", handler)

    def update_event(self, e):
        if e.name == "selection_update":
            self.__text_selection = TextSelection(json.loads(e.data))
            self.on_selection_change(self.__text_selection)

    def get_selection(self):
        return str(self.value)[self.__text_selection.baseOffset:self.__text_selection.extentOffset]

    def set_selection(self, base_offset: int, extent_offset: int):
        self.__text_selection = TextSelection({"baseOffset": base_offset, "extentOffset": extent_offset})
        self._set_attr("selection", self.__text_selection.to_json())
        self.update()
