class Spot:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_obstacle = False
        self.is_robot = False
        self.is_goal = False
        self.neighbours = []
    
    def set_obstacle(self, is_obstacle):
        self.is_obstacle = is_obstacle
    
    def set_robot(self, is_robot):
        self.is_robot = is_robot
    
    def set_goal(self, is_goal):
        self.is_goal = is_goal

    def get_pos(self):
        return self.x, self.y
    
    def get_neighbours(self):
        # For testing
        for s in self.neighbours:
            x, y = s.get_pos()
            print(x, y)
        print()
    
    def update_neighbours(self, spots):
        self.neighbours = []

        if self.y > 0 and not spots[self.x*self.height + self.y - 1].is_obstacle: # DOWN
            self.neighbours.append(spots[self.x*self.height + self.y - 1])
        if self.y < self.height - 1 and not spots[self.x*self.height + self.y + 1].is_obstacle: # UP
            self.neighbours.append(spots[self.x*self.height + self.y + 1])
        if self.x < self.width - 1 and not spots[(self.x + 1)*self.height + self.y].is_obstacle: # RIGHT
            self.neighbours.append(spots[(self.x + 1)*self.height + self.y])
        if self.x > 0 and not spots[(self.x - 1)*self.height + self.y].is_obstacle: # LEFT
            self.neighbours.append(spots[(self.x - 1)*self.height + self.y])
    