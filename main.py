from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import base64



class BASE64_to_file:
    def __init__(self):
        self.content = ""

        self.root = Tk()
        self.root.title("BASE64_to_file")
        self.root.geometry("400x150")
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)

        self.init_gui_elements()
        self.root.mainloop()

    def init_gui_elements(self):
        """Инициализация элементов пользовательского интерфейса"""

        ### command_panel_frame ###
        command_panel_frame = Frame(self.frame)
        command_panel_frame.config(padx=10, pady=10)
        command_panel_frame.pack(fill=BOTH, expand=1)

        source_file_patch_label = Label(command_panel_frame, text="Файл источник: ")
        source_file_patch_label.pack(side=TOP)

        source_file_patch = Label(command_panel_frame, text="Не выбран")
        source_file_patch.pack(side=TOP)

        close_button = Button(command_panel_frame, text="Открыть файл BASE64",
                              command=lambda: self.insert_text_to_memory(source_file_patch))
        close_button.pack(side=TOP)

        ### ROOT ###
        close_button = Button(self.root, text="Сохранить в файл",
                              command=lambda: self.extract_text_to_file())
        close_button.pack(side=TOP)

    @staticmethod
    def base64_to_file(content):
        return base64.b64decode(content)

    def insert_text_to_memory(self, source_file_patch):
        """Чтение теста из файла в текстовое поле"""
        file_name = filedialog.askopenfilename()
        if file_name:
            try:
                with open(file_name) as file_obj:
                    self.content = file_obj.read()
                    source_file_patch.configure(text=file_name)
            except (FileExistsError, FileNotFoundError, IOError) as err:
                messagebox.showerror(
                    "Ошибка",
                    "Ошибка при чтении/записи файла: {}".format(err))

    def extract_text_to_file(self):
        """Запись в файл"""
        file_name = filedialog.asksaveasfilename(
            filetypes=(("DOC (Документ MS Word)", ".doc"),
                       ("DOCX (Документ MS Word)", ".docx"),
                       ("XLS (Документ MS Excel)", ".xls"),
                       ("XLSX (Документ MS Excel)", ".xlsx"),
                       ("PDF (Portable Document Format)", ".pdf"),
                       ("Произвольный тип (необходимо указать)", ".*")),
            defaultextension=TRUE)

        if file_name:
            try:
                with open(file_name, 'wb') as file_obj:
                    bin_file = self.base64_to_file(self.content)
                    file_obj.write(bin_file)
                    file_obj.close()
                    messagebox.showinfo(
                        "(◠‿・)—☆",
                        "Файл успешно создан!")
            except (FileExistsError, FileNotFoundError, IOError) as err:
                messagebox.showerror(
                    "Ошибка",
                    "Ошибка при чтении/записи файла: {}".format(err))


if __name__ == "__main__":
    application = BASE64_to_file()
