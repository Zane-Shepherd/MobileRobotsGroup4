import rclpy
from rclpy.node import Node


class WaypointGenerator(Node):
    def __init__(self):
        super().__init__('waypoint_generator')

        # room_coordinates is a 2x4 array: 1 is top left, 2 is bottom left, 3 is bottom right, 4 is top right
        # [x1, x2, x3, x4]
        # [y1, y2, y3, y4]
        
        # w = robot width

                        
        # for i, wp in enumerate(self.waypoints):
        #     self.get_logger().info(f"Waypoint {i}: x={wp[0]:.2f}, y={wp[1]:.2f}")
            
    def generate_waypoints(self, room_coordinates, w):
        
        # Extract room bounds
        xleft = room_coordinates[0][0]
        xright = room_coordinates[0][1]
        ybottom = room_coordinates[1][0]
        ytop = room_coordinates[1][1]
    
        x = xleft + w / 2
        y = ybottom + w / 2
    
        index = 0
        waypoints = []
    
        while x < xright - w / 2:
            waypoints.append([x,y])
            
            if index % 2 == 1:
                x += w
            else:
                if y == ybottom + w / 2:
                    y = ytop - w / 2
                elif y == ytop - w / 2:
                    y = ybottom + w / 2
            index += 1
        
        waypoints.append([xright - w / 2, y])
        index += 1
        
        if y == ybottom + w / 2:
            y = ytop - w / 2
        elif y == ytop - w / 2:
            y = ybottom + w / 2
            
        waypoints.append([xright - w / 2, y])
        
        return waypoints
    
    
    
            
