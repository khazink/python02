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
            print(f"Plant {plant_name} is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("tomato", 5, 8)
    print()
    print("Testing empty plant name...")
    check_plant_health(None, 4, 7)
    print()
    print("Testing bad water level...")
    check_plant_health("Seaweed", 15, 3)
    print()
    print("Testing bad sunlight hour...")
    check_plant_health("Cotton", 5, 0)
    print()
    print("All error raising tests completed!")

    
if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()