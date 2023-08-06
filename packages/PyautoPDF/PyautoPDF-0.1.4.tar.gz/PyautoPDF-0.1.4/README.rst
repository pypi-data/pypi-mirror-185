Introduction
------------

PyautoPDF is a Python library to read/write Excel files which includes the format of xlsx/xlsm/xltx/xltm.

Mailing List
------------

Mail at - shaileshsuthar676@gmail.com

Sample Code::

    # import the library
    from PyautoPDF.PdfAutomationModule import PdfAutomation
    import PyautoPDF

    # create excel workbook
    wb = PyautoPDF.create_wb()

    # create a sheet at index zero in the existing workbook
    sheet1 = PyautoPDF.create_sheet(wb=wb, sheet_name='Sheet1', index=0)

    # variable declaration for sheet
    sheet1 = PdfAutomation(target_sheet=sheet1)

    # applying a methods to do the color filling task
    sheet1.color_filling(1, 1, 6, 8, 2, 1)

    # applying a methods to adjust the column width
    col_width = {'A': 10, 'B': 15, 'C': 8, 'D': 30}
    sheet1.adjust_columns(col_width=col_width)

    # saving the workbook
    wb.save('test.xlsx')

