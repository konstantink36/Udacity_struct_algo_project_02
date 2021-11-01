class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #assert(user)
    #assert(group)

    

    if not isinstance(group, Group):
        print("Error: Group must not be None")
        return

    if user in group.users:
        return True
    elif len(group.groups) == 0:
        return False
   
    else: 
        for x in group.groups:
            return is_user_in_group(user, x)  # recursively check sub-groups



parent = Group("parent")  
child = Group("child")    
sub_child = Group("subchild")  

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)  

child.add_group(sub_child)	   
parent.add_group(child)   	   



print("Test case 1")

user='sub_child_user'
group=sub_child
print(is_user_in_group(user, group))
# This returns True

user='sub_child_user'
group=parent
print(is_user_in_group(user, group))
# This returns True

user='child_user'
group=parent
print(is_user_in_group(user, group))
# This returns False

# returns: True, True, False



print("Test case 2")

user=' '
group=sub_child
print(is_user_in_group(user, group))
# Edge case: empty string returns: False


print("Test case 3")
user='child_user'
group = None
print(is_user_in_group(user, group))
# Edge case: group=None returns: error: group must not be None
