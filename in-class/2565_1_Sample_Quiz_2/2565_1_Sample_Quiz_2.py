def get_to_pattern(pattern, new_name, path):
    lowered_pattern = pattern.lower()
    lowered_path = path.lower()
    if len(pattern) != len(path):
        return path
    for i in range(len(pattern)):
        if pattern[i] != '?' and lowered_pattern[i] != lowered_path[i]:
            return path
    return new_name


def get_last_slash_index(path):
    for i in range(len(path) - 1, -1, -1):
        if path[i] == '/':
            return i
    return -1


def get_new_path(pattern, new_name, path):
    
    if '/' not in path:
        return path

    last_slash_index = get_last_slash_index(path)
    tail_path = path[last_slash_index + 1:]
    tail_cutted_path = path[:last_slash_index]
    new_path = tail_path

    while True:
        last_slash_index = get_last_slash_index(tail_cutted_path)
        tail_path = tail_cutted_path[last_slash_index + 1:]
        if last_slash_index == -1:
            tail_cutted_path = ''
        else:
            tail_cutted_path = tail_cutted_path[:last_slash_index]
        new_path = get_to_pattern(
            pattern, new_name, tail_path) + '/' + new_path
        if last_slash_index == -1:
            break

    return new_path


def main():
    file_name = input().strip()
    old_folder_name = input().strip()
    new_folder_name = input().strip()

    data = open(file_name, 'r')
    for path in data:
        print(
            get_new_path(
                old_folder_name,
                new_folder_name,
                path.strip()
            )
        )

    data.close()


main()
