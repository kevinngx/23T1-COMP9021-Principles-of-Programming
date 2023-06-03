# Insert your code in this file
import re

def valid_file_lines(file_lines):
    
    # 4.1 If we have more than one comma, return false
    if len(re.findall("[,]",file_lines)) > 1:
        return False

    if file_lines.__contains__(','):
        n1, n2 = file_lines.split(',')
        
        # 4.2 If we have any non-numeric, return False
        if not n1.isnumeric() or not n2.isnumeric():
#             print(f'E4.2 non numerics')
            return False
        
        # 4.3 If the 2nd number is smaller than the first, return False
        if int(n2) <= int(n1):
#             print(f'E4.3 Less than')
            return False
        
    return True

def check_input_lines(lines):
    valid_input = True
    
    # 0. Check for empty file
    if len(lines) == 0:
        return False
    
    # TODO: Error 6 --> Distance between lines
    file_1_prev = 0
    file_2_prev = 0
    
    # Check individual lines
    for line in lines:
        
        # 1. Check for spaces in the line 
#         print(line.strip('\n'))
        if line.__contains__(' '):
            return False
        
        # 2. Check if we have a valid command
        command = re.findall("[A-z]",line)
#         print(command)
        if len(command) != 1 or not command[0] in ['a', 'd', 'c']:
            return False
        
        # 3. Retrieve 2x variables for the first file lines, command, and second file lines
        command = command[0]
        first_file_lines, second_file_lines = line.split(command)
        second_file_lines = second_file_lines.strip('\n')
#         print(first_file_lines + " " + command + " " + second_file_lines)
        
        # 4. Need to check if line numbers are valid
        if not valid_file_lines(first_file_lines) or not valid_file_lines(second_file_lines):
#             print("E04 Invalid Line")
            return False
        
        # 5. Depending on the command we need to check different things
        # 5.1 Check for add commandd is of the format: [1]+[a]+[2.1,2.2]
        if command == 'a' : 
            if first_file_lines.__contains__(','):
                return False
        
        # 5.3 Check for delete commandd is of the format: [1.1,1.2]+[d]+[1]
        if command == 'd' : 
            if second_file_lines.__contains__(','):
                return False
            
        # 6. Check if the distances between previous commands is constant (i.e. checking for the 'same' lines)
        file_1_command_start, file_1_command_end = get_command_positions(first_file_lines, command, 1)
#         print(file_1_command_start, file_1_command_end)
        file_2_command_start, file_2_command_end = get_command_positions(second_file_lines, command, 2)    
#         print(file_2_command_start, file_2_command_end)
            
#         print(f'File 1: Prev = {file_1_prev} Command Start = {file_1_command_start}, Command End = {file_1_command_end}')
#         print(f'File 2: Prev = {file_2_prev} Command Start = {file_2_command_start}, Command End = {file_2_command_end}')
#         print(f'F1: Start - Prev = {file_1_command_start - file_1_prev}')
#         print(f'F2: Start - Prev = {file_2_command_start - file_2_prev}')
        
        if (file_1_command_start - file_1_prev) != (file_2_command_start - file_2_prev):
            return False

        if line != lines[0] and (file_1_command_start == file_1_prev or file_2_command_start == file_2_prev):
            # print('Start of 2nd command is not strictly greater than the end of the previous command')
            return False
            
        file_1_prev = file_1_command_end
        file_2_prev = file_2_command_end
        # TODO: ^ Start-Prev needs to be equal for both
            
#         print()
    return True

    
def get_command_positions(line_commands, command, file):
    if line_commands.__contains__(','):
        file_command_start = int(line_commands.split(',')[0])
        file_command_end = int(line_commands.split(',')[1])
    else:
        file_command_start = int(line_commands)
        file_command_end = int(line_commands)
        
    if command == "a" and file == 2:
        file_command_start -= 1

    if command == "c":
        file_command_start -= 1

    if command == "d" and file == 1:
        file_command_start -= 1
        
    return file_command_start, file_command_end
   
   
class DiffCommandsError(Exception):
    pass


class DiffCommands:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.readlines()
        if not check_input_lines(self.lines):
            raise DiffCommandsError('Cannot possibly be the commands for the diff of two files')
            
    def __str__(self):
        # TODO: last line has a '\n' that may need to be ignored
        return ''.join(self.lines).strip('\n')

