from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os
import logging
 
# Create and configure logger
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"]="--no-sandbox"


baseDir = os.path.dirname(__file__)

from controllers import *
from utils.utils import *

def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    myApp = MyApp()
    myApp.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()