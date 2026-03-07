def check_temperature(temp_str: str) -> int:
    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")
        return
    if (0 < temp_int < 40):
        print(f"Temperature {temp_int}\u00b0C is perfect for plants!\n")
        return temp_int
    elif (temp_int < 0):
        print(f"Error: {temp_str}\u00b0C is too cold for plants "
              "(min 0\u00b0C)\n")
    elif (temp_int > 40):
        print(f"Error: {temp_str}\u00b0C is too hot for plants "
              "(max 40\u00b0C)\n")
    return


def test_temperature_input() -> None:
    values = ['25', 'abc', '100', '-50']
    for value in values:
        print(f"Testing temperature: {value}")
        check_temperature(value)


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()


if __name__ == "__main__":
    main()
