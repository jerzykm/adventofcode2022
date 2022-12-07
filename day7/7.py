if __name__ == '__main__':

    with open('data.txt', 'r') as f:
        ops = [line.rstrip() for line in f.readlines()]

    paths = {}
    current_path = []
    current_path_str = ''

    for op in ops:
        if op.startswith("$ cd"):
            op_dir = op.split(' ')[2]
            if op_dir == '..':
                current_path.pop()
                current_path_str = "/".join(current_path).replace('//', '/')
            else:
                current_path.append(op_dir)
                current_path_str = "/".join(current_path).replace('//', '/')
                if current_path_str not in paths.keys():
                    paths[current_path_str] = []
        elif op.split(' ')[0].isdigit():
            paths[current_path_str].append(int(op.split(' ')[0]))
        elif op.startswith("dir"):
            dir_name = op.split(' ')[1]
            dir_name_str = ("/".join(current_path) + '/' + dir_name).replace('//', '/')
            if dir_name_str not in paths.keys():
                paths[dir_name_str] = []

    total_sizes = []

    paths_kv = [{"name": path[0], "size": sum(path[1])} for path in paths.items()]

    for path in paths_kv:
        total_sizes.append(sum([p['size'] for p in paths_kv if p['name'].startswith(path['name'])]))

    print(sum([s for s in total_sizes if s <= 100000]))
    to_delete = max(total_sizes) - (70000000 - 30000000)

    # to delete (7.2)
    print(min([s for s in total_sizes if s >= to_delete]))





