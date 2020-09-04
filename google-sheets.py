#pip install ezsheets
#https://console.developers.google.com/apis/library/sheets.googleapis.com to enable the api
#https://console.developers.google.com/apis/library/drive.googleapis.com to enable api
#https://developers.google.com/sheets/api/quickstart/python/ for the credentials file to put in the working directory.
#Rename credential.json file to credential-sheets.json
import ezsheets #Running this for the first time with the credential-sheets.json will open your browser to grant the app access to your drive

#Create a new spreadsheet
ss = ezsheets.createSpreadsheet('Test')
print(ss.spreadsheetId)
print(ss.title)
print(ss.url)
print(ss.sheetTitles)
print(ss.sheets)

#Get first sheet
sheet=ss[0]

#Change title
sheet.title='Test Data'

#Set header row
sheet['A1'] = 'Name'
sheet['B1'] = 'Age'
sheet['C1'] = 'Occupation'

#Set a row
sheet['A2'] = 'Bob'
sheet['B2'] = 40
sheet['C2'] = 'Engineer'

#Work with an entire row
print(sheet.getRow(2))
sheet.updateRow(2, ['Bob', 41, 'Engineer'])
print(sheet.getRow(2))

#Work with an entire column
print(sheet.getColumn(1))
sheet.updateColumn(1, ['First Name', 'Bob'])
print(sheet.getColumn(1))

#Get all the rows
rows = sheet.getRows()
for row in rows:
	for column in row:
		print(column)

#Counts
print(sheet.rowCount)
print(sheet.columnCount)

#Create a new sheet
ss.createSheet('Test Data - 2')
print(ss.sheetTitles)

#Copy the first sheet
sheet.copyTo(ss)

#Refresh the data
ss.refresh()


#Download as Test.xlsx
ss.downloadAsExcel()

#Delete
ss.delete()

#Check to see if spreedsheet is gone
print(ezsheets.listSpreadsheets())

#Uploads the downloaded file
ss = ezsheets.upload('Test.xlsx')

#Check to see if spreedsheet is uploaded
print(ezsheets.listSpreadsheets())

ss.delete()




