from projectilemotion import projectilemotion_solver, initial_velocity, angle

pm_range, pm_height = projectilemotion_solver(initial_velocity, angle)

print("The horizontal range of the object/person is:",pm_range)
print("The maximum height of the object/person is:",pm_height)