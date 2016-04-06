# csv file format conversion
# input file has header and no quotation marks around data
# desired output has no header and quotation marks around data 
# line terminator characters set for Linux environment

# import packages into the workspace for this program
from __future__ import division, print_function
import csv  # package from Python standard library

with open('xyz_test_item_excel_header.csv', 'r') as file_in:
    reader = csv.reader(file_in, delimiter = ',')
    with open('xyz_test_item_postgres.csv', 'w') as file_out:
        writer = csv.writer(file_out, quoting = csv.QUOTE_ALL, 
            quotechar = "'", lineterminator = "\n")
        for row in reader:
            if reader.line_num != 1: # write all but header row
                writer.writerow(row)
            


