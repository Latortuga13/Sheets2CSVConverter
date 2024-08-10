Hi this is an application that takes a google sheets file and turns it into a csv which can be
parsed or dealt with. In order to run the application one must use the command in your terminal in the following
format "python SheetToCSV.py 'your config'.json". In order to run, the app requires a config file which should 
be setup in this format.

{
    "SCOPES": ["https://www.googleapis.com/auth/spreadsheets"],
    "SPREADSHEET_ID": "1qV9zRkN0JDBTV7KB7dnKkMF-rRIf7dtsT1PeSICdKns",
    "SAMPLE_RANGE_NAME": "A1:C4",
    "UPDATE_RANGE": "A5",
    "CLEAR_RANGE": "A5"
}

You will be required to update the SpreadSheet ID in order to access the spreadsheet you desire.
This can be done by going to the spreadsheet on your web browser and going over to the url (it
should be the second to last section where sections are designated by /). 

example url:
https://docs.google.com/spreadsheets/d/1qV9zRkN0JDBTV7KB7dnKkMF-rRIf7dtsT1PeSICdKns/edit?gid=0#gid=0

1qV9zRkN0JDBTV7KB7dnKkMF-rRIf7dtsT1PeSICdKns -> is your SpreadSheet ID.

SAMPLE_RANGE_NAME is a range of values you can expect the app to print, where it will print all
vaues from the columns specified. In this example, the code will print values from columns A and C.
If you require a range, you can specify that with the numbers. If the numbers are the same, only 
the row specified will print (A1:C1 will print only the 1st row value from each column vs A4:C1 or A1:C4
will print all the values in each column from the 1st to the fourth row). 

UPDATE_RANGE is a value you can edit to allow the program to update your google sheets. The value 
is the specific cell you want to edit in the sheet. Both UPDATE and CLEAR range can be put as a range 
like SAMPLE_RANGE_NAME.

CLEAR_RANGE is a value that tells the app which cell you would like to remove the information 
from. Both UPDATE and CLEAR range can be put as a range like SAMPLE_RANGE_NAME.

Finally, the application I created outputs a CSV of the entire spreadsheet in a file called output.csv when
you run your python SheetToCSV.py 'your config file".json command. This file should be in the same
directory as the application.

After this is done. Follow the steps at the following url to create your own credential file.

https://developers.google.com/drive/api/quickstart/python

and add my sheet2CSV converter instead of the sample quickstart code given, the sheettocsv.py file should
return a csv file after running the "python SheetToCSV.py 'your config'.json" command.

