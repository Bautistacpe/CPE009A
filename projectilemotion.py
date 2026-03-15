import math

print("Projectile Motion Solver")

horizontal_range = 0.0
max_height = 0.0
gravity = 9.8

def projectilemotion_solver(initial_velocity, angle):
    rad_angle = math.radians(angle)
    horizontal_range = ((initial_velocity**2)*(math.sin(2*rad_angle)))/gravity
    max_height = ((initial_velocity**2)*((math.sin(rad_angle))**2))/2*gravity
    return horizontal_range, max_height

initial_velocity = float(input("Enter the velocity of the object/person: "))
angle = float(input("Enter the angle of the object/person: "))

pm_range, pm_height = projectilemotion_solver(initial_velocity, angle)

print("The horizontal range of the object/person is:",pm_range)
print("The maximum height of the object/person is:",pm_height)


