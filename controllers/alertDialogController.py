from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from enum import Enum

from views import *
import utils

class AlertDialog(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_alertDialog()
        self.ui.setupUi(self)
        self.app = QApplication.instance()
        self.extra = {
            # Button colors
            'danger':  '#dc3545',
            'warning': '#ffc107',
            'success': '#1ff29a',
            # Font
            'font_family': 'Fira Code',
        }
        # utils.css_utils.load_stylesheet(self.app,theme='dark_purple.xml',extra=self.extra)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
    
    def accept(self):
        super().accept()
    
    def reject(self):
        super().reject()

class AlertType(Enum):
    SUCCESS = 'Success'
    INFORMATION = 'Information'
    WARNING = 'Warning'

class IconType(Enum):
    SUCCESS = ':/images/assets/images/state-success.svg'
    INFORMATION = ':/images/assets/images/state-information.svg'
    WARNING = ':/images/assets/images/state-warning.svg'
    
class AlertButton(Enum):
    SUCCESS = QDialogButtonBox.Ok
    INFORMATION = QDialogButtonBox.Ok
    WARNING = QDialogButtonBox.Ok

class Alerts():
    dialog = None
    @staticmethod
    def Show(alert_type:AlertType,alert_title,alert_body,alert_icon:IconType,alert_buttons:AlertButton):
        if Alerts.dialog is None:
            Alerts.dialog = AlertDialog()
        Alerts.dialog.setWindowTitle(alert_type.value)
        Alerts.dialog.ui.titleLbl.setText(alert_title)
        Alerts.dialog.ui.bodyLbl.setText(alert_body)
        Alerts.dialog.ui.iconLbl.setPixmap(QPixmap(alert_icon.value))
        Alerts.dialog.ui.buttonBox.setStandardButtons(alert_buttons.value)
        Alerts.dialog.exec_()