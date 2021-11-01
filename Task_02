import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
   
    paths = list()		   # list of paths of files that have file name suffix
    entries = os.listdir(path)     # list of files/directories in path
   
    for entry in entries:          		 # loop over files/directories in path
        entrypath = os.path.join(path, entry)    # full path of each file/directory in path

        if os.path.isfile(entrypath) and entrypath.endswith(suffix):		 # if path is a file and ends with suffix
            paths.append(entrypath)		 				 # add that path to list of paths 

        elif os.path.isdir(entrypath):           		# if path is a (sub)directory
            paths = paths + find_files(suffix, entrypath)	# recursively find files with suffix in (sub)directories 
    
    return paths

print("Test case 1:")
print(find_files(".c","."))  
# Find files with suffix .c in home directory (.)
# returns: ['.\\testdir\\subdir1\\a.c', '.\\testdir\\subdir3\\subsubdir1\\b.c', '.\\testdir\\subdir5\\a.c', '.\\testdir\\t1.c']


print("Test case 2:")
print(find_files(".h","."))  
# Find files with suffix .h in home directory (.)
# returns: ['.\\testdir\\subdir1\\a.h', '.\\testdir\\subdir3\\subsubdir1\\b.h', '.\\testdir\\subdir5\\a.h', '.\\testdir\\t1.h']


print("Test case 3:")
print(find_files(".c","./testdir/subdir1")) 
# find files with suffix .c in /testdir/subdir1"
# returns: ['./testdir/subdir1\\a.c']


print("Test case 4:")
print(find_files(" ",".")) 
# returns empty list: []


print("Test case 5:")
#print(find_files(".c"," ")) 
#returns: The system cannot find the path specified
