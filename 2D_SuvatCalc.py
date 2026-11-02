def get_value(question):
    while True:
        answer = input(question).strip()
        if answer == '?':
            return None
        try:
            return float(answer)
        except ValueError:
            print("Please enter a valid number or '?'")

def calculate_final_velocity(values):
    s, u, v, a, t = values
    if v is None and u is not None and a is not None and t is not None:
        values[2] = u + a * t
    return values[2]

def calculate_initial_velocity(values):
    s, u, v, a, t = values
    if u is None and v is not None and a is not None and t is not None:
        values[1] = v - a * t
    return values[1]

def calculate_time(values):
    s, u, v, a, t = values
    if t is None and v is not None and a is not None and u is not None:
        if a != 0:
            values[4] = (v - u) / a
    return values[4]

def calculate_displacement(values):
    s, u, v, a, t = values
    if s is None:
        if u is not None and t is not None and a is not None:
            values[0] = u * t + 0.5 * a * (t ** 2)
        elif u is not None and v is not None and t is not None:
            values[0] = 0.5 * (u + v) * t
    return values[0]

while True:
    print("\n--- New Kinematics Calculation ---")
    print("Enter numerical values, or '?' if the value is unknown.")


    vert_displacement     = get_value("What is your vertical displacement (s)? ")
    vert_initial_velocity = get_value("What is your vertical initial velocity (u)? ")
    vert_final_velocity   = get_value("What is your vertical final velocity (v)? ")
    vert_acceleration     = -9.81
    time                  = get_value("What is your time (t)? ")

    vert_values = [vert_displacement, vert_initial_velocity, vert_final_velocity, float(vert_acceleration), time]

    horz_displacement     = get_value("What is your (horizontal) displacement (s)? ")
    horz_initial_velocity = get_value("What is your (horizontal) initial velocity (u)? ")
    horz_final_velocity   = horz_initial_velocity
    horz_acceleration     = 0.0

    horz_values = [horz_displacement, horz_initial_velocity, horz_final_velocity, float(horz_acceleration), time]

    vert_values[2] = calculate_final_velocity(vert_values)
    vert_values[1] = calculate_initial_velocity(vert_values)
    vert_values[4] = calculate_time(vert_values)
    vert_values[0] = calculate_displacement(vert_values)

    if horz_values[4] is None and vert_values[4] is not None:
        horz_values[4] = vert_values[4]

    horz_values[0] = calculate_displacement(horz_values)
    labels = ["Displacement (s)", "Initial Velocity (u)", "Final Velocity (v)", "Acceleration (a)", "Time (t)"]

    print("\nVertical Values:")
    for label, val in zip(labels, vert_values):
        print(f"  {label}: {val}")

    print("\nHorizontal Values:")
    for label, val in zip(labels, horz_values):
        print(f"  {label}: {val}")

    break