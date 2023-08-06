# Config

You can override the default `eval_funcs` in your `docs/conf.py`:

## Only evaluate shell

```python
from sphinxcontrib.eval import eval_sh

eval_funcs = {"sh": eval_sh}
```

## Evaluate shell, python, vim script

```python
from sphinxcontrib.eval import eval_sh, eval_python
from subprocess import check_output


def eval_vim(input: str) -> str:
    try:
        output = check_output(  # nosec B603
            ["nvim", "--headless", "-c", input, "-c", "q"],
            universal_newlines=True,
        )
    except Exception:
        output = ""
    return output


eval_funcs = {"sh": eval_sh, "python": eval_python, "vim": eval_vim}
```

## Evaluate cmd

```python
def eval_cmd(input: str) -> str:
    try:
        output = check_output(  # nosec B603
            ["cmd", "/c", input], universal_newlines=True
        )
    except Exception:
        output = ""
    return output


eval_funcs = {"cmd": eval_cmd}
```
