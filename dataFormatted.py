import csv
import os

data = "./data"
formatted = "./formatted.csv"
with open(formatted, "w", newline="") as formatted_file:
    write = csv.writer(formatted_file)
    header = ["sales", "date", "region"]
    write.writerow(header)

    for file_name in os.listdir(data):
        with open(os.path.join(data, file_name), "r") as csv_file:
            reader = csv.reader(csv_file)
            row_count = 0
            for row in reader:
                if row_count > 0:
                    product = row[0]
                    price = row[1]
                    quantity = row[2]
                    date = row[3]
                    region = row[4]

                    if product == "pink morsel":
                        price = float(price[1:])
                        sale = price * int(quantity)
                        output = [sale, date, region]
                        write.writerow(output)
                row_count += 1
