FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file:
        local_todos = file.readlines()
    return local_todos

def write_todos(todos,filepath=FILEPATH):
    """ Write the do=do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)