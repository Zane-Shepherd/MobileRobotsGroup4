def blocked_path_waypoints(self, blocked, waypoint, pose, width):
    if blocked == True:
        x = pose.x
        y = pose.y
        new_waypoints = []
        new_waypoints.append([x,y])
        if y<waypoint[1]:
            while y<waypoint[1]:
                y += width
                new_waypoints.append([x,y])
        else:
            while y>waypoint[1]:
                y -= width
                new_waypoints.append([x,y])
    return new_waypoints