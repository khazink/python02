def test_error_types() -> None:
    errors = ["value_error", "zero_division_error", "file_not_found_error",
              "key_error"]
    for error in errors:
        try:
            garden_operation(error)
        except ValueError:
            print("Caught ValueError: invalid literal for int()")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: no such file 'missing.txt'")
        except KeyError:
            print("Caught KeyError: 'missing\\_plant'")
        finally:
            print()
    try:
        garden_operation("multiple_error")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
        print()
    print("All error types tested succesfully")


def garden_operation(error: list) -> None:
    if error == "value_error":
        print("Testing ValueError...")
        int("abc")
    elif error == "zero_division_error":
        print("Testing ZeroDivisionError...")
        8 / 0
    elif error == "file_not_found_error":
        print("Testing FileNotFoundError...")
        open("missing.txt")
    elif error == "key_error":
        print("Testing KeyError...")
        user = {"name": "Siti"}
        _ = user["age"]
    elif error == "multiple_error":
        print("Testing Multiple Error together...")
        int("abc")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
