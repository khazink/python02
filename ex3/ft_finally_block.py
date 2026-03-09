class InvalidPlant(Exception):
    pass


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant != None:
                print(f"Watering {plant}")
            else:
                raise InvalidPlant
    except InvalidPlant:
        print("Error: Cannot water None - invalid plant!")
    finally:
        print("Closing watering system(cleanup)")
    print("Watering completed successfully")


def test_watering_system() -> None:
    print("Testing normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Testing with error...")
    plant_list = ["tomato", None, "Mandrake"]
    water_plants(plant_list)
    print("Cleanup always happen, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    