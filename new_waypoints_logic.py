# upon receiving error notice that cost is too high

room_coordinates = [
    [1, 1, 4, 4],  # x coordinates
    [1, 3, 3, 1]   # y coordinates
]

ytop = room_coordinates[1][0]
ybottom = room_coordinates[1][1]

w = 1 # robot width

novalidroute = 0 # get from ros2

current_y_pos = 5 # get this from ros2
current_waypoint = [1, 0] #need to get this from ros2 somehow
x = current_waypoint[0]
y_waypoint = current_waypoint[1]
y = current_y_pos


waypoints = [
    [0, 0], [0, 10], [1, 10], [1, 0],
    [2, 0], [2, 10], [3, 10], [3, 0], 
    [4, 0], [4, 10], [5, 10], [5, 0], 
    [6, 0], [6, 10], [7, 10], [7, 0], 
    [8, 0],[8, 10]
] # get this from waypoint generation node

index = waypoints.index(current_waypoint)

i = 1

if y < y_waypoint: #traveling up
    while novalidroute == 1:
        new_waypoint = [x, y + i * w]
        waypoints.insert(index, new_waypoint)
        waypoints.pop[index]
        i += 1
else:
        new_waypoint = [x, y - i * w]
        waypoints.insert(index, new_waypoint)
        waypoints.pop[index]
        i += 1               
