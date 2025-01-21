import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Открыть диалоговое окно для выбора файла
Tk().withdraw()  # Скрыть главное окно
filename = askopenfilename(filetypes=[("Excel files", "*.xlsx")])

if filename:
    # Загрузить файл Excel
    df = pd.read_excel(filename)

    # Получить названия колонок
    column_names = df.columns.tolist()
    
    print("Названия колонок в файле:")
    for col in column_names:
        print(col)
