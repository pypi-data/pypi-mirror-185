# teX2svg

```bash
pip install tex4svg
```

A simple python module to renders LaTeX snippets to SVG text.

```python
from tex4svg import tex2svg

# for "inline mode" LaTeX
svg = tex2svg(tex)
svg = tex2svg(tex, mode="inline")       # by default

# for "block" LaTeX
svg = tex2svg(tex, mode="block")
```

Depends on `pdflatex`, `pdfcrop`, `pdf2svg`. On Arch Linux, you can install these with:

```bash
sudo pacman -S pdf2svg texlive-most
```
