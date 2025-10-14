import os
import threading
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
from typing import Dict


file_dir = r"C:\Users\himan\PycharmProjects\DesignInPython\src\python\learning\multithreading\output"
os.makedirs(file_dir, exist_ok=True)

LARGE_TEXT = "This is a large content block. " * 500_000_00  # ~14 MB per file

mp1: Dict[str, str] = {
    "file1.txt": LARGE_TEXT,
    "file2.txt": LARGE_TEXT,
    "file3.txt": LARGE_TEXT,
    "file4.txt": LARGE_TEXT,
    "file5.txt": LARGE_TEXT,
}

def write_file(file_name: str, content: str) :
    file_path = os.path.join(file_dir,file_name)
    thread_name = threading.current_thread().name
    print(f"{thread_name}:starting the writing in:{file_name}")
    time.sleep(1)
    with open(file_path,'w',encoding='utf-8') as f:
        f.write(content)
    print(f"{thread_name}:completed writing to file:{file_name}")
    return file_name




with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(write_file,name, content) for name, content in mp1.items()]

    for future in as_completed(futures):
        result = future.result()
        print(f"Completed writing:{result}")


    # for file_name, content in mp1.items():
    #     # print(f"key={key}:value={value}")
    #     file_path = os.path.join(file_dir, file_name)
    #     with open(file_path, "w") as file:
    #         file.write(content)

