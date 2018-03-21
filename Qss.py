MyPushButton = """
QPushButton {
    border: 0.5px solid #8f8f91;
    border-radius: 6px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
    min-width: 80px;
    font: 16px;
    font-family: Arial;
    
}

QPushButton:pressed {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
}

QPushButton:flat {
    border: none; /* no border for a flat push button */
}

QPushButton:default {
    border-color: navy; /* make the default button prominent */
}"""

MyLineEdit = """QLineEdit {
    border: 1.5px solid gray;
    border-radius: 10px;
    padding: 0 8px;
    background: #EEEEEE;
    selection-background-color: darkgray;
    font: 17px;
    font-family: Arial;
}"""

MyTreeView = """QTreeView {
    border: 0px;
    show-decoration-selected: 1;
    font: 16px bold;
    font-family: Arial;
    alternate-background-color: #F6FBFD;
}

QTreeView::item {
    border: 1px solid #d9d9d9;
    border-top-color: transparent;
    border-bottom-color: transparent;
}

QTreeView::item:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e7effd, stop: 1 #cbdaf1);
    border: 1px solid #bfcde4;
}

QTreeView::item:selected {
    border: 1px solid #9bc2e8;
}

QTreeView::item:selected:active{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6ea1f1, stop: 1 #567dbc);
}

QTreeView::item:selected:!active {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #6b9be8, stop: 1 #577fbf);
}
QHeaderView::section {
    background-color: transparent;
    color: #666666;
    padding-left: 4px;
    border: 1px solid #DDDDDD;
    font: 15px;
    font-family: Consolas;
}

}
"""


MyGroupBox = """

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center; /* position at the top center */
    padding: 0 3px;
    font: 18px;
    font-family: Arial;

}"""

MyLabel = """QLabel {
    font: 17px;
    font-family: "Lucida Console";
}"""

UnderLabel = """QLabel {
    font: 17px;
    font-family: "黑体";
}"""