import os

LIST1 = ["a", "b"]
LIST2 = ["b", "c", "d"]

PATH1 = 'materials\\FirstDir'
PATH2 = 'materials\\SecondDir'


def compare_lists(list1, list2):
    shared = []
    only_in_a = []
    only_in_b = []
    for item in list1:
        if item in list2:
            shared.append(item)
        else:
            only_in_a.append(item)

    for item in list2:
        if item in list1:
            if item not in shared:
                shared.append(item)
        else:
            only_in_b.append(item)

    return shared, only_in_a, only_in_b


def get_absolut_path(dir_path):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ROOT_DIR, dir_path)


def get_files_from_dir(dir_name):
    path = get_absolut_path(dir_name)
    items = os.listdir(path)
    return items


def compare_folders(folder1, folder2):
    files1 = get_files_from_dir(folder1)
    files2 = get_files_from_dir(folder2)
    return compare_lists(files1, files2)


assert compare_lists(["a", "b"], ["b", "c", "d"]) == (['b'], ['a'], ['c', 'd']), 'Lists test FAILED'
assert compare_folders(PATH1, PATH2) == (['DocToRead3.txt', 'DocToRead4.txt'], ['DocToRead1.txt', 'DocToRead2.txt'],
                                         ['DocToRead5.txt']), 'Folders items test FAILED'


def run_folders_check(path1, path2):
    common_files, only_in_first_dir, only_in_second_dir = compare_folders(path1, path2)
    print('Common files are: {},\nOnly in folder 1: {},\nOnly in folder 2: {}'.format(common_files, only_in_first_dir,
                                                                                      only_in_second_dir))


if __name__ == "__main__":
    exit(run_folders_check(PATH1, PATH2))
