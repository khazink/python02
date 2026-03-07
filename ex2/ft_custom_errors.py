class GardenError(Exception):
    def __init__(self, message: str) -> str:
        super().__init__(message)


class PlantError(GardenError):
    print("Caught PlantError: The tomato plant is wilting!")


class WaterError(GardenError):
    print("Caught WaterError: Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")



if __name__ == "__main__":
    main()
