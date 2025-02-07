import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []  # Список для хранения окружностей

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(QColor(255, 255, 0))  # Желтый цвет
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])  # Рисуем окружность

    def add_circle(self):
        diameter = random.randint(20, 100)  # Случайный диаметр
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        self.circles.append((x, y, diameter))  # Добавляем окружность в список
        self.update()  # Обновляем виджет для перерисовки


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.circle_widget = CircleWidget()  # Создаем виджет для рисования окружностей

        # Создаем компоновщик и добавляем виджеты
        layout = QVBoxLayout()
        layout.addWidget(self.circle_widget)
        layout.addWidget(self.pushButton)  # Добавляем кнопку в компоновщик

        # Устанавливаем компоновщик в центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.pushButton.clicked.connect(self.circle_widget.add_circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())