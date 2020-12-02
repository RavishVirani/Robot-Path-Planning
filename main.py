from Spot import Spot
import output
from path_finding import manhattan, A_star

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

    obstacleArr = []
    goal = None
    rob = []
    
    for spot in spots:
        if spot.is_obstacle:
            obstacleArr.append((spot.x, height-1-spot.y))
        elif spot.is_goal:
            goal = (spot.x, spot.y)
        elif spot.is_robot:
            rob.append((spot.x, spot.y))
        spot.update_neighbours(spots)
        #spot.get_neighbours() # For testing
    
    arr = []
    cost_map = []
    #Calculate all the manhattan distances of each spot
    for i in range(height-1,-1,-1):
        temp = []
        for n in range(width):
            if spots[n*height+i].is_obstacle:
                temp.append(-1)
            else:
                temp.append(manhattan((spots[n*height+i].x,spots[n*height+i].y))(goal))
        cost_map.append(temp)
    
    #Order the robots from closest to farthest
    robots = sorted(robots,key = manhattan(goal))
    
    #Find the paths of each robot
    for i in range(num_of_robots):
        path = A_star(robots[i],cost_map,goal,arr)
        if path is None:
            print("The room is impossible to navigate! Robot at {} is stuck!".format(robots[i]))
            print("Continue for the other robots")
            #break
        else:        
            arr.append(path)
    
    #Restate the goal and robots. They are y-inverted.
    goal = (goal[0],height - int(goal[1]) - 1)
    for i in range(len(rob)):
        rob[i] = (rob[i][0],height - rob[i][1] - 1)
            
    #Restate the paths for the draw method. Draw method takes (y,x) coordinates
    for i in range(len(arr)):
        temp = []
        for n in range(len(arr[i])):
            temp.append((height - arr[i][n][1] - 1,arr[i][n][0]))
        arr[i] = temp

    output.drawBoard(height, width, arr, obstacleArr, goal, rob)

# Run the main function
main()
