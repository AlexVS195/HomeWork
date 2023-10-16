from pathlib import Path
import sys
from normalize import normalize
from file_parser import process_folder



def main():
    # Запитуємо у користувача шлях до директорії для сортування
    folder_path = input("Введіть шлях до директорії для сортування: ")
    folder_path = Path(folder_path)

    # Перевіряємо, чи існує директорія
    if folder_path.exists() and folder_path.is_dir():
        # Запускаємо функцію сортування та передаємо шлях до директорії
        process_folder(folder_path)
        print("Сортування завершено.")
    else:
        print("Директорія не існує. Перевірте введений шлях.")

if __name__ == "__main__":
    main()