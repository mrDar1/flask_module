"""The file covers all 7 sections — basic raise, re-raise,
custom exceptions, chaining, type conversion,
custom attributes, and a quick reference summary."""
# ============================================================
#         Python `raise` Statement - Complete Guide
# ============================================================


# ── 1. Basic raise ──────────────────────────────────────``─────
print("=" * 50)
print("1. Basic raise")
print("=" * 50)

def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")


# ── 2. Re-raise the current exception ────────────────────────
print("\n" + "=" * 50)
print("2. Re-raise with bare `raise`")
print("=" * 50)

def risky():
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Logging the error...")
        raise  # Re-raises ZeroDivisionError

try:
    risky()
except ZeroDivisionError as e:
    print(f"Caught re-raised exception: {e}")


# ── 3. Custom exception ───────────────────────────────────────
print("\n" + "=" * 50)
print("3. Custom Exception")
print("=" * 50)

class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if balance < amount:
        raise InsufficientFundsError("Not enough funds!")
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(f"Caught: {e}")


# ── 4. Exception chaining (raise ... from ...) ────────────────
print("\n" + "=" * 50)
print("4. Exception Chaining (raise from)")
print("=" * 50)

try:
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("Conversion failed") from e
except RuntimeError as e:
    print(f"Caught: {e}")
    print(f"Original cause: {e.__cause__}")


# ── 5. Convert exception type ─────────────────────────────────
print("\n" + "=" * 50)
print("5. Convert Exception Type")
print("=" * 50)

try:
    try:
        open("missing_file.txt")
    except FileNotFoundError:
        raise RuntimeError("Config file is missing!")
except RuntimeError as e:
    print(f"Caught: {e}")


# ── 6. Custom exception with extra attributes ─────────────────
print("\n" + "=" * 50)
print("6. Custom Exception with Attributes")
print("=" * 50)

class AppError(Exception):
    """Base class for app errors"""
    pass

class DatabaseError(AppError):
    def __init__(self, message, query=None):
        super().__init__(message)
        self.query = query

try:
    raise DatabaseError("Connection failed", query="SELECT *")
except DatabaseError as e:
    print(f"Error   : {e}")
    print(f"Query   : {e.query}")


# ── 7. raise vs raise Exception vs raise Exception from e ─────
print("\n" + "=" * 50)
print("7. Quick Reference Summary")
print("=" * 50)

summary = """
| Syntax                        | Behavior                                      |
|-------------------------------|-----------------------------------------------|
| raise                         | Re-raises the current active exception        |
| raise ValueError("msg")       | Raises a new exception                        |
| raise RuntimeError("m") from e| Raises new exception, chains original as cause|
"""
print(summary)
