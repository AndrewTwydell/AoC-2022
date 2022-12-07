
def is_command(line):
    return line.startswith('$')

def is_dir(line):
    return line.startswith('dir')

def is_cd_command(line):
    return line.startswith('$ cd')

def is_ls_command(line):
    return line.startswith('$ ls')

def get_dir_name(line):
    return line.split(' ')[1]

def get_file_size(line):
    return int(line.split(' ')[0])

dirs_to_add = []

def print_if_size_appropriate(dir):
    if int(dir.get_size()) < 100000:
        dirs_to_add.append(dir)
    if len(dir.get_subdirs()) > 0:
        for subdir in dir.get_subdirs():
            print_if_size_appropriate(subdir)
    

class dir:
    def __init__(self, name, parentDir=None):
        self.name = name
        self.subdirs = []
        self.size = 0
        self.sizes = []
        self.parentDir = parentDir
    
    def get_subdirs(self):
        return self.subdirs
    
    def get_size(self):
        total = 0
        for size in self.sizes:
            total += size
        for subdir in self.subdirs:
            total += subdir.get_size()
        return total
    
    def get_parent_dir(self):
        return self.parentDir
    
    def add_subdir(self, subdir):
        self.subdirs.append(subdir)
    
    def add_file_size(self, size):
        self.size += size
        self.sizes.append(size)
    
    def has_subdir(self, name):
        for subdir in self.subdirs:
            if subdir.name == name:
                return True
        return False
    
    def get_subdir(self, name):
        for subdir in self.subdirs:
            if subdir.name == name:
                return subdir
        return None
    
    def __str__(self):
        output = self.name + ' ' + str(self.get_size()) + ' '
        for subdir in self.subdirs:
            output += subdir.name + ' '
        return output

with open('input.txt') as input:
    inputArr = []
    for line in input:
        inputArr.append(line.strip())
    
    top_level_dir = dir('/')
    currentDir = top_level_dir
    previousDir = None
    
    for line in inputArr:
        if is_cd_command(line):
            dir_to_change_to = line.split(' ')[2]
            if dir_to_change_to == '..':
                currentDir = currentDir.get_parent_dir()
            else:
                if currentDir.has_subdir(dir_to_change_to):
                    previousDir = currentDir
                    currentDir = currentDir.get_subdir(dir_to_change_to)
                else:
                    new_dir = dir(dir_to_change_to, currentDir)
                    currentDir.add_subdir(new_dir)
                    previousDir = currentDir
                    currentDir = new_dir
        elif is_dir(line):
            if currentDir.has_subdir(get_dir_name(line)):
                pass
            else:
                new_dir = dir(get_dir_name(line), currentDir)
                currentDir.add_subdir(new_dir)
        else:
            if not is_ls_command(line):
                size = get_file_size(line)
                currentDir.add_file_size(size)


    print_if_size_appropriate(top_level_dir)

    totalcount = 0
    for dir in dirs_to_add:
        totalcount += dir.get_size()
    
    print(totalcount)