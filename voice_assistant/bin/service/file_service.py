import pathlib

directory = pathlib.Path.cwd()


def open_file(os, filename):

    if os == 'Windows':
        os.system(f'explorer {directory}\\files\\{filename}')
    elif os == 'Darwin':
        os.system(f'open {directory}/files/{filename}')
    else:
        os.system(f'xdg-open {directory}/files/{filename}')


def select_file_type():
    # TODO: implement
    return
