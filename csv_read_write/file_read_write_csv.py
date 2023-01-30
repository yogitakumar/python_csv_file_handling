#!python3
import csv
with open ('./test/file_to_read.csv', mode ='r') as csv_read_file:
    csv_reader = csv.reader(csv_read_file,delimiter=',')
    
    with open('./test/file_to_write1.csv', mode='w',newline='') as csv_write_file1:
        csv_writer1 = csv.writer(csv_write_file1,delimiter=',')

        with open('./test/file_to_write2.csv', mode='w',newline='') as csv_write_file2:
            csv_writer2 = csv.writer(csv_write_file2,delimiter=',')

            for row in csv_reader:
                if row[2] == 'A' or row[2] == 'B':
                    csv_writer1.writerow(row)
                else:
                    csv_writer2.writerow(row)
                


        