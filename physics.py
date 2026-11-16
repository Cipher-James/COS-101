def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid Input! ')


def density(mass, volume):
    return mass / volume



def frequency(time):
    return 1 / time



def wave_speed(frequency, wavelength):
    return frequency * wavelength


def electrical_power(voltage, current):
    return voltage * current



def gravitational_force(m1, m2, distance):
    G = 6.674 * (10 ** -11)
    return (G * m1 * m2) / (distance ** 2)

while True :

    print("PHYSICS CALCULATOR")
    print("1. Density")
    print("2. Frequency")
    print("3. Wave Speed")
    print("4. Electrical Power")
    print("5. Gravitational Force")
    print("6.Exit")

    choice = int(input("Choose a formula (1-5): "))

    if choice == 1:
        m = float(input("Enter mass (kg): "))
        v = float(input("Enter volume (m3): "))

        if v > 0:
            print("Density =", density(m, v), "kg/m3")
        else:
            print("Volume must be greater than zero.")

    elif choice == 2:
        t = float(input("Enter time period (seconds): "))

        if t > 0:
            print("Frequency =", frequency(t), "Hz")
        else:
            print("Time must be greater than zero.")

    elif choice == 3:
        f = float(input("Enter frequency (Hz): "))
        w = float(input("Enter wavelength (m): "))

        print("Wave Speed =", wave_speed(f, w), "m/s")

    elif choice == 4:
        v = float(input("Enter voltage (V): "))
        i = float(input("Enter current (A): "))

        print("Electrical Power =", electrical_power(v, i), "Watts")

    elif choice == 5:
        m1 = float(input("Enter first mass (kg): "))
        m2 = float(input("Enter second mass (kg): "))
        r = float(input("Enter distance between masses (m): "))

        if r > 0:
            print("Gravitational Force =", gravitational_force(m1, m2, r), "N")
        else:
            print("Distance must be greater than zero.")

    else:
        print("Invalid choice. Select between 1 and 6.")
