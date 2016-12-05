import xlrd
from zipfile import ZipFile

datafile = "./XLRD/2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    max = sheet.cell_value(1, 1)
    min = sheet.cell_value(1, 1)
    sum = 0.0
    for r in range(sheet.nrows):
        if r is not 0:
            if max < sheet.cell_value(r, 1):
                max = sheet.cell_value(r, 1)
                maxdate = sheet.cell_value(r, 0)
            if min > sheet.cell_value(r, 1):
                min = sheet.cell_value(r, 1)
                mindate = sheet.cell_value(r, 0)
            sum = sum + sheet.cell_value(r, 1)

    avg = sum / (sheet.nrows - 1)
    print max, "  ", min, " ", avg

    # ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)



    data = {
        'maxtime': (0, 0, 0, 0, 0, 0),
        'maxvalue': 0,
        'mintime': (0, 0, 0, 0, 0, 0),
        'minvalue': 0,
        'avgcoast': 0
    }

    data['avgcoast'] = avg
    data['maxvalue'] = max
    data['minvalue'] = min
    data['maxtime'] = xlrd.xldate_as_tuple(maxdate, 0)
    data['mintime'] = xlrd.xldate_as_tuple(mindate, 0)

    return data


def test():
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()