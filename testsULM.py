#encoding=UTF-8
from interfaz import Ui_MainWindow
from PyQt4 import QtCore, QtGui
import sys
import sqlite3

DATABASE_NAME = './preguntas.sqlite'

class TestDataModel(object):
  """ This class knows how to access the database, and is able to iterate
  over the multiple-choice question
  TODO: random questions
  """
  
  def __init__(self):
    self.conn = sqlite3.connect(DATABASE_NAME)
    self.conn.text_factory = str
    self.c = self.conn.cursor()
    self.c.execute('select * from preguntas')
  
  def get_question(self):
    while True:
      yield self.c.fetchone()

class TestUI(QtGui.QMainWindow):
  """ This is the user interface.
  """
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)


class TestData(object):
  """ This class contains the data of a single test
  , that is the 10, 20, 50 or 100 questions,
  the solution for each question and the answer given 
  by the user, if any.
  """
  
  def __init__(self):
    self.question_indexes = [] # this is to keep order only, probably useless
    self.questions = {}
    self.results = {}
    self.chosen_options = {}
    
  def add_question(self,question_index, question, choice1, choice2, choice3, choice4, right_index):
    self.question_indexes.append(question_index)
    self.questions[question_index] = (choice1, choice2, choice3, choice4)
    self.results[question_index] = right_index
    self.chosen_options[question_index] = None
    
    
def main():
  app = QtGui.QApplication(sys.argv)
  myapp = TestUI()
  myapp.show()
  sys.exit(app.exec_())
  
def test_datamodel():
  t = TestDataModel()
  iterator = t.get_question()
  for i in range(10):
    print iterator.next()
  
if __name__ == "__main__":
  main()
  #test_datamodel()
