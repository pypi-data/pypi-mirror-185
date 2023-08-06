# click-lazy

$ click_lazy

Click lazy is an extention for [click](https://palletsprojects.com/p/click).

Click lazy allow you to separate set of commands in file and import it only if necessary.

## A Simple Example

```python
from click_lazy import LazyGroup

...

if __name__ == '__main__':
    # This group of commands will import group_heavy only if needed
    cli.add_command(LazyGroup(name='heavy', import_name='group_heavy:cli'))

    cli()
```

group_heavy.py

```python
import click


@click.group()
def cli():
    """Havy script"""


@cli.command(name='heavy_cmd')
def run_heavy_cmd():
    print('Running command from heavy group file')
```

[See complete example on github](https://github.com/nagolos/click-lazy/tree/main/examples)

## Links

- [click-lazy on PyPi](https://pypi.org/project/click-lazy/)
- [click-lazy source code](https://github.com/nagolos/click-lazy)
- [click documentation](https://click.palletsprojects.com/)