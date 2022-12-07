from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class SelectGroupWindowBase(QWidget):
    def __init__(self, *args, **kwargs):
        super(SelectGroupWindowBase, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.Window)

        self.setObjectName("object_name")
        self.setWindowTitle("window_title")

        main_layout = QFormLayout(self)
        selection_layout = QHBoxLayout(self)
        list_layout = QVBoxLayout(self)
        radio_layout = QVBoxLayout(self)
        box_layout = QGridLayout(self)

        main_layout.addRow(list_layout)
        main_layout.addRow(selection_layout)
        main_layout.addRow(radio_layout)
        main_layout.addRow(box_layout)

        self.create_button = QPushButton("create",self)
        self.rename_button = QPushButton("rename",self)
        self.delete_button = QPushButton("delete",self)
        
        self.set_button = QPushButton("set",self)
        self.add_button = QPushButton("add",self)
        self.edit_button = QPushButton("edit",self)
        self.import_button = QPushButton("import",self)
        self.export_button = QPushButton("export",self)
        self.file_button = QPushButton("file",self)
        self.all_export_button = QPushButton("all export",self)

        self.selections_radio = QRadioButton("selections",self)
        self.connections_radio = QRadioButton("connections",self)
        self.parent_childs_radio = QRadioButton("parent<childs",self)
        self.parents_child_radio = QRadioButton("child<parents",self)
        self.lists_radio = QRadioButton("lists",self)

        #self.list_table = QTableView(self)
        self.selection_view = QListView(self)
        self.model = QStringListModel(self)
        self.model.setStringList(["aaa", 'bbb', 'ccc'])
        self.selection_view.setModel(self.model)
        
        selection_layout.addWidget(self.create_button)
        selection_layout.addWidget(self.rename_button)
        selection_layout.addWidget(self.delete_button)

        list_layout.addWidget(self.selection_view)
        radio_layout.addWidget(self.selections_radio)
        radio_layout.addWidget(self.connections_radio)
        radio_layout.addWidget(self.parent_childs_radio)
        radio_layout.addWidget(self.parents_child_radio)
        radio_layout.addWidget(self.lists_radio)

        box_layout.addWidget(self.set_button,0,0)
        box_layout.addWidget(self.add_button,0,1)
        box_layout.addWidget(self.edit_button,0,2)
        box_layout.addWidget(self.import_button,1,0)
        box_layout.addWidget(self.export_button,1,1)
        box_layout.addWidget(self.file_button,1,2)
        box_layout.addWidget(self.all_export_button,2,0,2,3)

        self.create_button.clicked.connect(self.create_button_onClicked)
        self.rename_button.clicked.connect(self.rename_button_onClicked)
        self.delete_button.clicked.connect(self.delete_button_onClicked)
        self.set_button.clicked.connect(self.set_button_onClicked)
        self.add_button.clicked.connect(self.add_button_onClicked)
        self.edit_button.clicked.connect(self.edit_button_onClicked)
        self.import_button.clicked.connect(self.import_button_onClicked)
        self.export_button.clicked.connect(self.export_button_onClicked)
        self.file_button.clicked.connect(self.file_button_onClicked)
        self.all_export_button.clicked.connect(self.all_export_button_onClicked)

    def create_button_onClicked(self):
        print("base")
    def rename_button_onClicked(self):
        print("base")
    def delete_button_onClicked(self):
        print("base")
    def set_button_onClicked(self):
        print("base")
    def add_button_onClicked(self):
        print("base")
    def edit_button_onClicked(self):
        print("base")
    def import_button_onClicked(self):
        print("base")
    def export_button_onClicked(self):
        print("base")
    def file_button_onClicked(self):
        print("base")
    def all_export_button_onClicked(self):
        print("base")

#window_instance = MgearDictWindow()
#window_instance.show()

