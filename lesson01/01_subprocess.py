# ======================= Потоки и многозадачность ============================
# ------------------ Обзор возможностей модуля subprocess (UNIX) --------------
import glob
import subprocess
import os

cur_dir = os.getcwd()

PROGRAM = "notepad.exe"

EXT = ".txt"

print(f"Основоной процесс: {os.getpid()}")


def main():
    # При таком подходе следующая программа не запускается, пока не завершится вторая
    subprocess.run(PROGRAM)
    subprocess.run(['ping', '8.8.8.8'], creationflags=subprocess.CREATE_NEW_CONSOLE)


def pope_test():
    # "Popen" позволяет запустить новый препроцесс и не нужно ждать завершение, чтобы запустить следующий
    process1 = subprocess.Popen(PROGRAM)
    print(f"Дочерний процесс 1: {process1.pid}")
    # Но можно принудительно заставит процесс ждать своего завершения
    # code = process1.wait()
    # print(code)

    process2 = subprocess.Popen(['ping', '8.8.8.8'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    print(f"Дочерний процесс 2: {process2.pid}")
    # Возможность общаться с процессом и передавать или получать данные
    data = process2.communicate()
    print(data)


def zip_files():
    files = [f.name for f in os.scandir() if f.is_files() and f.name.endswith(EXT)]
    # files = [file for file in glob.glob(cur_dir + '\\*') if file.endswith((EXT))]
    print('Файлы для упаковки: ', files)

    packer = subprocess.Popen(['tar.exe', ['a', 'c', 'f'], 'test.zip', *files],
                              shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)

    # with subprocess.Popen(['tar.exe', ['a', 'c', 'f'], 'test.zip', *files],
    #                       shell=True,
    #                       stdout=subprocess.PIPE,
    #                       stderr=subprocess.PIPE) as packer:
    #     print("Ждём упаковку...")

    print(f'Дочерний процесс: {packer.pid}')

    packer.wait()
    packer.communicate()


if __name__ == '__main__':
    pope_test()
    print('Программа завершена')
