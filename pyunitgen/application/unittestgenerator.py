from .objects.generator import Generator
import hashlib
import os
import time
from os import path

file_sums = {}

list_of_changed_file = {}


def checksum(root_dir):
    sums = []
    global list_of_changed_file

    for file_dir, dirs, files in os.walk(root_dir):
        # if '__pycache__' not in dirs:
        # print(file_dir)
        # print(dirs)
        for subdir in dirs:
            sums += checksum(os.path.join(file_dir, subdir))
        for file_name in files:
            if ('__pycache__' not in file_dir) and (".git" not in file_dir):
                if ".py" in file_name:
                    file_hash = filesum(os.path.join(file_dir, file_name))
                    if file_sums.get(file_name) is None:
                        sums.append(file_hash)
                        file_sums[file_name] = file_hash
                    else:
                        if file_sums.get(file_name) != file_hash:
                            if not list_of_changed_file.get(file_dir):
                                list_of_changed_file[file_dir] = []
                            sums.append(file_hash)
                            file_sums[file_name] = file_hash
                            list_of_changed_file[file_dir].append(file_name)

    return sums


def filesum(path_to_file):

    file_data = open(path_to_file, 'r',
                     encoding='utf-8').read()
    return hashlib.md5(str(file_data).encode('utf-8')).hexdigest()


def watch(argument):

    global list_of_changed_file

    if path.isfile(argument.module):
        filename = path.basename(argument.module)
        path_dir = path.dirname(argument.module) + "/"
        list_of_changed_file[path_dir] = []
        list_of_changed_file[path_dir].append(filename)
        argument.module = list_of_changed_file

    if argument.no_watch:
        Generator(argument).start()
    else:
        module = argument.module
        sums = checksum(module)
        sum_hash = hashlib.md5(str(''.join(sums)).encode('utf-8')).hexdigest()

        while True:
            try:

                sums = checksum(module)

                new_sum = hashlib.md5(
                    str(''.join(sums)).encode('utf-8')).hexdigest()

                if list_of_changed_file:
                    argument.module = list_of_changed_file
                    list_of_changed_file = {}

                if new_sum != sum_hash:
                    Generator(argument).start()

                sum_hash = new_sum
                time.sleep(1)
            except OSError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
