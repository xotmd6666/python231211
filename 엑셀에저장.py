import openpyxl
from openpyxl import Workbook
import random

# 엑셀 파일 생성
workbook = Workbook()
sheet = workbook.active

# 헤더 추가
sheet.append(['제품ID', '수량', '가격'])

# 100개의 랜덤 데이터 생성 및 추가
for _ in range(100):
    product_id = random.randint(1000, 9999)
    quantity = random.randint(1, 10)
    price = round(random.uniform(10.0, 100.0), 2)
    sheet.append([product_id, quantity, price])

# 엑셀 파일 저장
file_path = 'c:\\work\\product.xlsx'
workbook.save(file_path)

print(f'파일이 {file_path} 경로에 성공적으로 저장되었습니다.')
