#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 

    ls = dir(hidden_4)
    
    for x in ls:
        if x[:2] == '__':
            continue
        print(f"{x}")

