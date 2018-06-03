import os


def rename_files():
    print_list = os.listdir(r"/home/tadashera/Pictures/prank")
    base_path = os.getcwd()
    os.chdir(r"/home/tadashera/Pictures/prank")
    table = str.maketrans(dict.fromkeys('0123456789'))

    for file_name in print_list:
        os.rename(file_name, file_name.translate(table))

    os.chdir(base_path)

    print_list = os.listdir(r"/home/tadashera/Pictures/prank")
    print(print_list)

rename_files()