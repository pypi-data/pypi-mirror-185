# Lamarkdown

Command-line markdown document compiler based on Python-Markdown.

The intent is to provide a tool comparable to Latex, but with the Markdown and HTML formats in
place of Latex and PDF. Lamarkdown is _not_ a drop-in replacement for Latex, but it attempts to
address the same document-preparation use case. To this end, Lamarkdown:

* Is a locally-run, command-line tool.
* Builds a complete HTML document, where the author has complete control over the appearance
    (though making it easy to produce something that _looks_ more like a document than a webpage).
* Builds an entirely _self-contained_ HTML document (except where you insert external references
    yourself), which can be stored and distributed as a standalone file.
    * (Also currently with the exception of fonts, which are, for now, declared as links to `fonts.googleapis.com`.)
* Allows embedding of Latex environments (or entire Latex documents), with the resulting output converted
    to SVG format and embedded within the HTML.

Further goals of the project (sometimes also associated with Latex document preparation) are to:

* Provide a live-updating feature to improve editing productivity. When enabled, the markdown file
    is automatically re-compiled, and the HTML document auto-reloaded, when changes are detected.
* Provide a scheme for compiling multiple variants of a single source document.


## Requirements and Installation

Lamarkdown depends on Python 3.7+. To install via pip:

`$ pip install lamarkdown`

This will resolve dependencies on other PyPi packages (including "markdown", others).

However, to embed Latex code, you need to a Latex distribution (e.g., Texlive), which must be 
installed separately. The actual commands are configurable. By default, Lamarkdown's Latex 
extension runs 'xelatex' and 'dvisvgm'.


## Basic usage

To compile `mydocument.md` into `mydocument.html`, just run:

`$ lamd mydocument.md`

(Or `lamd.py` if appropriate.)

You can enable the live-update mode using `-l`/`--live`:

`$ lamd -l mydoc.md`

This will launch a local web-server and a web-browser, and will keep `mydoc.html` in sync with any
changes made to `mydoc.md`, until you press Ctrl+C in the terminal.


## Wiki

For detailed documentation, see [the wiki](https://bitbucket.org/cooperdja/lamarkdown/wiki/).
