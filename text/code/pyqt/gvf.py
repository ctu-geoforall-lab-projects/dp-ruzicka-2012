import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class GraphicsView(QGraphicsView):
    '''
        Vytvoreni vlastniho pohledu A.
    '''
    def __init__(self,  parent = None):
        super(GraphicsView,  self).__init__(parent)
        # umoznuje vybirani nekolika objektu naraz
        self.setDragMode(QGraphicsView.RubberBandDrag)
        # vyhlazovani hran
        self.setRenderHint(QPainter.Antialiasing)
        
    'Umoznuje rotaci. WheelEvent je volan vzdy, kdyz tocime koleckem na mysi.'
    def wheelEvent(self, event):
        # ten faktor je prevzat z knihy
        factor = 1.41 ** (-event.delta() / 240.0) # event.delta() vraci hodnotu, o kolik se kolecko pootocilo. (+znamena, ze bylo toceno od uzivatele, -bylo toceno k uzivateli)
        self.scale(factor, factor)
        
    def mouseDoubleClickEvent(self, event):
        dlg = QMessageBox(self)
        dlg.show()

def main():
    """
        Hlavni funkce, kde se vytvori pohled s scenou naplenou zakladnimi grafickymi 2D prvky.
    """
    app = QApplication(sys.argv)

    dlg = QDialog()
    lt = QHBoxLayout()
    scene = QGraphicsScene()
    
    # obdelnik
    rect = QGraphicsRectItem(0, 0, 40, 40)
    rect.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
    rect.setPos(0, 0)
    scene.addItem(rect)
    rectM = QGraphicsRectItem(10, 10, 10, 10,  rect)
    rectM.setBrush(QColor(255, 0, 0, 127))
    rectM.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
    
    rect2 = QGraphicsRectItem(0, 0, 20, 20)
    rect2.setPen(QPen(Qt.red))
    rect2.setBrush(QColor(255, 220, 10, 127))
    rect2.setPos(50, 50)
    scene.addItem(rect2)
    
    
    pa = QPainterPath(QPointF(0,  50))
    pa.cubicTo(90,  20, 100, 70,  100, 10)
    path = QGraphicsPathItem(pa)
    scene.addItem(path)
    view = QGraphicsView()
    view2 = GraphicsView()
    lt.addWidget(view)
    lt.addWidget(view2)
    dlg.setLayout(lt)
    view.setScene(scene)
    view2.setScene(scene)
    # umoznuje vybirani nekolika objektu naraz
    view2.setBackgroundBrush(QColor(55, 220, 10, 127))
    view2.scale(0.4, 0.7)
    view2.rotate(45)
#    view2.setDragMode(QGraphicsView.RubberBandDrag)
    # vyhlazovani hran
#    view2.setRenderHint(QPainter.Antialiasing)

    
    dlg.show()
    
    app.exec_()

main()
