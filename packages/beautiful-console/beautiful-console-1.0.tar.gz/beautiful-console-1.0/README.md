# Beautiful Console

## Installation

### Install

```bash
pip install beautiful-console
```

### Import

```python
from beautiful_console import beautiful_console as bc
```

## Defined Colors

>black, red, green, yellow, blue, magenta, cyan, white

## Defined Styles

>**bold**, _italic_, underline, underline_bold, overline, ~~strikethrough~~

<br>

## beautiful_console() Parameters

```python
# Only the text-parameter is required, then you can use any option you need.

"""
text: A text.
text_color: Color of the text.
text_style: Style of the text.
text_highlight_color: Color of the text background.
text_blink: Blinking the text <True or False>.
continuous_color: Color of continuous text (when typing input).
continuous_style: Style of continuous text.
continuous_highlight_color: Color of continuous text background.
continuous_blink: Blinking continuous text <True or False>.
text_color_degree: Intensity of the text color <0 or 1>
text_highlight_color_degree: Intensity of text background color <0 or 1>
continuous_color_degree: Intensity of continuous text color <0 or 1>
continuous_highlight_color_degree: Intensity of continuous text background color <0 or 1>
get_input: To use continuous text options it must be True, then beautiful_console() handle a input-function and returns input value.
"""
```

## Tips

>**Tip** : Some things may not work on some consoles.

>**Tip** : get_input can only be filled as a keyword argument (get_input=True).
---
