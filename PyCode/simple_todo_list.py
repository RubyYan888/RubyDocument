# simple_todo_list.py
class TodoList:
    def __init__(self):
        self.todos = []

    def add_item(self, item):
        self.todos.append(item)

    def remove_item(self, item):
        if item in self.todos:
            self.todos.remove(item)

    def view_items(self):
        return self.todos

if __name__ == "__main__":
    todo_list = TodoList()
    while True:
        action = input("Choose action: add, remove, view, or quit: ").strip().lower()
        if action == 'add':
            item = input("Enter item to add: ")
            todo_list.add_item(item)
        elif action == 'remove':
            item = input("Enter item to remove: ")
            todo_list.remove_item(item)
        elif action == 'view':
            items = todo_list.view_items()
            print("Todo List:")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")
        elif action == 'quit':
            break
