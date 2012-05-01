import sys
import cPickle
import pickle

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class editStud(QWidget):
    """
        Widget, ktery se objevi pri editaci dat.
    """
    def __init__(self, index, parent=None):
        super(editStud, self).__init__(parent) 
        self.index = index
        self.setFocusPolicy(Qt.StrongFocus)
        self.setAutoFillBackground(True)
        self.layout = QHBoxLayout()
        self.layout.setMargin(0)
        self._initGui()

    def _initGui(self):
        name = QLineEdit(self.index.data().toString())
        age = QSpinBox()
        age.setValue(self.index.data(Qt.UserRole+4).toInt()[0])
        self.layout.addWidget(name)
        self.layout.addWidget(age)
        self.setLayout(self.layout)

    def age(self):
        for child in self.children():
            if isinstance(child, QSpinBox):
                return child.value()
        return False

    def name(self):
        for child in self.children():
            if isinstance(child, QLineEdit):
                return child.text()
        return False

class Delegate(QItemDelegate):
    """
        Pomoci tohoto delegata nastavime, aby se student vypisoval modre 
        a studentka cervene. Dale nastavime, aby se pri editaci objevil 
        radek pro editaci jmena studenta(ky) a QSpinBox pro editaci veku.
    """
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        # nastaveni widgetu pro editaci dat
        editor = editStud(index, parent)
        return editor
    
    def setModelData(self, editor, model, index):
        # aktualizace dat v modelu podle editace
        model.setData(index,QVariant(editor.name()))
        model.setData(index,QVariant(editor.age()), Qt.UserRole+4)
        sIndex = model.mapToSource(index)
        toolTip = "<b>vek</b>: {0} <b>pohlavi</b>: {1}". \
            format(index.data(Qt.UserRole+4).toInt()[0], index.data(Qt.UserRole+3).toString())
        model.setData(index,QVariant(toolTip), Qt.ToolTipRole)

    def paint(self, painter, option, index):
        # pomoci teto funkce nastavime font jmena studentu a dale barvu jmena podle pohlavi
        painter.save()       
        
        # nastaveni fontu a barvy
        painter.setPen(QPen(Qt.black))
        painter.setFont(QFont("Times", 10, QFont.Bold))

        if index.data(Qt.UserRole + 3).toString() == "female":
            painter.setPen(QPen(Qt.red))
        elif index.data(Qt.UserRole + 3).toString() == "male":
            painter.setPen(QPen(Qt.blue))

        value = index.data(Qt.DisplayRole)
        if value.isValid():
            text = value.toString()
            painter.drawText(option.rect, Qt.AlignLeft, text)
            
        painter.restore()

class ProxyModel(QSortFilterProxyModel):
    '''
    Proxy model bude vyhledavat podle jmena, pohlavi, veku a pokoje.
    '''
    def filterAcceptsRow( self, source_row, source_parent ): 
        result = False
        
        useIndex = self.sourceModel().index(source_row,  0,  source_parent)
        
        name = self.sourceModel().data(useIndex, Qt.DisplayRole).toString()
        room = self.sourceModel().data(useIndex, Qt.UserRole+5).toString()
        age = self.sourceModel().data(useIndex, Qt.UserRole+4).toString()
        sex = self.sourceModel().data(useIndex, Qt.UserRole+3).toString()
        floor = self.sourceModel().data(useIndex, Qt.UserRole+2).toString()
        
        if ( floor ):
            result = True
        elif ( name.contains(self.filterRegExp()) ):
            result = True
        elif (room.contains(self.filterRegExp())):
            result = True
        elif (sex.contains(self.filterRegExp())):
            result = True
        elif (age.contains(self.filterRegExp())):
            result = True

        return result

        
class TreeView(QTreeView):
    """
        QTreeView for processing manager.
    """
    def __init__(self, parent=None):
        super(TreeView, self).__init__(parent)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self,  event):
        event.accept()
        
    def dragMoveEvent(self,  event):
        event.accept()
        
    def dropEvent(self,  event):
        d = event.mimeData()
        b = d.retrieveData("application/x-pf", QVariant.ByteArray)
        pfM = pickle.loads(b.toByteArray())
        event.accept()
    
    def mouseMoveEvent(self, event):
        '''
            We accept just Left Button of mouse. Then we check if we moved.
        '''
        if not (event.buttons() & Qt.LeftButton):
            return

        index = self.indexAt(event.pos())
        
        if not index.isValid():
            return

        # Keep position of index. After drop on scene we'll use it to obtain item from list of modules.
        point = event.pos()
        drag = QDrag(self)
        mime = QMimeData()        
        bstream = cPickle.dumps(point)
        mime.setData( "application/x-pf", bstream )
        drag.setMimeData(mime)

        drag.start(Qt.MoveAction)



