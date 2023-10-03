import csv

def from_dataset(field, dataset, file_name) :
    with open(file_name, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        #field = ["text"]
        writer.writerow(field)

        for row in range(len(dataset)):
            # write a row to the csv file
            writer.writerow([dataset[row][field]])