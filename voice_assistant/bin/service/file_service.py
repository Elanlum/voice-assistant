import pathlib
import os

directory = pathlib.Path.cwd()


def open_file(system, file_name_type):
    (filename, filetype) = select_file_type(file_name_type)

    if system == 'Windows':
        os.system(f'explorer {directory}\\files\\{filename}.pdf')
    elif system == 'Darwin':
        os.system(f'open {directory}/files/{filename}')
    else:
        system.system(f'xdg-open {directory}/files/{filename}')


def select_file_type(file_name_type):
    supported_filetypes = ['pdf', 'audio', 'word', 'excel']

    for filetype in supported_filetypes:
        if filetype in file_name_type:
            filename = file_name_type.replace(filetype, '').strip()
            return filename, filetype

    raise NotImplementedError('You tried to open unsupported type of file or type is not recognized')
