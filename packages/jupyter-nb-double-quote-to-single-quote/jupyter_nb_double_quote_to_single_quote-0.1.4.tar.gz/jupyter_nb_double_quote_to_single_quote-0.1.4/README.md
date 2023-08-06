# jupyter-nb-double-quote-to-single-quote

Convert double quotes ("") to single quotes ('') in Jupyter notebook code cells

## Installation

```bash
pip install jupyter-nb-double-quote-to-single-quote
```

## As a command line tool

```bash
jupyter-nb-double-quote-to-single-quote my_notebook.ipynb
```
Use `--help` to see documentations of command line arguments.

### As a pre-commit hook

Put the following into your `.pre-commit-config.yaml` file. Remember to replace `<VERSION>` with your version of this tool (such as `v0.1.0`):
```yaml
-   repo: https://github.com/cyyc1/jupyter-nb-double-quote-to-single-quote
    rev: <VERSION>
    hooks:
    -   id: jupyter-nb-double-quote-to-single-quote
```
See [pre-commit](https://github.com/pre-commit/pre-commit) for more instructions.

### Licenses

The license of this tool is MIT License.  See the file `LICENSE`

A significant portion of the code used in this tool comes from https://github.com/pre-commit/pre-commit-hooks, in particular, the file [`string_fixer.py`](https://github.com/pre-commit/pre-commit-hooks/blob/6b03546fc3082141db46b5146a1f1c4fc011f96f/pre_commit_hooks/string_fixer.py).  As such, we added pre-commit-hooks' license as the original license (see the file `ORIGINAL_LICENSE`).
