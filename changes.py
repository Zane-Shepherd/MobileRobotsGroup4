## Put this above the main while loop for waypoint generation (optional, makes the robot starts closer to the door)
if abs(entry_point[1] - ybottom) > abs(entry_point[1] - ytop):
    x = xleft + w / 2
    y = ytop - w / 2
else:
    x = xleft + w / 2
    y = ybottom + w / 2


## replace the main while loop with this ##

waypoints.append([x,y])  # note that this first append has been moved out of the loop, and subsequent in-loop appends happen after the variables have been changed


while x < xright - w / 2:
    
    if index % 2 == 0:   #changed because append happens 
        x += w
    else:
        if y == ybottom + w / 2:
            y = ytop - w / 2
        elif y == ytop - w / 2:
            y = ybottom + w / 2
    index += 1

    waypoints.append([x,y])


waypoints.append([xright - w / 2, y])
index += 1

if y == ybottom + w / 2:
    y = ytop - w / 2
elif y == ytop - w / 2:
    y = ybottom + w / 2
    
waypoints.append([xright - w / 2, y])

# second pass added here

if y == ybottom + w/2:
    while y < ytop - w / 2:
        
        if index % 2 == 0:
            y += w
        else:
            if x == xleft + w / 2:
                x = xright - w / 2
            elif x == xright - w / 2:
                x = xleft + w / 2
        index += 1

        waypoints.append([x,y])


    waypoints.append([x, ytop - w / 2])
    index += 1
    
    if x == xleft + w / 2:
        x = xright - w / 2
    elif x == xright - w / 2:
        x = xleft + w / 2
        
    waypoints.append([x, ytop - w / 2])
elif y == ytop - w/2:
            while y > ybottom + w / 2:
                
                if index % 2 == 0:
                    y -= w
                else:
                    if x == xleft + w / 2:
                        x = xright - w / 2
                    elif x == xright - w / 2:
                        x = xleft + w / 2
                index += 1

                waypoints.append([x,y])

        
            waypoints.append([x, ybottom + w / 2])
            index += 1
            
            if x == xleft + w / 2:
                x = xright - w / 2
            elif x == xright - w / 2:
                x = xleft + w / 2
                
            waypoints.append([x, ybottom + w / 2])
