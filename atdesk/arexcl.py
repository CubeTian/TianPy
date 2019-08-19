import xlwt
new_workbook = xlwt.Workbook()  #‘W’必须大写
worksheet = new_workbook.add_sheet('1')
worksheet.write(0,0,'test')
new_workbook.save('atdesk/wttest.xlsx')
