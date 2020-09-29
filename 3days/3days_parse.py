import csv

def calc_change(data):
    for i in range(1, len(data) - 3):
        val_after = float(data[i][-2])
        val_before = float(data[i + 3][-2])
        data[i].append(val_after/val_before)
    data[0].append('3days_before_change')

def write_result(data, filename):
    with open(filename, 'w+', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=',')
     for row in data:
         spamwriter.writerow(row)     

filename = input('Enter file name to parse: ')

with open(filename, newline='') as csvfile:
     raw_data = list(csv.reader(csvfile, delimiter=','))
     calc_change(raw_data)
     write_result(raw_data, '3days_' + filename)


     
     
