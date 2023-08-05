# Tiptapy

### Library that generates HTML output from JSON export of tiptap editor

![tiptapy](https://github.com/scrolltech/tiptapy/workflows/tiptapy/badge.svg)

> This is a forked version of [stckme/tiptapy](https://github.com/stckme/tiptapy) by Shekhar Tiwatne. This version includes camel case support for newer tiptap versions. Please consider using the original project in your projects.

### Install

```bash
pip install cfm-tiptapy
```

### Test

```bash
python -m pytest
```

### Usage

```{.sourceCode .python}
import tiptapy

s = """

{
  "type": "doc",
  "content": [
    {
      "type": "blockquote",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Readability counts."
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "marks": [
                {
                  "type": "link",
                  "attrs": { "href": "https://en.wikipedia.org/wiki/Zen_of_Python" }
                }
              ],
              "text": "Zen of Python"
            },
            {
              "type": "text", "text": " By "
            },
            {
              "type": "text",
              "marks": [
                {
                  "type": "bold"
                }
              ],
              "text": "Tom Peters"
            }
          ]
        }
      ]
    }
  ]
}
"""

class config:
    """
    Config class to store constants used by the other nodes.
    """
    DOMAIN = "python.org"


renderer = tiptapy.BaseDoc(config)
out = renderer.render(s)
print(out)
```

#### Output

```{.sourceCode .html}
<blockquote>
  <p>Readability counts.</p>
  <p>
      <a href="https://en.wikipedia.org/wiki/Zen_of_Python">Zen of Python</a> By
      <strong>Tom Peters</strong>
  </p>
</blockquote>
```
