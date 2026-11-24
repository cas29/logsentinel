def read_lines(path):
    with open (path, encoding='utf-8') as f:
        return f.readlines()

if __name__ == "__main__":
    lines = read_lines("samples/auth.log")
    print(f"Read {len(lines)} line")
    