class OriginalNewFiles:
    def __init__(self, original_filename, new_filename):
        with open(original_filename, 'r') as f1, open(new_filename, 'r') as f2:
            self.first_file = f1.readlines()
            self.second_file = f2.readlines()
    
    def output_diff(self, diff_file):
        # print("testing output diffs") # Test 14
        for line in diff_file.lines:
            print(line.strip('\n'))
            command = re.findall("[A-z]",line)[0]
            first_file_lines, second_file_lines = line.split(command)
            second_file_lines = second_file_lines.strip('\n')

            file_1_command_start, file_1_command_end = get_command_positions(first_file_lines, command, 1)    
            file_2_command_start, file_2_command_end = get_command_positions(second_file_lines, command, 2)    

            if command == 'a':
                for i in range(file_2_command_start, file_2_command_end):
                    print(">", self.second_file[i].strip('\n'))

            if command == 'd':
                for i in range(file_1_command_start, file_1_command_end):
                    print("<", self.first_file[i].strip('\n'))

            if command == 'c':
                for i in range(file_1_command_start, file_1_command_end):
                    print("<", self.first_file[i].strip('\n'))
                print("---")
                for i in range(file_2_command_start, file_2_command_end):
                    print(">", self.second_file[i].strip('\n'))
        
    def output_unmodified(self, diff_file, command_skipped, file_to_output):
        prev = 0
        file = (self.first_file, self.second_file)[file_to_output - 1]
        
        for line in diff_file.lines:
            # print(line.strip('\n'))
            command = re.findall("[A-z]",line)[0]
            if command == command_skipped:
                continue
            file_lines = line.split(command)[file_to_output - 1]
            command_start, command_end = get_command_positions(file_lines, command, file_to_output)    
            # print(f'File Stats: Prev = {prev} Command Start = {command_start}, Command End = {command_end}')
            for i in range(prev, command_start):
                print(file[i].strip('\n'))
            prev = command_end
            print("...")

        for i in range(prev, len(file)):
            print(file[i].strip('\n'))

    def output_unmodified_from_original(self, diff_file):
        self.output_unmodified(diff_file, 'a', 1)
    
    def output_unmodified_from_new(self, diff_file):
        self.output_unmodified(diff_file, 'd', 2)
    
    def get_all_diff_commands():
        print("Testing get_all_diff_commands")

    def compute_levenshtein_distance(self):
        deletion_cost = 1
        insertion_cost = 1
        substitution_cost = 2
        F_1 = len(self.first_file) + 1
        F_2 = len(self.second_file) + 1
        table = [[(0, []) for _ in range(F_2)] for _ in range(F_1)]

        for i in range(1, F_1):
            table[i][0] = i, ['-']
        for j in range(1, F_2):
            table[0][j] = j, ['|']

        d = {}

        for i in range(1, F_1):
            for j in range(1, F_2):
                d['-'] = table[i - 1][j][0] + deletion_cost
                d['|'] = table[i][j - 1][0] + insertion_cost
                d['/'] = table[i - 1][j - 1][0] if self.first_file[i - 1] == self.second_file[j - 1] else table[i - 1][j - 1][0] + substitution_cost
                minimal_cost = min(d.values())        
                table[i][j] = minimal_cost, [x for x in d if d[x] == minimal_cost]

        return table[len(self.first_file)][len(self.second_file)][0]

    def compute_diff_file_cost(self, diff_file):
        cost = 0
        for line in diff_file.lines:
#             print(line.strip('\n'))
            command = re.findall("[A-z]",line)[0]
            first_file_lines, second_file_lines = line.split(command)
            second_file_lines = second_file_lines.strip('\n')

            file_1_command_start, file_1_command_end = get_command_positions(first_file_lines, command, 1)    
            file_2_command_start, file_2_command_end = get_command_positions(second_file_lines, command, 2)    

            if command == 'd':
                cost += file_1_command_end - file_1_command_start

            if command == 'a':
                cost += file_2_command_end - file_2_command_start    

            if command == 'c':
                cost += file_1_command_end - file_1_command_start
                cost += file_2_command_end - file_2_command_start    
            
        return cost
    
    def is_a_possible_diff(self, diff_file):
        if self.compute_diff_file_cost(diff_file) == self.compute_levenshtein_distance():
            return True
        else:
            return False

