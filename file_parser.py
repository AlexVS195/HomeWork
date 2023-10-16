from pathlib import Path
from normalize import normalize
import shutil

def handle_media(file_name: Path, target_folder: Path):
    # Обробка медіа-файлів: створюємо папку та перейменовуємо файл
    target_folder.mkdir(exist_ok=True, parents=True)
    new_name = target_folder / normalize(file_name.name)
    file_name.replace(new_name)

def handle_archive(file_name: Path, target_folder: Path):
    # Обробка архівів: розпаковуємо та організовуємо файли
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.stem)
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()

# Функція для обробки папки та файлів в ній
def process_folder(folder: Path):
    for item in folder.iterdir():
        if item.is_dir() and item.name not in ('archives', 'video', 'audio', 'documents', 'images'):
            process_folder(item)
        elif item.is_file():
            extension = item.suffix[1:].upper()
            new_name = normalize(item.stem)
            target_folder = determine_target_folder(extension, folder)
            move_and_rename_file(item, target_folder, new_name)

# Визначення папки, в яку треба перенести файл
def determine_target_folder(extension, folder):
    if extension in ('JPEG', 'JPG', 'PNG', 'SVG'):
        return folder / 'images'
    elif extension in ('AVI', 'MP4', 'MOV', 'MKV'):
        return folder / 'video'
    elif extension in ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'):
        return folder / 'documents'
    elif extension in ('MP3', 'OGG', 'WAV', 'AMR'):
        return folder / 'audio'
    elif extension in ('ZIP', 'GZ', 'TAR'):
        return folder / 'archives'
    else:
        return folder / 'unknown'

# Перейменовання та переміщення файлу
def move_and_rename_file(source, target_folder, new_name):
    target_folder.mkdir(parents=True, exist_ok=True)
    new_name_with_extension = new_name + source.suffix
    source.rename(target_folder / new_name_with_extension)