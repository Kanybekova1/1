import random

def initialize_cargo():
    return [
        {"location": random.randint(1, 7), "weight": 200},
        {"location": random.randint(1, 7), "weight": 310},
        {"location": random.randint(1, 7), "weight": 203}
    ]

def move_cargo(cargo):
    for i in cargo:
        i["location"] = random.randint(1, 7)

def check_total_weight(found_cargo):
    total_weight = sum(i ["weight"] for i in found_cargo)
    return total_weight == 713

def main():
    cargo = initialize_cargo()
    found_cargo = []

    print("It is a program, which will help Martians find their Cargo!")
    print("Please input location coordinates to find the cargo (1-7).")

    while len(found_cargo) < 3:
        move_cargo(cargo)

        for i in range(3):
            location = int(input(f"Enter the location coordinate {i + 1}: "))
            for i in cargo:
                if i ["location"] == location:
                    print(f"Cargo found at location {location} with a weight of {i['weight']} units.")
                    found_cargo.append(i)
                    cargo.remove(i)
                    break

        if not check_total_weight(found_cargo):
            print("The total weight is not 713 units. Cargo will be relocated.")
            found_cargo = []
            cargo = initialize_cargo()

    print("Congratulations! All cargo has been located!")     

if __name__ == "__main__":
    main()
