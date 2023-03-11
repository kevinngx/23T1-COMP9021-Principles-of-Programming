import sys

class rectangle:
    def __init__(self, x1, y1, x2, y2):
        
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
    
    def print_points(self):
        print(f'p1 = ({self.x1},{self.y1}) , p2 = ({self.x2},{self.y2})')
    
    def miny(self):
        return min(self.y1, self.y2)
    
    def minx(self):
        return min(self.x1, self.x2)
    
    def maxy(self):
        return max(self.y1, self.y2)
    
    def maxx(self):
        return max(self.x1, self.x2)
        
def print_all_rectangles(rectangles):
    for rectangle in rectangles:
        rectangle.print_points()

def get_min_points():
    minx = 0
    miny = 0
    for rectangle in rectangles:
        minx = min(minx, rectangle.minx())
        miny = min(miny, rectangle.miny())
    return minx, miny    
        
def get_grid_shift():
    # We only want to shift where the lowest points are negative. If they are greater than 0, we do not shift the points i.e. 0
    minx, miny = get_min_points()
    minx = min(minx, 0)
    miny = min(miny, 0)
    return abs(minx), abs(miny)

def get_max_points(rectangles):
    maxx = 0
    maxy = 0
    for rectangle in rectangles:
        maxx = max(maxx, rectangle.maxx())
        maxy = max(maxy, rectangle.maxy())
    return maxx, maxy  
    

def shift_points(xshift, yshift):
    for rectangle in rectangles:
        rectangle.x1 += xshift + 1
        rectangle.x2 += xshift + 1
        rectangle.y1 += yshift + 1
        rectangle.y2 += yshift + 1
        
def print_grid(grid):
    y_cord = len(grid)
    x_cord = len(grid[0])
    
    for y in range(len(grid)):
        print(f'{y_cord:5}|',end='')
        
        for x in range(len(grid[0])):
            print(f'{grid[-y][x]:3}', end='')
        
        y_cord = y_cord - 1
        print()
        
    print(f'{0:5}|',end='')
    print('---' * len(grid[0]))
    print(f'     |',end='')
    for i in range(len(grid[0])):
        print(f'{i:3}', end='')

def draw_rectangle(grid, rectangle):
    minx = rectangle.minx()
    maxx = rectangle.maxx()
    miny = rectangle.miny()
    maxy = rectangle.maxy()
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            if x in (minx, maxx-1) or y in (miny, maxy-1):
                    grid[y][x] = '0'
            else: 
                grid[y][x] = '-'
        
def assign_perimeter_values(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '0':
                grid[x][y] = check_surrounding(grid, x, y)
                
def check_surrounding(grid, x, y):
    surrounding_perimeter = 0
    try:
        if grid[x][y+1] == '':
            surrounding_perimeter += 1
    except IndexError:
        surrounding_perimeter += 1
    try:
        if grid[x][y-1] == '':
            surrounding_perimeter += 1
    except IndexError:
        surrounding_perimeter += 1
    
    try:
        if grid[x+1][y] == '':
            surrounding_perimeter += 1
    except IndexError:
        surrounding_perimeter += 1
    
    try:
        if grid[x-1][y] == '':
            surrounding_perimeter += 1
    except IndexError:
        surrounding_perimeter += 1
    
    return surrounding_perimeter

def count_perimeter(grid):
    sum = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] not in ('', '-','0'):
                sum += grid[x][y]
    return sum

filename = input('Which data file do you want to use? ')
# filename = 'frames_1.txt'

rectangles = []

try:
    with open(filename) as file:

        for line in file:
            x1, y1, x2, y2 = line.removesuffix('\n').split(' ')
            rectangles.append(rectangle(x1, y1, x2, y2))


except FileNotFoundError:
    print('Could not open a file named', filename)
    print('Giving up...')
    sys.exit()

# Step 1 = Shift the rectangles such that all points are positive (makes it easier to map to an array)
xshift, yshift = get_grid_shift()
shift_points(xshift, yshift)
# print_all_rectangles(rectangles)

# Step 2 Create an empty grid for us to draw on
maxx, maxy = get_max_points(rectangles)
grid = [[''] * maxx for _ in range(maxy)]
# print_grid(grid)

# Step 3 Draw on the grid  
for rectangle in rectangles:
    draw_rectangle(grid, rectangle)
# print_grid(grid)

# Step 4 Assign the perimeter value
assign_perimeter_values(grid)
# print_grid(grid)

# Step 5 Calculate and print the perimeter
print('The perimeter is:', count_perimeter(grid))