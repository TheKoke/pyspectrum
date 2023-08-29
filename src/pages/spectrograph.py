from business.analysis import SpectrumAnalyzer

from pages.workbooker import Workbooker
from pages.calibration import CalibrationWindow

from matplotlib.figure import Figure
from matplotlib.backend_bases import MouseEvent, MouseButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT

from PyQt5.QtGui import QFont, QIcon, QPalette, QBrush, QColor
from PyQt5.QtCore import Qt, QSize, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QVBoxLayout, 
    QComboBox, QHBoxLayout, QPushButton, 
    QFrame, QLabel, QFileDialog
)


class Ui_Spectrograph(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        MainWindow.setMinimumSize(QSize(1300, 900))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QPushButton{\nbackground-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);\n}\nQPushButton:pressed{\nbackground-color: rgb(55, 55, 97);\n}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.matplotlib_layout = QFrame(self.centralwidget)
        self.matplotlib_layout.setMinimumSize(QSize(880, 880))
        self.matplotlib_layout.setMaximumSize(QSize(2000, 1760))
        self.matplotlib_layout.setFrameShape(QFrame.StyledPanel)
        self.matplotlib_layout.setFrameShadow(QFrame.Raised)
        self.matplotlib_layout.setObjectName("matplorlib_layout")
        self.horizontalLayout.addWidget(self.matplotlib_layout)
        self.services_layout = QFrame(self.centralwidget)
        self.services_layout.setMinimumSize(QSize(400, 880))
        self.services_layout.setMaximumSize(QSize(800, 1760))
        self.services_layout.setFrameShape(QFrame.StyledPanel)
        self.services_layout.setFrameShadow(QFrame.Raised)
        self.services_layout.setObjectName("services_layout")
        self.verticalLayout = QVBoxLayout(self.services_layout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.particle_layout = QHBoxLayout()
        self.particle_layout.setObjectName("particle_layout")
        self.particle_label = QLabel(self.services_layout)
        self.particle_label.setMinimumSize(QSize(42, 0))
        self.particle_label.setMaximumSize(QSize(85, 16777215))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.particle_label.setFont(font)
        self.particle_label.setObjectName("particle_label")
        self.particle_layout.addWidget(self.particle_label)
        self.particle_box = QComboBox(self.services_layout)
        self.particle_box.setMinimumSize(QSize(0, 30))
        self.particle_box.setMaximumSize(QSize(16777215, 45))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 120, 215))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        self.particle_box.setPalette(palette)
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.particle_box.setFont(font)
        self.particle_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.particle_box.setObjectName("particle_box")
        self.particle_layout.addWidget(self.particle_box)
        self.verticalLayout.addLayout(self.particle_layout)
        self.angle_layout = QHBoxLayout()
        self.angle_layout.setObjectName("angle_layout")
        self.angle_label = QLabel(self.services_layout)
        self.angle_label.setMinimumSize(QSize(42, 0))
        self.angle_label.setMaximumSize(QSize(85, 16777215))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.angle_label.setFont(font)
        self.angle_label.setObjectName("angle_label")
        self.angle_layout.addWidget(self.angle_label)
        self.angle_box = QComboBox(self.services_layout)
        self.angle_box.setMinimumSize(QSize(0, 30))
        self.angle_box.setMaximumSize(QSize(16777215, 45))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(85, 85, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        brush = QBrush(QColor(0, 120, 215))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush)
        self.angle_box.setPalette(palette)
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.angle_box.setFont(font)
        self.angle_box.setStyleSheet("background-color: rgb(85, 85, 127);\ncolor: rgb(255, 255, 255);")
        self.angle_box.setObjectName("angle_box")
        self.angle_layout.addWidget(self.angle_box)
        self.verticalLayout.addLayout(self.angle_layout)
        self.calibrate_button = QPushButton(self.services_layout)
        self.calibrate_button.setMinimumSize(QSize(0, 90))
        self.calibrate_button.setMaximumSize(QSize(16777215, 180))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calibrate_button.setFont(font)
        self.calibrate_button.setObjectName("calibrate_button")
        self.verticalLayout.addWidget(self.calibrate_button)
        self.peaks_button = QPushButton(self.services_layout)
        self.peaks_button.setMinimumSize(QSize(0, 90))
        self.peaks_button.setMaximumSize(QSize(16777215, 180))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.peaks_button.setFont(font)
        self.peaks_button.setObjectName("peaks_button")
        self.verticalLayout.addWidget(self.peaks_button)
        self.impurity_button = QPushButton(self.services_layout)
        self.impurity_button.setMinimumSize(QSize(0, 90))
        self.impurity_button.setMaximumSize(QSize(16777215, 180))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.impurity_button.setFont(font)
        self.impurity_button.setObjectName("impurity_button")
        self.verticalLayout.addWidget(self.impurity_button)
        self.workbook_button = QPushButton(self.services_layout)
        self.workbook_button.setMinimumSize(QSize(0, 90))
        self.workbook_button.setMaximumSize(QSize(16777215, 180))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workbook_button.setFont(font)
        self.workbook_button.setObjectName("workbook_button")
        self.verticalLayout.addWidget(self.workbook_button)
        self.ladder_button = QPushButton(self.services_layout)
        self.ladder_button.setMinimumSize(QSize(0, 90))
        self.ladder_button.setMaximumSize(QSize(16777215, 180))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ladder_button.setFont(font)
        self.ladder_button.setObjectName("ladder_button")
        self.verticalLayout.addWidget(self.ladder_button)
        self.save_button = QPushButton(self.services_layout)
        self.save_button.setMinimumSize(QSize(0, 90))
        self.save_button.setMaximumSize(QSize(16777215, 180))
        font = QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.horizontalLayout.addWidget(self.services_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "dSigma — Spectra Window"))
        self.particle_label.setText(_translate("MainWindow", "Particle:"))
        self.angle_label.setText(_translate("MainWindow", "Angle:"))
        self.calibrate_button.setText(_translate("MainWindow", "Calibrate"))
        self.peaks_button.setText(_translate("MainWindow", "Show Peaks"))
        self.impurity_button.setText(_translate("MainWindow", "Validate Impurities"))
        self.workbook_button.setText(_translate("MainWindow", "Open Workbook"))
        self.ladder_button.setText(_translate("MainWindow", "Build Ladder View"))
        self.save_button.setText(_translate("MainWindow", "Save as .txt"))


