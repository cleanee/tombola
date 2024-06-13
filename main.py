import csv
import random
from struct import Struct

souches = []

# Open the CSV file in read mode
with open('souches.csv', 'r', newline='') as csvfile:
    # Create a reader object
    reader = csv.DictReader(csvfile)

    souche_txt = "{couleur} {numero}"
    # Iterate through the rows in the CSV file
    for row in reader:
        for i in range(int(row['debut']), int(row['fin']) + 1):
            souches.append(souche_txt.format(couleur=row['couleur'], numero=i))

print(souches)
random.shuffle(souches)

print(souches)

distribution = []

# Open the CSV file in read mode
with open('lots.csv', 'r') as csvfile:
    # Create a reader object
    reader = csv.DictReader(csvfile)

    # Iterate through the rows in the CSV file
    for row in reader:
        current_lot = row['libelle']
        if souches:
            distribution.append({'lot': current_lot, 'souche': souches.pop()})
        else:
            distribution.append({'lot': current_lot, 'souche': 'plus de souches'})

print(distribution)

with open('distribution.csv', mode='w') as employee_file:
    fieldnames = ['lot', 'souche']
    distribution_writer = csv.DictWriter(employee_file, quoting=csv.QUOTE_MINIMAL,
                                         fieldnames=fieldnames)
    distribution_writer.writeheader()
    for row in distribution:
        distribution_writer.writerow(row)
