
import xlwt3

if __name__ == '__main__':
    datas = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]  # 二维数组
    file_path = '/Users/vpjacob/Desktop/Demo/03-Python\ 股票'
wb = xlwt3.Workbook()

sheet = wb.add_sheet('test')  # sheet的名称为test

# 单元格的格式
style = 'pattern: pattern solid, fore_colour yellow; '  # 背景颜色为黄色
style += 'font: bold on; '  # 粗体字
style += 'align: horz centre, vert center; '  # 居中
header_style = xlwt3.easyxf(style)

row_count = len(datas)
col_count = len(datas[0])
for row in range(0, row_count):
	col_count = len(datas[row])
	for col in range(0, col_count):
		if row == 0:  # 设置表头单元格的格式
			sheet.write(row, col, datas[row][col], header_style)
		else:
			sheet.write(row, col, datas[row][col])
wb.save(file_path)
