import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',  # Скрипт
    '--clean',  # Очистка кеша
    '--onefile',  # Один исполняемый файл
    '-F',  # Эт хз что
    '-w',  # Не использовать консоль (оконное приложение)
    '-i',  # Иконка
    'logo.ico'  # файл с иконкй
])
