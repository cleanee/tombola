import csv
import random

souches = []
# Open the CSV file in read mode
with open('souches.csv', 'r', newline='') as csvfile:
    # Create a reader object
    reader = csv.DictReader(csvfile)

    souche_txt = "{couleur} {numero}"
    # Iterate through the rows in the CSV file
    for row in reader:
        debut = int(row['debut'])
        fin = int(row['fin']) + 1
        if debut > 0:
            for i in range(debut, fin):
                souches.append(souche_txt.format(couleur=row['couleur'], numero=i))

vendu = len(souches)
random.shuffle(souches)

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

with open('distribution.csv', mode='w') as employee_file:
    fieldnames = ['lot', 'souche']
    distribution_writer = csv.DictWriter(employee_file, quoting=csv.QUOTE_MINIMAL,
                                         fieldnames=fieldnames)
    distribution_writer.writeheader()
    for row in distribution:
        distribution_writer.writerow(row)

print("nombre de lots distribuées {lots}.".format(lots=len(distribution)))
print("nombre de billets vendus {vendu}.".format(vendu=vendu))
