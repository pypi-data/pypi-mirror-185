## Overview

Colorout is a simple tool to color your console using *ANSI Escape Codes*. It 
consists of using interpolated colored strings for ease of use and not polluting 
your code with reset escapes.

Use the `%` operator to link your text, e.g.:

```py
coloredstr = colorout.fg((0, 255, 0)) % "This is green!"
```

*Note: ``colorout.fg`` is an alias for ``colorout.dye``, use `help(colorout.dye)` to learn more.*

## Support on Windows

Colorout is fully compatible with Windows 10+ and has been successfully tested on
Windows Terminal *(default)*, PowerShell and
[Windows Terminal App](https://www.microsoft.com/store/productId/9N0DX20HK701).

> To use it in previous versions, it may be necessary to use dependencies that
> allow use of ANSI Escape Sequence in terminal, e.g.
> [ANSICON](https://github.com/adoxa/ansicon).
