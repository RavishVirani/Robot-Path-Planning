from Spot import Spot

FILENAME = "input.txt"

def getInput(file):
    # Get dimensions of the room
    dimensions = file.readline().split()
    height = int(dimensions[0])
    width = int(dimensions[1])

    # Get positions of robots
    num_of_robots = int(file.readline())
    robots = []
    for i in range(num_of_robots):
        pos = file.readline().split()
        map_object = map(int, pos)
        list_pos = list(map_object)
        robots.append(list_pos)
    
    # Get the rendezvous point R
    pos = file.readline().split()
    map_object = map(int, pos)
    goal = list(map_object)

    # Get locations of obstacles
    obstacles = []
    for i in range(height - 1, -1, -1):
        pos = file.readline().split()
        ind = 0
        for x in pos[0]:
            if x == "1":
                obstacles.append([ind, i])
            ind = ind + 1        
    
    return width, height, num_of_robots, robots, goal, obstacles

def getSpots(width, height, robots, obstacles, goal):
    # Set all spots in the room
    spots = []
    for i in range(width):
        for j in range(height):
            spots.append(Spot(i, j, width, height))
    
    # Set robot positions
    for robot in robots:
        x = robot[0]
        y = robot[1]
        spot_x, spot_y = spots[x*height + y].get_pos()
        if spot_x == x and spot_y == y:
            spots[x*height + y].set_robot(True)
    
    # Set obstacle positions
    for obstacle in obstacles:
        x = obstacle[0]
        y = obstacle[1]
        spot_x, spot_y = spots[x*height + y].get_pos()
        if spot_x == x and spot_y == y:
            spots[x*height + y].set_obstacle(True)
    
    # Set goal position
    x = goal[0]
    y = goal[1]
    spot_x, spot_y = spots[x*height + y].get_pos()
    if spot_x == x and spot_y == y:
        spots[x*height + y].set_goal(True)
    
    return spots

def heuristic():
    pass

def algorithm():
    pass

def main():
    f = open(FILENAME, "r")
    width, height, num_of_robots, robots, goal, obstacles = getInput(f)
    spots = getSpots(width, height, robots, obstacles, goal)
    
    for spot in spots:
        spot.update_neighbours(spots)
        #spot.get_neighbours() # For testing

    algorithm()

# Run the main function
main()