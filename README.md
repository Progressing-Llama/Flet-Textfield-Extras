# FletTextfieldExtras
The `FletTextfieldExtras` control is an enhanced version of the standard Flet `TextField`, offering a wider range of text manipulation and selection capabilities. It provides additional properties and methods for handling text selection, cursor position, and text insertion, giving developers more granular control over user input. This makes it ideal for building applications that require rich text editing features or precise cursor and selection management.

## Installation

The python api can be installed from PyPI:
```bash
pip install flet-textfield-extras
```

Add dependency to `pyproject.toml` of your Flet app:

  * **Git dependency**

Link to git repository:

```
dependencies = [
  "flet-textfield-extras @ git+https://github.com/Progressing-Llama/Flet-Textfield-Extras",
  "flet>=0.28.3",
]
```

  * **PyPi dependency** If the package is published on pypi.org:

<!-- end list -->

```
dependencies = [
  "flet-textfield-extras",
  "flet>=0.28.3",
]
```

Build your app:

```
flet build macos -v
```

## Documentation

[Link to documentation](https://github.com/Progressing-Llama/Flet-Textfield-Extras)

## Text Selection Properties and Functions

The `FletTextfieldExtras` control extends the standard Flet `TextField` to provide enhanced text selection capabilities. It introduces new properties and methods for getting and setting the text selection, as well as handling selection-related events.

| Property/Function | Type | Description |
| :--- | :--- | :--- |
| `text_selection` | `TextSelection` | Represents the current text selection state of the `TextField` as a `TextSelection` object. |
| `on_selection_change` | `Callable[[TextSelection], None]` | An event handler that is called when the text selection within the `TextField` changes. It passes the new `TextSelection` object to the handler. |
| `set_cursor_position(position: int, update: bool = True)` | `function` | Sets the cursor position (a collapsed selection) at the specified `position`. If `update` is `True`, the UI is updated immediately. |
| `get_cursor_position()` | `function` | Returns the current cursor position. |
| `insert_text(text: str, position: int)` | `function` | Inserts the given `text` at the specified `position` in the `TextField`'s value. |
| `get_selection()` | `function` | Returns the currently selected text as a string. |
| `set_selection(base_offset: int, extent_offset: int)` | `function` | Sets the text selection from `base_offset` to `extent_offset`. |

## `TextSelection` Object

The `TextSelection` class is a crucial part of the enhanced selection functionality. It represents the state of the text selection and is used by the `text_selection` property and the `on_selection_change` event.

| Property | Type | Description |
| :--- | :--- | :--- |
| `baseOffset` | `int` | The starting offset of the selection. |
| `extentOffset` | `int` | The ending offset of the selection. |
| `isCollapsed` | `bool` | `True` if the selection is a collapsed cursor, meaning `baseOffset` and `extentOffset` are the same. |
| `isValid` | `bool` | `True` if the selection is valid. |
| `start` | `int` | The index of the first character in the selection. This is the minimum of `baseOffset` and `extentOffset`. |
| `end` | `int` | The index after the last character in the selection. This is the maximum of `baseOffset` and `extentOffset`. |
