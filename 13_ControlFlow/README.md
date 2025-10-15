## Control Flow

### Overview

The goal of this assignment is to generate code for expressions involving variable [control flow](https://en.wikipedia.org/wiki/Control_flow).

Variable control flow is characterized by the presence of branches in a program: instructions that can modify the program counter (PC).

In this exercise, we use a subset of RISC-V instructions, including all instructions from the previous lab, plus two new branch instructions:

- ``beq rs1 rs2 lab``: sets ``PC = lab`` if ``rs1 == rs2``; otherwise, ``PC = PC + 1``.

- ``jal rd lab``: saves ``PC + 1`` in register ``rd`` and sets ``PC = lab``.

    - if ``rd = x0``, this behaves as an unconditional jump (``goto``) since writing to ``x0`` has no effect.

Note: For simplicity, we adopt absolute jump semantics. Unlike standard RISC-V, the ``lab`` parameter is treated as an absolute PC value, not a relative offset.

---
### Asm.py and Program Methods

This VPL comes with an updated Asm.py, which includes the new instructions and adds methods to the ``Program`` class:

- ``get_number_of_instructions()`` → returns the number of instructions currently stored.

- ``get_pc()`` → returns the current program counter.

- ``set_pc(value)`` → sets a new program counter value.

The last two methods are used internally by ``beq`` and ``jal``.
The first method, ``get_number_of_instructions()``, is useful for computing branch targets.

Example pattern for implementing a forward conditional branch:

```Python
# Evaluate an expression and store its value in v
v = exp.accept(gen, prog)

# If v is zero, jump to target (to be determined)
beq = AsmModule.Beq(v, "x0")
prog.add_inst(beq)

# Add more instructions
prog.add_inst(AsmModule.sub(...))
prog.add_inst(AsmModule.add(...))
...
prog.add_inst(AsmModule.mul(...))

# Determine branch target
beq.set_target(prog.get_number_of_instructions())
```

---
### Expressions with Variable Control Flow

You must extend the RenameVisitor and GenVisitor classes (in Visitor.py) to handle three new expressions:

- ``exp1 and exp2`` → returns ``false`` if ``exp1`` is false, otherwise evaluates ``exp2``.

- ``exp1 or exp2`` → returns ``true`` if ``exp1`` is true, otherwise evaluates ``exp2``.

- ``if exp0 then exp1 else exp2`` → evaluates ``exp1`` if ``exp0`` is true, else evaluates ``exp2``.

These expressions involve variable control flow.
The ``and`` and ``or`` expressions implement short-circuit semantics. For example:

```sml
false and ((1 / 0) < 0)   # evaluates to false (0)
```

- Division by zero is never evaluated.

- Boolean values in assembly are represented as integers: ``0 = false``, ``1 = true``.

Do not assume that variable names are unique.
The driver automatically uses ``RenameVisitor`` to enforce Static Single Assignment (SSA) before code generation.

---
### Submission and Testing

This assignment builds on VPL 12.

Do not modify ``Asm.py``, ``driver.py``, or ``Expression.py``.

To test your implementation locally, run:

```Bash
python3 driver.py
```

Example program:

```sml
true and false
# Press CTRL+D
```

Expected output:
```Bash
0
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