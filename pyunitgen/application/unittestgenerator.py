from .objects.generator import Generator
import hashlib
import os
import time

file_sums = {}


def checksum(dir):
    sums = []

    for dir, dirs, files in os.walk(dir):
        # if '__pycache__' not in dirs:
        for subdir in dirs:
            sums += checksum(os.path.join(dir, subdir))
        for file_name in files:
            if '__pycache__' not in dir:
                if ".py" in file_name:
                    file_hash = filesum(os.path.join(dir, file_name))
                    if file_sums.get(file_name) is None:
                        sums.append(file_hash)
                        file_sums[file_name] = file_hash
                    else:
                        if file_sums.get(file_name) != file_hash:
                            sums.append(file_hash)
                            file_sums[file_name] = file_hash

    return sums


def filesum(path_to_file):

    file_data = open(path_to_file, 'r',
                     encoding='utf-8').read()
    return hashlib.md5(str(file_data).encode('utf-8')).hexdigest()


def watch(argument):

    if argument.no_watch:
        Generator(argument).start()
    else:
        module = argument.module
        sums = checksum(module)
        sum = hashlib.md5(str(''.join(sums)).encode('utf-8')).hexdigest()

        while True:
            try:

                sums = checksum(module)

                new_sum = hashlib.md5(
                    str(''.join(sums)).encode('utf-8')).hexdigest()

                if new_sum != sum:
                    Generator(argument).start()

                sum = new_sum
                time.sleep(1)
            except OSError as ex:
                print(ex)
            except Exception as ex:
                print(ex)
