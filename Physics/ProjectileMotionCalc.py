import math
import matplotlib

matplotlib.use("QtAgg")

import matplotlib.pyplot as plt

#define get_value
def get_value(question):
    while True:
        answer = input(question).strip()
        try:
            ans = float(answer)
            if ans < 0:
                print("Please enter a valid number")
            else:
                return ans
        except ValueError:
            print("Please enter a valid number")

#get variables
velocity = get_value("What is your velocity?: ")
angle = get_value("What is your angle to the horizontal?: ")
g = 9.81

#Calculations
angle_rad = math.radians(angle)
h_comp = velocity * math.cos(angle_rad)
v_comp = velocity * math.sin(angle_rad)
final_velocity = -1 * (v_comp)
initial_velocity = 1 * (v_comp)
max_height = (v_comp ** 2) / (2 * g)
flight_time = (final_velocity - initial_velocity) /(-g)
horizontal_range = h_comp * flight_time

#display calculated values
print(f"Horizontal Component: {round(h_comp, 2)} m/s")
print(f"Vertical Component: {round(v_comp, 2)} m/s")
print(f"Max Height: {round(max_height, 2)} m")
print(f"Time of flight: {round(flight_time, 2)} s")
print(f"horizontal_range: {round(horizontal_range, 2)} m")

#measure distance travelled by each second
horizontal_positions = []
vertical_positions = []
print("Distance travelled by each second:")
for time in range(int(flight_time * 10) + 1):
    vert_distance_travelled = (v_comp * time/10) + (0.5 * (-g * ((time/10) ** 2)))
    horz_distance_travelled = (h_comp * time/10)
    horizontal_positions.append(horz_distance_travelled)
    vertical_positions.append(vert_distance_travelled)
    print(f"{time/10}s:({round(horz_distance_travelled, 2)}, {round(vert_distance_travelled, 2)})")
horizontal_positions.append(horizontal_range)
vertical_positions.append(0)
max_height_b = max(vertical_positions)
max_height_index = vertical_positions.index(max_height_b)
max_height_horz = horizontal_positions[max_height_index]
print(f"{round(flight_time, 2)}s:({round(horizontal_range, 2)}, 0.0)")
print(f"Horizontal Positions: { [round(pos, 2) for pos in horizontal_positions] }")
print(f"Vertical Positions: { [round(pos, 2) for pos in vertical_positions] }")
print(f"Max Height: ({round(max_height_horz, 2)}, {round(max_height_b, 2)})")

plt.plot(
    horizontal_positions,
    vertical_positions,
    color="cyan",
    marker="o",
    markerfacecolor="pink",
    markeredgecolor="black"
)
plt.xlim(0, max(horizontal_positions))
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Projectile Motion")
plt.grid(True)
plt.axhline(y=0, color='black', linewidth=2, linestyle='--')

plt.show()