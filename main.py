from pathlib import Path
import sys
from file_parser import process_folder

if __name__ == "__main__":
    folder_path = Path(sys.argv[1])
    process_folder(folder_path)