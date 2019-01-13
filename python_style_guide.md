# Python Style Guide   
(most of the following information is taken straight from [the almighty PEP8](https://www.python.org/dev/peps/pep-0008/))

## Indentation   

Use 4 spaces per indentation level.    

### Tabs or Spaces?
Spaces are the preferred indentation method.

Tabs should be used solely to remain consistent with code that is already indented with tabs.

Python 3 disallows mixing the use of tabs and spaces for indentation.

Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively.

When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code that illegally mixes tabs and spaces. When using -tt these warnings become errors. These options are highly recommended!

## Maximum Line Length

Limit all lines to a maximum of 79 characters.

## Should a Line Break Before or After a Binary Operator?

In short, do this ([check out the detailed reason why here](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)):    
```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

## Imports

Imports should usually be on separate lines:    

```
    import os
    import sys
```

Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

Imports should be grouped in the following order:

1. Standard library imports.
2. Related third party imports.
3. Local application/library specific imports.   

You should put a blank line between each group of imports.

When importing a class from a class-containing module, it's usually okay to spell this:

```
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

If this spelling causes local name clashes, then spell them explicitly:

```
import myclass
import foo.bar.yourclass
```

and use `myclass.MyClass` and `foo.bar.yourclass.YourClass`.

Wildcard imports (`from <module> import *`) should be avoided. 

## Module Level Dunder Names

Module level "dunders" (i.e. names with two leading and two trailing underscores) such as `__all__`, `__author__`, `__version__`, etc. should be placed after the module docstring but before any import statements except `from __future__` imports. Python mandates that future-imports must appear in the module before any other code except docstrings:

```
"""This is the example module.

This module does stuff.
"""


from __future__ import barry_as_FLUFL

__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Cardinal Biggles'

import os
import sys
```

## Naming things

[We fully recommend reading the full length of PEP8 for this one.](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

