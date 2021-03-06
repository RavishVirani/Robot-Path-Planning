# Robot-Path-Planning
CP-468 Group 15 Term Project

Matthew Nitsopoulos (170673880)<br/>
Harkaran Grewal (170531870)<br/>
Min-Ho Choi (170813020)<br/>
Ravish Virani (173084290)<br/>
Jungeun Choi (156803830)<br/>

Consider a Museum room that is patrolled by N robots at night.  At a pre-determined time,  the robots are supposed to rendezvous at a given point R in the room.  The robots move inside the room, and the room contains obstacles,  such as chairs and benches for the visitors,  paintings,  sculptures etc.  The robots are supposed to know the locations of the obstacles in the room. Implement  an A*-based  algorithm  to  compute  the  path  of  each  robot,  from  its  initial  position  to  the  given rendezvous point R.

## Path Planning Algorithm
Path planning is a simple problem to find the shortest path from one vertex to another. The term “shortest” here means the least cumulative edge cost, which can be represneted as physical distance (the robot's path in this problem), any kind of delay or any other type of metric that is important to the given application.

## Requirements
1. Python 3.0 or higher
2. Pygame
3. Input in the form of text file (explained below)

## How it works
### Input
The input is accepted as a text file which has a specific data regarding the robot and the room. Each line represents the dimensions of the room, the number of robots, the initial position of each robot, the given rendezvous point as well as the locations of the obstacles in the room.
### Order of Robots
Order of robots is conducted to make the code more efficient as this eliminates the path calculations for the robots after the first robot. This is done as the later robots take the same path as the first robot and avoid the recalculations until needed.
### Algorithm
This program uses the A* algorithm. This implementation of the A* algorithm uses nodes that contain the coordinate, the actual cost of reaching that node, the heuristic cost of the node reaching the goal, and the parent node that created this node. 
The heuristic used here is the manhattan heuristic. Since the manhattan heuristic is consistent, the first instance of a successor node is the optimal way to reach that node from the current node. Thus we can ignore any other instance of adding the node. Since heaps do not support searching, another data structure is needed to check which nodes are inside the heap. This is done through a hash table where each index of the hash table points to a sorted array.
The code also implements priority queue as heaps such that ties in the estimated cost to the goal [f(n)] is broken with Last in, First Out..
### Path Conflict Resolution
The robots can only overlap eachother at the meeting point which can create a conflict in the paths. If a conflict is detected by the robot by other robot, or any other obstacle, it will the A* algorithm again to find the new shortest path.
### Output
The output of the program displays multiple results. 
1. Pygame Window: The window created through pygame which displays the robots, room and the path taken by the robot to reach the destination.
2. Console Output: i. Robot identified by its location and its path cost.
                   ii. The total cost of all paths.

## How to run
01. Install python and pygame onto the device.
02. Clone this repository as a zip onto your machine.
03. Unzip the file
04. Create the input.txt file with the data.
05. Locate the directory of the file in command prompt through 'cd' function. 
06. Type "python main.py" to run the program through main.py file.
07. The cmd will display the path costs, then the pygame window will open.
08. Press the -> key on the keyboard to advance the robots.
09. Press the <- key to reverse the robots in time.
10. To autorun the robot just press 'a'.
11. Shut the program by pressing "x" on the keyboard.<br/>

**How to make input.txt**<br/>
To change the input of the program please alter the text in the “input.txt” file<br/>
The text in the input file must be in the following format<br/>
- The first line must contain 2 numbers separated by a space, these represent the room dimensions (height by width)<br/>
- The next line must contain 1 number which is the number of robots<br/>
- The next n lines must contain 2 numbers separated by a space which indicate the robots positions. N is the number that was entered in ii.<br/>
- The next line must contain 2 numbers separated by a space which represent the rendezvous point that the robots will meet at (if possible)<br/>
- Lastly, the next n lines must contain x number of 1’s or 0’s where n is the first number entered in step i and x is the second number entered in step i. A 1 represents a space that is obstructed by an object and a 0 represents an open space.<br/>


## Sample Run
**input.txt**

20 27<br/>
2<br/>
6 7<br/>
12 1<br/>
13 15<br/>
111001101010101111101001000<br/>
000000100111100011011111000<br/>
110111101010001110000000110<br/>
000001011010010101110010011<br/>
000100010011001100011100001<br/>
100000100101010010101110111<br/>
000111111000000101100000000<br/>
111010010110011111000000110<br/>
001000010001000001000001110<br/>
010000110001110101111100011<br/>
101101100101010010110101100<br/>
011111101100111000100100110<br/>
000000001010010000101100001<br/>
011000100011001010101011100<br/>
001011000011101011000111010<br/>
100010001111100011101010010<br/>
100011011100110010010000011<br/>
101111110111101000111110010<br/>
101011101001001110100000100<br/>
101111000010100000000100011<br/>

![](Output_Img/output.JPG)
<br/>
