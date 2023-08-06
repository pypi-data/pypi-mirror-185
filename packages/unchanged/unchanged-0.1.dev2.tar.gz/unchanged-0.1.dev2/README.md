# Unchanged

A simple approvals/snapshot/golden master library that lets you configure your testing tools any way you want.  

## Features
 
  - **Sensible defaults**: Just want to do some basic snapshot on most Python objects?  Go for it.  Snapshot testing should be easy.
  - **Highly Modular**: Want to do fuzzy comparison, pre-check file scrubbing, have the diff display in a non-Python program, and use the latest test runner?  No problem, plug your tools and functions into `unchanged` based on your own preferences and project needs.  
  - **No External Dependencies**: `unchanged`'s internals are stupidly simple, using only the Python standard library--you decide what packages your tests will rely on, not us.
  

## Installation

```bash
pip install unchanged
```

## Example Usage

```python
from unchanged import verify
```

### Hello world is still "Hello world"
```python
from unchanged import verify

verify("Hello, world", path="greeting.txt")
```

### Use Git Diff to Compare files

With `subprocess`:

```python
from unchanged import Verifier
from subprocess import Popen

verify = Verifier(show_diffs=lambda f1, f2: Popen(['git' ,'diff', '--no-index', f1, f2]))
verify("Hello, world", path='greeting.txt')
```

With the `unchanged.Program` utility:
```python
from unchanged import Verifier, Program

verify = Verifier(show_diffs=Program(['git' ,'diff', '--no-index']))
verity("Hello world")
```

### Use NBDime to Compare Jupyter Notebooks
```python
from unchanged import Verifier
from subprocess import Popen

notebooks_match = lambda f1, f2: Popen(['nbdime', 'diff', '--ignore-metadata', f1, f2]).stdout.read() == ''
show_notebook_diff = lambda f1, f2: Popen(['nbdime', 'diff-web'])

verify_notebook = Verifier(show_diffs=Program(['nbdime', 'diff-web']), files_match=notebooks_match)


```

### Use BeyondCompare 3 to Display Diffs
```python
from unchanged import Verifier
from subprocess import Popen

path_to_bc3 = "{ProgramFiles}/Beyond Compare 4/BCompare.exe"
show_diff_in_BC3 = lambda f1, f2: Popen([path_to_bc3])

verify = Verifier(show_diffs=show_diff_in_BC3)
```


### Check Matplotlib Plots, Displaying Diffs in VSCode

```
from unchanged import Verifier
from subprocess import Popen
```