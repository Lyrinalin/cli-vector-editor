import cmd
from shapes import Point, Line, Circle, Square
from editor import VectorEditor

class VectorEditorCLI(cmd.Cmd):
    intro = 'Добро пожаловать в CLI Векторный Редактор. Введите help или ? для списка команд.\n'
    prompt = '(vector-editor) '

    def __init__(self):
        super().__init__()
        self.editor = VectorEditor()

    def do_add_point(self, arg):
        """Добавить точку: add_point <x> <y>"""
        try:
            x, y = map(float, arg.split())
            shape = Point(x, y)
            idx = self.editor.add_shape(shape)
            print(f"Добавлена фигура [{idx}]: {shape}")
        except ValueError:
            print("Ошибка: неверные аргументы. Использование: add_point <x> <y>")

    def do_add_line(self, arg):
        """Добавить отрезок: add_line <x1> <y1> <x2> <y2>"""
        try:
            x1, y1, x2, y2 = map(float, arg.split())
            shape = Line(x1, y1, x2, y2)
            idx = self.editor.add_shape(shape)
            print(f"Добавлена фигура [{idx}]: {shape}")
        except ValueError:
            print("Ошибка: неверные аргументы. Использование: add_line <x1> <y1> <x2> <y2>")

    def do_add_circle(self, arg):
        """Добавить круг: add_circle <x> <y> <radius>"""
        try:
            x, y, r = map(float, arg.split())
            if r <= 0:
                print("Ошибка: радиус должен быть положительным.")
                return
            shape = Circle(x, y, r)
            idx = self.editor.add_shape(shape)
            print(f"Добавлена фигура [{idx}]: {shape}")
        except ValueError:
            print("Ошибка: неверные аргументы. Использование: add_circle <x> <y> <radius>")

    def do_add_square(self, arg):
        """Добавить квадрат: add_square <x> <y> <side>"""
        try:
            x, y, side = map(float, arg.split())
            if side <= 0:
                print("Ошибка: длина стороны должна быть положительной.")
                return
            shape = Square(x, y, side)
            idx = self.editor.add_shape(shape)
            print(f"Добавлена фигура [{idx}]: {shape}")
        except ValueError:
            print("Ошибка: неверные аргументы. Использование: add_square <x> <y> <side>")

    def do_list(self, arg):
        """Вывести список всех фигур: list"""
        shapes = self.editor.list_shapes()
        if not shapes:
            print("Список фигур пуст.")
        else:
            print("Список фигур:")
            for i, shape in enumerate(shapes):
                print(f"  [{i}] {shape}")

    def do_remove(self, arg):
        """Удалить фигуру по ID (индексу): remove <id>"""
        try:
            idx = int(arg)
            if self.editor.remove_shape(idx):
                print(f"Фигура с ID {idx} успешно удалена.")
            else:
                print(f"Ошибка: фигуры с ID {idx} не существует.")
        except ValueError:
            print("Ошибка: неверный аргумент. Использование: remove <id>")

    def emptyline(self):
        """Не повторяет последнюю команду при пустом вводе."""
        pass

    def do_EOF(self, arg):
        """Выйти по Ctrl+D (EOF)."""
        print()
        return True

    def do_exit(self, arg):
        """Выйти из редактора: exit"""
        print("До свидания!")
        return True

    def do_quit(self, arg):
        """Выйти из редактора: quit"""
        return self.do_exit(arg)

if __name__ == '__main__':
    VectorEditorCLI().cmdloop()
