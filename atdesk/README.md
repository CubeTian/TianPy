python自动办公学习笔记
1.excel相关
    import xlrd  #xlsx_read
xlsx文件-工作薄
    xlsx = xlrd.open_workbook('文件名')
工作簿-工作表
    1.通过index(0,1,2..)
        table = xlsx.sheet_by_index(0)
    2.通过表名
        table = xlsx.sheet_by_name('表名')
工作表-值（三种方式）(例第三行第二列)
    table.cell_value(1,2)
    table.cell(1,2).value
    table.row(1)[2].value

写入
    import xlwt   #xlsx_write
新建空白工作簿-新建表-赋值
存工作簿-文件
    new_workbook = xlwt.Workbook()  #‘W’必须大写
    worksheet = new_workbook.add_sheet('表名')
    worksheet.write(0,0,'test')
    new_workbook.save('文件名')



