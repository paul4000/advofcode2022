from read import read_input


# model
class Directory:

    def __init__(self, label):
        self.label = label
        self.directories = []
        self.files = []
        self.parent_directory = None

    def __str__(self):
        return self.label

    def create_subdirectory(self, directory):
        directory.parent_directory = self
        self.directories.append(directory)

    def add_file(self, label, size):
        self.files.append(File(label, size))

    def find_subfolder(self, label):
        subfolder = list(filter(lambda x: label == x.label, self.directories))
        return subfolder[0] if len(subfolder) > 0 else None

    def sum_size(self):
        files_sum = sum(map(lambda x: x.size, self.files))
        files_sum += sum(map(lambda y: y.sum_size(), self.directories))
        return files_sum

    def list_directories_with_sizes(self):
        sizes = [(di.label, di.sum_size()) for di in self.directories]
        for d in self.directories:
            sizes.extend(d.list_directories_with_sizes())
        return sizes


class File:
    def __init__(self, label, size):
        self.label = label
        self.size = size

    def __str__(self):
        return self.label + "," + str(self.size)


# part 1
LS = "ls"
CD = "cd"
CMD_SIGN = '$'
commands_data = read_input('day_7.txt')
# create model
home_folder = Directory("/")
current_folder = home_folder
for input_line in commands_data:
    if input_line.startswith(CMD_SIGN):
        parsed_command = input_line.split(" ")
        command = parsed_command[1]
        if command == CD:
            argument = parsed_command[2]
            if argument == "..":
                current_folder = current_folder.parent_directory
            elif argument == "/":
                current_folder = home_folder
            else:
                subfolder = Directory(argument)
                current_folder.create_subdirectory(subfolder)
                current_folder = subfolder
    else:
        # it's result of ls command
        if not input_line.startswith("dir"):
            # it's a file! let's add it to current directory
            size = int(input_line.split(" ")[0])
            label = input_line.split(" ")[1]
            current_folder.add_file(label, size)

# compute
print("/ " + str(home_folder.sum_size()))
print(home_folder.list_directories_with_sizes())
sizes_list = home_folder.list_directories_with_sizes()
sizes_list.append(("/", home_folder.sum_size()))
MAX_SIZE = 100000
s = sum(map(lambda size_tuple: size_tuple[1], filter(lambda size_tuple: size_tuple[1] < MAX_SIZE, sizes_list)))
print(s)

# part 2
free_space = 70000000 - home_folder.sum_size()
SPACE_NEEDED_FOR_UPDATE = 30000000
need_to_free = SPACE_NEEDED_FOR_UPDATE - free_space
print(need_to_free)
sorted_sizes = list(sorted(filter(lambda size_tuple: size_tuple[1] > need_to_free, sizes_list), key = lambda x: x[1]))
print(sorted_sizes)