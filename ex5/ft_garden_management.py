class GardenError(Exception):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name) -> None:
        try:
            if not plant_name:
                raise ValueError("Plant name cannot be empty!")
        except ValueError as e:
            print(f"Error adding plant: {e}")
        else:
            self.plants.append(plant_name)
            print(f"Adding {plant_name} successfully")

    def water_plant(self) -> None:
        print("Opening watering system")
        try:
            if self.plants is None:
                raise ValueError("Plant is empty")
        except ValueError:
            print("Error: Cannot water None - invalid plant!")
        else:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system(cleanup)")


    def check_plant_health(plant_name: str, water_level: int, 
                       sunlight_hours: int) -> None:
        try:
            if plant_name == None:
                raise ValueError("Plant name cannot be empty!")
            elif water_level < 1:
                raise ValueError(f"Water level {water_level} too low (min 1)")
            elif water_level > 10:
                raise ValueError(f"Water level {water_level} too high (max 10)")
            elif sunlight_hours < 2:
                raise ValueError(f"Sunlight hour {sunlight_hours} is too low (min 2)")
            elif sunlight_hours > 12:
                raise ValueError(f"Sunlight hour {sunlight_hours} "
                            "is too high (max 12)")
            else:
                print(f"{plant_name}: healthy (water:{water_level},"
                    f" sun: {sunlight_hours}")
        except ValueError as e:
            print(f"Error: {e}")

    def check_water_level(self, water_tank: int) -> None:
        try:
            if water_tank <= 0:
                raise GardenError
        except GardenError as e:
            print("Caught GardenError: Not enough water in tank")
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("Adding plants to garden...")
    garden = GardenManager()
    mygarden_list = ["tomato", "lettuce", ""]
    for mygarden in mygarden_list:
        garden.add_plant(mygarden)
    print()
    garden.water_plant()
    print()
    


if __name__ == "__main__":
    test_garden_management()