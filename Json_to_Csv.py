import json
import csv

with open('sample_json_2.json', 'r') as json_file:
    json_data = json.load(json_file)

book_data = json_data['glossary']
csv_writer = open('created_csv.csv', 'w')
csv_data = csv.writer(csv_writer)
count = 0
for book in book_data:
    print(book)
    # if count == 0:
    #     csv_data.writerow(book.keys())
    #     csv_data.writerow(book.values())
    #     count += 1
    # else:
    #     csv_data.writerow(book.values())

csv_writer.close()

# with open("sample_json.json", "r") as json_file:
#     json_data = json.load(json_file)
#
# book_data = json_data['Book_Details']
# csv_writer = open("created_csv.csv", "w")
# csv_data = csv.writer(csv_writer)
#
# count = 0
# for book in book_data:
#     if count == 0:
#         csv_data.writerow(book.keys())
#         count += 1
#     else:
#         csv_data.writerow(book.values())
#
# csv_writer.close()
