# FAQ

## eval-sh does not work for Windows

POSIX shell is not installed in Windows by default. See
[evaluate cmd](resources/config.md#evaluate-cmd) or
[install a POSIX shell](https://www.msys2.org)

## Why not Makefile

Save your time to write Makefile.

## Why this name

Comes from `eval-rst` of
[MyST](https://myst-parser.readthedocs.io/en/latest/faq/index.html#include-rst-files-into-a-markdown-file).

## What is translate shell

[My another project](https://pypi.org/project/translate-shell). The intention
of this project is to serve its document generation.

## Eval is evil

I don't guarantee any consequence like:

```sh
rm -rf your_import_file
```

## Difference from other projects

- [sphinx-execute-code](https://pypi.org/project/sphinx-execute-code) Display
  code execute result in a code fence, not inject generated markdown/rst to the
  source code.
- [sphinxcontrib-programoutput](https://pypi.org/project/sphinxcontrib-programoutput)
  Same as above.
