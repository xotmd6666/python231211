import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic
import sqlite3
import os.path

# 데이터베이스 파일 경로
db_file = "ProductList.db"

# 데이터베이스 연결 및 커서 생성
with sqlite3.connect(db_file) as connection:
    cursor = connection.cursor()
    # 테이블 생성: 파일이 이미 존재하는 경우 무시
    cursor.execute("CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);")

# UI 디자인 파일 로드
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 초기값 설정
        self.id = 0
        self.name = ""
        self.price = 0

        # 테이블의 각 열 너비 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)

        # 테이블의 헤더 라벨 설정
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)

        # 엔터 키로 포커스 이동 설정
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 초기 데이터 로딩
        self.getProduct()

    def addProduct(self):
        # 입력 파라미터 처리
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()

        # 제품 추가 SQL 실행
        cursor.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (self.name, self.price))

        # 데이터 갱신
        self.getProduct()

        # 커밋
        connection.commit()

    def updateProduct(self):
        # 업데이트 파라미터 처리
        self.id = self.prodID.text()
        self.name = self.prodName.text()
        self.price = self.prodPrice.text()

        # 제품 업데이트 SQL 실행
        cursor.execute("UPDATE Products SET name=?, price=? WHERE id=?;", (self.name, self.price, self.id))

        # 데이터 갱신
        self.getProduct()

        # 커밋
        connection.commit()

    def removeProduct(self):
        # 삭제 파라미터 처리
        self.id = self.prodID.text()

        # 제품 삭제 SQL 실행
        cursor.execute("DELETE FROM Products WHERE id=?;", (self.id,))

        # 데이터 갱신
        self.getProduct()

        # 커밋
        connection.commit()

    def getProduct(self):
        # 검색 결과를 보여주기 전에 기존 컨텐트를 삭제(헤더는 제외)
        self.tableWidget.clearContents()

        # 모든 제품 검색 SQL 실행
        cursor.execute("SELECT * FROM Products;")
        row = 0
        for item in cursor:
            # 각 열을 Item으로 생성해서 숫자를 오른쪽으로 정렬해서 출력
            itemID = QTableWidgetItem("{:10}".format(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)

            # 제품명은 그대로 출력
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))

            itemPrice = QTableWidgetItem("{:10}".format(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

            row += 1

    def doubleClick(self):
        # 더블클릭으로 선택한 행의 데이터를 각 LineEdit에 설정
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    sys.exit(app.exec_())