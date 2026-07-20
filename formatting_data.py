import csv
import os

directory_path = "./data"
output_file_name = "merged_data.csv"

with open(output_file_name,"w") as output_file:
    writer = csv.writer(output_file)

    header = ["Sales","Region","Date"]
    writer.writerow(header)

    for file_name in os.listdir(directory_path):
        with open(f"{directory_path}/{file_name}",'r') as files:
            reader = csv.reader(files)
            row_index = 0
            for row in reader:
                if row_index>0:
                    # finding product,price,quantity,date,region
                    product = row[0]
                    price = row[1]
                    quantity = row[2]
                    date = row[3]
                    region = row[4]

                    if product == "pink morsel":
                        sales = float(price[1:])*int(quantity)
                        
                        output_row = [sales,region,date]
                        writer.writerow(output_row)
                row_index += 1
        
                