def main():
    """
        Hlavni funkce, kde se vytvori a naplni model, vytvori a nastavi proxy server, pohled, delegat a vytvori dialog.
    """
    app = QApplication(sys.argv)
    
    # vytvoreni modelu
    #
    kolej = QStandardItemModel()
    
    # naplneni modelu daty
    #
    # vyvoreni moveho pokoje
    item = QStandardItem("801c")
    # Qt.UserRole+2 bude slouzit jako cislo patra
    item.setData(8, Qt.UserRole+2)
    # nastaveni ToolTipu napovedy, ktera se zobrazi kdyz prejedeme pres polozku
    item.setToolTip("room no. {0} on {1}. floor".format(item.data(Qt.DisplayRole).toString(), item.data(Qt.UserRole+2).toInt()[0]))
    # nastavime, aby se nemohla kolej editovat ani vybrat
    item.setEditable(False)
    item.setSelectable(False)
    # pridame pokoj do koleje/modelu
    kolej.appendRow(item)
    # vytvoreni noveho prvku, studenta, ktereho vlozime do pokoje, bude jeho potomek
    itemS = QStandardItem("Julius")
    itemS.setData("male", Qt.UserRole+3)
    itemS.setData(27, Qt.UserRole+4)
    itemS.setData(item.data(Qt.DisplayRole).toString(), Qt.UserRole+5)
    itemS.setToolTip("<b>age</b>: {0} <b>sex</b>: {1}".format(itemS.data(Qt.UserRole+4).toInt()[0], itemS.data(Qt.UserRole+3).toString()))
    item.appendRow(itemS)

    # vytvorime novy pokoj a naplnime ho studenty
    item = QStandardItem("604ab")
    item.setData(6, Qt.UserRole+2)
    item.setToolTip("room no. {0} on {1}. floor".format(item.data(Qt.DisplayRole).toString(), item.data(Qt.UserRole+2).toInt()[0]))
    item.setEditable(False)
    item.setSelectable(False)
    kolej.appendRow(item)
    itemS = QStandardItem("Maria")
    itemS.setData("female", Qt.UserRole+3)
    itemS.setData(22, Qt.UserRole+4)
    itemS.setData(item.data(Qt.DisplayRole).toString(), Qt.UserRole+5)    
    itemS.setToolTip("<b>age</b>: {0} <b>sex</b>: {1}".format(itemS.data(Qt.UserRole+4).toInt()[0], itemS.data(Qt.UserRole+3).toString()))
    item.appendRow(itemS)

    itemS = QStandardItem("Fiorenza")
    itemS.setData("female", Qt.UserRole+3)
    itemS.setData(22, Qt.UserRole+4)
    itemS.setData(item.data(Qt.DisplayRole).toString(), Qt.UserRole+5)
    itemS.setToolTip("<b>age</b>: {0} <b>sex</b>: {1}".format(itemS.data(Qt.UserRole+4).toInt()[0], itemS.data(Qt.UserRole+3).toString()))
    item.appendRow(itemS)

    # proxy model
    #
    proxyModel = ProxyModel()
    # nastaveni zdrojoveho modelu
    proxyModel.setSourceModel(kolej)
    # nebudeme rozlisovat mala/velka pismena
    proxyModel.setFilterCaseSensitivity(0)
    #proxyModel.setDynamicSortFilter(True)

    # vytvoreni pohledu(view)
    #
    kolejView = TreeView()
    # nastavime, aby se nam nezobrazovala hlavicka
    kolejView.header().setVisible(False)
    # nastavime, aby se nam strom pekne rozbaloval - samozrejmne to neni nutne
    kolejView.setAnimated(True)
    # nastavime model do pohledu
    kolejView.setModel(proxyModel)
    
    # vytvorime delegata
    #
    delegate = Delegate()
    # nastavime model do pohledu
    kolejView.setItemDelegate(delegate)
    
    # vytvorime dialog, ve kterem se vse zobrazi
    dorm = QDialog()
    layout = QVBoxLayout()
    dorm.setLayout(layout)
    # radek pro filtrovani
    filterBox = QLineEdit()
    layout.addWidget(filterBox)
    layout.addWidget(kolejView)

    # propojeni radku pro filtrovani s proxy modelem
    QObject.connect(filterBox, SIGNAL("textChanged(QString)"), proxyModel.setFilterRegExp)
    
    dorm.show()
    app.exec_()

main()

