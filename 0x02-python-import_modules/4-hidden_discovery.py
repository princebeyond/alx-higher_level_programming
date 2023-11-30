#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    module_name = dir(hidden_4)
    for name in module_name:
        if not name.startswith("__"):
            print(name)
