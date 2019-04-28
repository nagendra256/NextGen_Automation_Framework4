import xlrd
import os


def read_test_data(file_name, sheet_name, input_data):
    path = os.getcwd()
    wb = xlrd.open_workbook(path + "\\testdata\\" + file_name)
    ws = wb.sheet_by_name(sheet_name)
    row_data = ws.nrows
    col_data = ws.ncols
    for i in range(row_data):
        for j in range(col_data):
            if input_data == ws.cell_value(i, j):
                return ws.cell_value(i + 1, j)
        break
