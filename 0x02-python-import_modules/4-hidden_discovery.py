#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    life = dir(hidden_4)
    for life in life:
        if life[0] != '_':
            print(life)
