from queue import PriorityQueue

def manhattan(goal):
    def other(coor):
        x = abs(coor[0]-goal[0])
        y = abs(coor[1]-goal[1])
        return x+y
    return other

class Node:
    def __init__(self,actualCost,coord,parent,hCost):
        self.actualCost = actualCost
        self.coord = coord
        self.parent = parent
        self.hCost = hCost
    def __eq__(self,other):
        return self.actualCost + self.hCost == other.actualCost + other.hCost
    def __lt__(self,other):
        return self.actualCost + self.hCost<other.actualCost + other.hCost
    def is_goal(self,goal):
        return self.coord == goal
    
def binary_search(item,array):
    start = 0
    end = len(array)-1
    while start<=end:
        mid = (end + start)//2        
        if array[mid]>item:
            end = mid - 1
        elif array[mid]<item:
            start = mid + 1
        else:
            return mid
    return start

def A_star(robot,room,goal,paths):
    print("Current Robot is ",robot)
    q = PriorityQueue()
    visited = []
    for i in range(len(room[0])):
        visited.append([])
    q.put(Node(0,(robot[0],robot[1]),None,room[len(room)-robot[1]-1][robot[0]]))
    current=None
    
    while not q.empty():
        current = q.get()
        count+=1
        temp = None
        #Add nodes of (cost,location)
        if current.is_goal((goal[0],goal[1])):
            #Do things
            break #return
        ##Should we check if the current node is in other paths?
        ##Or is it better to do time check later

        else:
            #Check parent node as well?
            #Check the up spot
            if current.coord[1]<len(room)-1 and room[len(room)-current.coord[1]-1-1][current.coord[0]]!=-1:
                temp = binary_search((current.coord[0],current.coord[1]+1),visited[current.coord[0]])                
                if len(visited[current.coord[0]])==temp or visited[current.coord[0]][temp]!=(current.coord[0],current.coord[1]+1):                    
                    q.put(Node(current.actualCost+1,(current.coord[0],current.coord[1]+1),current,room[len(room)-current.coord[1]-1-1][current.coord[0]]))

            #Check the Right spot
            if current.coord[0]<len(room[0])-1 and room[len(room)-current.coord[1]-1][current.coord[0]+1]!=-1:
                temp = binary_search((current.coord[0]+1,current.coord[1]),visited[current.coord[0]+1])
                if len(visited[current.coord[0]+1])==temp or visited[current.coord[0]+1][temp]!=(current.coord[0]+1,current.coord[1]): 
                    q.put(Node(current.actualCost+1,(current.coord[0]+1,current.coord[1]),current,room[len(room)-current.coord[1]-1][current.coord[0]+1]))
                    
            #Check the Down spot
            if current.coord[1]>0 and room[len(room)-current.coord[1]-1+1][current.coord[0]]!=-1:
                temp = binary_search((current.coord[0],current.coord[1]-1),visited[current.coord[0]])
                if len(visited[current.coord[0]])==temp or visited[current.coord[0]][temp]!=(current.coord[0],current.coord[1]-1):                    
                    q.put(Node(current.actualCost+1,(current.coord[0],current.coord[1]-1),current,room[len(room)-current.coord[1]-1+1][current.coord[0]]))
                    #temp = binary_search(current.coord,visited[current.coord[0]]) <- Why this here?
            
            #Check the Left spot
            if current.coord[0]>0 and room[len(room)-current.coord[1]-1][current.coord[0]-1]!=-1:
                temp = binary_search((current.coord[0]-1,current.coord[1]),visited[current.coord[0]-1])
                if len(visited[current.coord[0]-1])==temp or visited[current.coord[0]-1][temp]!=(current.coord[0]-1,current.coord[1]):
                    q.put(Node(current.actualCost+1,(current.coord[0]-1,current.coord[1]),current,room[len(room)-current.coord[1]-1][current.coord[0]-1]))
            
            temp = binary_search(current.coord,visited[current.coord[0]])            
            visited[current.coord[0]].insert(temp,current.coord)
    #Not sure
    #Cannot find a path
    if q.empty() and not current.is_goal((goal[0],goal[1])):
        #print("Impossible Puzzle")
        return None
    
    #Construct an array for the path
    current_path = []
    while current is not None:
        current_path.insert(0,current.coord)
        current = current.parent
    
    #Check the other paths for conflicts
    i=1
    while i < len(current_path)-1:
        for n in range(len(paths)):
            if i < len(paths[n]):
                if current_path[i] == paths[n][i]:
                    print("conflict at",current_path[i])
                    
                    #Remove conflict spot from the map temporarily
                    temp_index = (len(room)-current_path[i][1]-1,current_path[i][0])
                    temp_value = room[temp_index[0]][temp_index[1]]
                    room[temp_index[0]][temp_index[1]] = -1

                    print()
                    #Check for another path for the current robot
                    temp_current = A_star(robot,room,goal,paths)
                    if temp_current is None or len(temp_current)>len(current_path):
                        #Check for another path for the robot it is in conflict with
                        actual_path = paths.pop(n)
                        temp_other = A_star(actual_path[0],room,goal,paths)
                        if temp_other is None or len(temp_other)>len(actual_path):
                            current_path.insert(i,current_path[i-1])
                            print("No other satisfying paths. Just wait once")
                        else:
                            actual_path = temp_other
                            print("Modify old path",temp_other)
                        paths.insert(n,actual_path)

                    else:
                        print("Another current path found")
                        current_path = temp_current
                        #i=0
                        
                    room[temp_index[0]][temp_index[1]] = temp_value
                    
        i+=1
    return current_path      
