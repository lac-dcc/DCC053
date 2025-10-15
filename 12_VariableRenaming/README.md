# Code for arithmetic expressions

### Overview
In the previous lab, we developed a code generator for a subset of [RISC-V](https://en.wikipedia.org/wiki/RISC-V) instructions.

That exercise had an important restriction: all let blocks were assumed to define variables with unique names.
For example, the following program was not valid, because the variable x is defined twice:

```sml
let x <- 1 in let x <- 2 in x end + x end
```

However, this restriction is artificial, since the program itself is perfectly valid. Its value is ``3``.

In this lab, we remove this restriction, allowing variable names to be reused in different ``let`` blocks.

Examples of valid programs:

```sml
let v <- 1 in let v <- 2 in v end + v end   # value = 3
let v <- 1 in let v <- 2 in let v <- 3 in v end + v end + v end  # value = 6
```

---
### Goal
You must ensure that variables are renamed before generating code, so that all variables in ``let`` blocks have unique names.

For instance, the first program above:
```sml
let v <- 1 in let v <- 2 in v end + v end
```
should be translated to instructions similar to:
```sml
v_0 = addi x0 1      -- Define v_0 with value 1
v_1 = addi x0 2      -- Define v_1 with value 2
v3 = add v_1 v_0     -- Define v3 as v_0 + v_1
```
This corresponds to the program:
```sml
let v_0 <- 1 in let v_1 <- 2 in v_1 end + v_0 end
```

---
### Implementation

To achieve this, you must implement a RenameVisitor class:

- Modifies expressions in place, ensuring all ``let`` blocks create variables with unique names.

- The ``visit`` methods do not need to return a value.

Example of a ``visit`` method:
```Python
def visit_eql(self, exp, name_map):
    exp.left.accept(self, name_map)
    exp.right.accept(self, name_map)
```

Usage:

```Python
def rename_variables(exp):
    ren = RenameVisitor()
    exp.accept(ren, {})
    return exp
```
This exercise effectively implements a [Static Single Assignment (SSA)](https://en.wikipedia.org/wiki/Static_single-assignment_form) property over the [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree).
Normally, SSA is applied at a lower-level representation (e.g., the [control-flow graph](https://en.wikipedia.org/wiki/Control-flow_graph)). Here, we ensure unique assignment at the AST level.

---
### Submission and Testing

This assignment builds on Lab 11.

The only extension is the implementation of ``RenameVisitor``.

You must **not** modify ``driver.py`` or ``Expression.py``or ``Asm.py``.

To test your implementation locally, run:

```Bash
python3 driver.py
```

Example program:

```sml
2 + 3
# Press CTRL+D
```

Expected output:
```Bash
5
```

Each file contains doctests that validate your implementation.
To run them, use:
```bash
python3 -m doctest filename.py
```

For example:

```bash
python3 -m doctest Visitor.py
```

If no errors appear, your implementation is (almost) complete.