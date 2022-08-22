import sys
import ui


if __name__ == '__main__':
    app = ui.QApplication(sys.argv)
    w = ui.MyWidget()
    w.show()
    sys.exit(app.exec_())