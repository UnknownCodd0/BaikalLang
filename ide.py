import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QFont, QSyntaxHighlighter, QTextCharFormat, QColor
from PyQt5.QtCore import QRegExp
import io
import main


# 1. Класс для подсветки синтаксиса
class BaikalHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlight_rules = []

        # Правила для ключевых слов (синий цвет)
        keywords = ["Функция", "Если", "Пока", "ДляКаждого", "Вернуть", "Строка", "Число", "Переменная", "ОбъявитьДругое", "ЛогТип", "Или", "Если", "Иначе", "Ничего", "Список", "ПревратитьВЧисло", "Вид", "Ввод", "ВызватьФункцию", "СоздатьФункцию"]
        for word in keywords:
            pattern = QRegExp(f"\\b{word}\\b")
            fmt = QTextCharFormat()
            fmt.setForeground(QColor("#4682B4"))  # SteelBlue
            self.highlight_rules.append((pattern, fmt))

        # Правило для строк (зелёный)
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#2E8B57"))  # SeaGreen
        self.highlight_rules.append((QRegExp('\".*\"'), string_format))

    def highlightBlock(self, text):
        for pattern, fmt in self.highlight_rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)


# 2. Основное окно IDE
class BaikalIDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BaikalLang IDE 1.0.0")
        self.setGeometry(100, 100, 800, 600)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Редактор кода
        self.editor = QTextEdit()
        self.editor.setFont(QFont("Consolas", 12))

        # Подсветка (теперь она привязана!)
        self.highlighter = BaikalHighlighter(self.editor.document())

        # Кнопка запуска
        self.run_btn = QPushButton("Запуск (Ctrl+R)")
        self.run_btn.clicked.connect(self.run_code)

        # Разметка
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.run_btn)
        central_widget.setLayout(layout)

        # Кнопка сохранения
        self.save_btn = QPushButton("Сохранить в файл")
        self.save_btn.clicked.connect(self.save_file)

        # Добавляем кнопку в layout (рядом с "Запуск")
        layout.addWidget(self.save_btn)

    def run_code(self):
        code = io.StringIO(self.editor.toPlainText())

        try:
            main.main_body(code)

        except:
            print("Ошибка: неправильно введён код!")

    def save_file(self):
        # Получаем текст из редактора
        code = self.editor.toPlainText()

        # Диалог выбора файла
        file_path, _ = QFileDialog.getSaveFileName(
            self,  # Родительское окно
            "Сохранить файл",  # Заголовок диалога
            "",  # Начальная директория (пусто = домашняя папка)
            "BaikalLang Files (*.bkln);;All Files (*)"  # Фильтры файлов
        )

        # Если пользователь выбрал путь
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(code)
                print(f"Файл сохранён: {file_path}")  # Для отладки (видно в консоли)
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{e}")


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ide = BaikalIDE()
    ide.show()
    sys.exit(app.exec_())