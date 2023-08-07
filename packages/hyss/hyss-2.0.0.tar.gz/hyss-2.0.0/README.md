# Hyss - High Ympact Style Sheets

## Rationale

Define styles as python dicts! 
All of the power of python, realised to create stylesheets.
Coming soon to a package index near you!

## Features

- Create minified css content from a nested dictionary structure

- Helper for compound css classes (think 'div p', 'main section')  


## Potential Future Features

- Generate helpers for various css features. Already exist for animations.

- Build an indenter for output css; ease of debugging for users

- Means to convert 

## Usage Demonstrations

Here is a set of examples to illustrate the behaviour of functions within 
hyss

**stylesheet(styles: dict) -> str**

Takes a fractal dictionary structure and generates a minified css string as
shown

```python
from hyss import stylesheet

css = stylesheet(
        {
            'body': {
                'background-color': 'yellow',
            }, 
            'div': {
                'color': 'red'
            }
        }

print(css)

# This prints the following

# "body{background-color:yellow;}div{color:red;}"
```

**with_linebreaks(css: str) -> str**

Applies linebreaks to a minified css string, for debugging purposes as shown

```python

from hyss.format import with_linebreaks

minified_css = "body{background-color:yellow;}div{color:red;}"

linebreak_css = with_linebreaks(minified_css)

print(linebreaks_css)

# This prints "body{\nbackground-color:yellow;\n}\ndiv{\ncolor:red;\n}\n"

```

In a file, *linebreak_css* will look as follows

```css

body{
background-color:yellow;
}
div{
color:red;
}

```

