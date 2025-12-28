import csv

with open("/home/yashwanth/projects/daily-progress/notes/python/18.1.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("/home/yashwanth/projects/daily-progress/notes/python/18.2.csv", 'w') as csv_write:
        csv_writer = csv.writer(csv_write, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)