class GardenError(Exception):
    pass

class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super.__init__(self, message)
        print("Caught PlantError: ")


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super.__init__(self, message)
        print("Caught WaterError: ")


def main() -> None:
    try:
        print("Testing PlantError...")
        plant = "tomato"
        raise PlantError("The {plant} is wilting!")
    except PlantError:
        pass
    water_level = 5
    try:
        print("Testing WaterError...")
        if water_level < 10:
            raise WaterError()
    except WaterError as e:
        print("Caught WaterError: {e}")
    print("Testing catching all garden errors")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    main()
