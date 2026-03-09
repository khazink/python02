class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant: str) -> None:
        message = f"The {plant} is wilting!"
        super().__init__(message)
        self.message = message


class WaterError(GardenError):
    def __init__(self) -> None:
        message = "Not enough water in the tank!"
        super().__init__(message)
        self.message = message


def main() -> None:
    try:
        print("Testing PlantError...")
        raise PlantError("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print()
    try:
        print("Testing WaterError...")
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    finally:
        print()
    print("Testing catching all garden errors")
    try:
        raise PlantError("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("All custom error type works correctly")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    main()
