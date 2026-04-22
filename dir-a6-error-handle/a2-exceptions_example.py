"""
Python Exception Handling Examples
Covers many built-in exception types with practical scenarios.
"""

import os
import json


def demonstrate_exceptions():

    # ── 1. ZeroDivisionError ────────────────────────────────────────────────
    print("=== ZeroDivisionError ===")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"  Caught: {e}")

    # ── 2. TypeError ────────────────────────────────────────────────────────
    print("\n=== TypeError ===")
    try:
        result = "hello" + 42
    except TypeError as e:
        print(f"  Caught: {e}")

    # ── 3. ValueError ───────────────────────────────────────────────────────
    print("\n=== ValueError ===")
    try:
        number = int("not_a_number")
    except ValueError as e:
        print(f"  Caught: {e}")

    # ── 4. IndexError ───────────────────────────────────────────────────────
    print("\n=== IndexError ===")
    try:
        items = [1, 2, 3]
        value = items[99]
    except IndexError as e:
        print(f"  Caught: {e}")

    # ── 5. KeyError ─────────────────────────────────────────────────────────
    print("\n=== KeyError ===")
    try:
        data = {"name": "Alice"}
        age = data["age"]
    except KeyError as e:
        print(f"  Caught: missing key {e}")

    # ── 6. AttributeError ───────────────────────────────────────────────────
    print("\n=== AttributeError ===")
    try:
        number = 42
        number.upper()          # integers have no .upper()
    except AttributeError as e:
        print(f"  Caught: {e}")

    # ── 7. NameError ────────────────────────────────────────────────────────
    print("\n=== NameError ===")
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"  Caught: {e}")

    # ── 8. FileNotFoundError ────────────────────────────────────────────────
    print("\n=== FileNotFoundError ===")
    try:
        with open("/nonexistent/path/file.txt") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"  Caught: {e}")

    # ── 9. PermissionError ──────────────────────────────────────────────────
    print("\n=== PermissionError ===")
    try:
        with open("/etc/shadow", "r") as f:   # root-only file
            content = f.read()
    except PermissionError as e:
        print(f"  Caught: {e}")
    except FileNotFoundError:
        print("  (file doesn't exist on this system — skipped)")

    # ── 10. IsADirectoryError ───────────────────────────────────────────────
    print("\n=== IsADirectoryError ===")
    try:
        with open("/tmp") as f:               # /tmp is a directory
            content = f.read()
    except IsADirectoryError as e:
        print(f"  Caught: {e}")

    # ── 11. OverflowError ───────────────────────────────────────────────────
    print("\n=== OverflowError ===")
    try:
        import math
        result = math.exp(100_000)            # exceeds float range
    except OverflowError as e:
        print(f"  Caught: {e}")

    # ── 12. RecursionError ──────────────────────────────────────────────────
    print("\n=== RecursionError ===")
    def infinite_recurse():
        return infinite_recurse()
    try:
        infinite_recurse()
    except RecursionError as e:
        print(f"  Caught: {e}")

    # ── 13. StopIteration ───────────────────────────────────────────────────
    print("\n=== StopIteration ===")
    try:
        gen = iter([1, 2])
        next(gen)
        next(gen)
        next(gen)                             # exhausted
    except StopIteration as e:
        print(f"  Caught: iterator exhausted")

    # ── 14. NotImplementedError ─────────────────────────────────────────────
    print("\n=== NotImplementedError ===")
    class Shape:
        def area(self):
            raise NotImplementedError("Subclasses must implement area()")

    try:
        Shape().area()
    except NotImplementedError as e:
        print(f"  Caught: {e}")

    # ── 15. AssertionError ──────────────────────────────────────────────────
    print("\n=== AssertionError ===")
    try:
        x = -5
        assert x >= 0, f"Expected non-negative, got {x}"
    except AssertionError as e:
        print(f"  Caught: {e}")

    # ── 16. json.JSONDecodeError (subclass of ValueError) ───────────────────
    print("\n=== json.JSONDecodeError ===")
    try:
        json.loads("{bad json}")
    except json.JSONDecodeError as e:
        print(f"  Caught: {e.msg} at line {e.lineno}")

    # ── 17. UnicodeDecodeError ──────────────────────────────────────────────
    print("\n=== UnicodeDecodeError ===")
    try:
        bad_bytes = b"\xff\xfe invalid"
        bad_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        print(f"  Caught: {e.reason}")

    # ── 18. MemoryError (simulated) ─────────────────────────────────────────
    print("\n=== MemoryError (simulated) ===")
    try:
        raise MemoryError("Simulated: not enough memory")
    except MemoryError as e:
        print(f"  Caught: {e}")

    # ── 19. Custom Exception ────────────────────────────────────────────────
    print("\n=== Custom Exception ===")
    class InsufficientFundsError(Exception):
        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            super().__init__(
                f"Cannot withdraw {amount}; balance is only {balance}"
            )

    def withdraw(balance, amount):
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        return balance - amount

    try:
        withdraw(50, 200)
    except InsufficientFundsError as e:
        print(f"  Caught: {e}")

    # ── 20. Multiple except + else + finally ────────────────────────────────
    print("\n=== Multiple except + else + finally ===")
    def safe_divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("  except: division by zero")
        except TypeError:
            print("  except: invalid types")
        else:
            print(f"  else:   result = {result}")   # runs only if no exception
        finally:
            print("  finally: always runs")         # always runs

    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide("a", "b")

    # ── 21. Exception chaining (raise … from …) ─────────────────────────────
    print("\n=== Exception chaining (raise ... from ...) ===")
    try:
        try:
            int("bad")
        except ValueError as original:
            raise RuntimeError("Conversion failed") from original
    except RuntimeError as e:
        print(f"  Caught: {e}")
        print(f"  Caused by: {e.__cause__}")


if __name__ == "__main__":
    demonstrate_exceptions()