class LadderViewer(QWidget):
    def __init__(self, spectra: SpectrumAnalyzer) -> None:
        # SETUP OF WINDOW
        super().__init__()
        self.setWindowTitle('dSigma — Ladder/Kinematics viewer')
        self.setWindowIcon(QIcon("./icon.ico"))

        # DATA
        self.spectra = spectra

        # MATPLOTLIB INITIALIZING
        layout = QVBoxLayout(self)
        self.view = FigureCanvasQTAgg(Figure(figsize=(16, 9)))
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)

        self.draw()

    def draw(self) -> None:
        allrange = self.spectra.spectrums[:]
        mean = sum([sp.data.mean() for sp in allrange]) / len(allrange)

        self.axes.clear()
        for i in range(len(allrange)):
            self.axes.plot(list(range(1, len(allrange[i].data) + 1)), allrange[i].data + allrange[i].angle * mean, color='blue')

        self.view.draw()


class Spectrograph(QMainWindow, Ui_Spectrograph):
    def __init__(self, analitics: list[SpectrumAnalyzer]) -> None:
        # WINDOW SETUP
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("./icon.ico"))

        self.analitics = analitics
        self.current_index = 0
        
        self.pointers = []

        # MATPLOTLIB INITIALIZING
        layout = QVBoxLayout(self.matplotlib_layout)
        self.view = FigureCanvasQTAgg(Figure(figsize=(16, 9)))
        self.view.mpl_connect('button_press_event', self.add_pointer)
        self.axes = self.view.figure.subplots()
        self.toolbar = NavigationToolbar2QT(self.view, self.matplotlib_layout)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.view)

        # EVENT HANDLING
        self.angle_box.currentTextChanged.connect(self.draw_angle)
        self.angle_box.currentTextChanged.connect(self.pointers.clear)
        self.particle_box.currentTextChanged.connect(self.take_current)
        particles = [analyzer.spectrums[0].reaction.fragment for analyzer in self.analitics]
        self.particle_box.addItems([str(p) for p in particles])

        self.calibrate_button.clicked.connect(self.open_calibration)
        self.peaks_button.clicked.connect(self.show_peaks)
        self.impurity_button.clicked.connect(self.validate_impurities)
        self.workbook_button.clicked.connect(self.open_workbook)
        self.ladder_button.clicked.connect(self.build_ladder)
        self.save_button.clicked.connect(self.save)

    def add_pointer(self, event: MouseEvent) -> None:
        if event.button == MouseButton.LEFT and event.dblclick:
            if len(self.pointers) < 2:
                self.pointers.append(int(event.xdata))
            else:
                self.pointers.pop(0)
                self.pointers.append(int(event.xdata))

            self.draw_pointers()

    def draw_pointers(self) -> None:
        angle = self.angle_box.currentIndex()
        analitics = self.analitics[self.current_index]
        maximum = analitics.spectrums[angle].data.max()
        
        self.draw_angle()
        for i in range(len(self.pointers)):
            self.axes.plot([self.pointers[i], self.pointers[i]], [0, maximum], color='red')

        self.view.draw()

    def open_calibration(self) -> None:
        angle = self.angle_box.currentIndex()
        analitics = self.analitics[self.current_index]

        self.window = CalibrationWindow(analitics, angle)
        self.window.show()

    def show_peaks(self) -> None:
        angle_index = self.angle_box.currentIndex()
        spectrum = self.analitics[self.current_index].spectrums[angle_index]

        if spectrum.is_calibrated and len(spectrum.peaks) == 0:
            self.analitics[self.current_index].approximate(angle_index)

        self.draw_angle()

    def validate_impurities(self) -> None:
        pass

    def open_workbook(self) -> None:
        angle_index = self.angle_box.currentIndex()
        spectrum = self.analitics[self.current_index].spectrums[angle_index]

        self.window = Workbooker(spectrum.to_workbook())
        self.window.show()

    def build_ladder(self) -> None:
        self.window = LadderViewer(self.analitics[self.current_index])
        self.window.show()

    def save(self) -> None:
        name, _ = QFileDialog.getSaveFileName(self, 'Save File', filter='TXT Documents (*.txt)')
        if name == '':
            return
        
        angle = self.angle_box.currentIndex()
        analitics = self.analitics[self.current_index]
        spectrum = analitics.spectrums[angle].data

        txt = open(name, 'w')
        for i in range(len(spectrum)):
            print(f'{i + 1}\t{spectrum[i]}', file=txt)

        txt.close()

    def take_current(self) -> None:
        self.current_index = int(self.particle_box.currentIndex())
        angles = [spectrum.angle for spectrum in self.analitics[self.current_index].spectrums]

        self.angle_box.clear()
        self.angle_box.addItems([str(a) for a in angles])

    def draw_angle(self) -> None:
        angle_index = self.angle_box.currentIndex()
        spectrum = self.analitics[self.current_index].spectrums[angle_index]

        self.axes.clear()
        
        for i in range(len(spectrum.data)):
            self.axes.plot([i + 1, i + 1], [0, spectrum.data[i]], color='blue')

        for peak in spectrum.peaks.values():
            self.axes.plot(peak.three_sigma(), peak.function(), color='red')
        
        self.axes.plot(list(range(1, len(spectrum.data) + 1)), spectrum.data, color='blue')
        self.view.draw()


if __name__ == '__main__':
    pass
