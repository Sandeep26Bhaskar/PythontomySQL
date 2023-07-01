import csv
import mysql.connector as connection
conn = connection.connect(host='localhost',user='root',passwd='********')
print(conn.is_connected())
curr = conn.cursor()

input_file = "carbon_nanotubes.csv"
output_file = "preprocessed_final.csv"
with open(input_file,"r") as file:
    reader = csv.reader(file,delimiter="\n")
    new_file = [i[0].replace(",",".").replace(";",",") for i in reader]
# print(new_file[0])
# print(tuple(new_file[0].split(",")))

with open(output_file,"w") as f:
    for line in new_file:
        f.write(line)
        f.write("\n")
# print((new_file[0]))
# line1 = tuple(new_file[0].replace(" ","_").split(","))
# print(line1)

query = "CREATE TABLE IF NOT EXISTS Sandeep.nanotube (" \
        "Chiral_indice_n FLOAT, " \
        "Chiral_indice_m FLOAT, " \
        "Initial_atomic_coordinate_u FLOAT, " \
        "Initial_atomic_coordinate_v FLOAT, " \
        "Initial_atomic_coordinate_w FLOAT, " \
        "Calculated_atomic_coordinates_u FLOAT, " \
        "Calculated_atomic_coordinates_v FLOAT, " \
        "Calculated_atomic_coordinates_w FLOAT)"

curr.execute(query)


with open("preprocessed_final.csv","r+") as f:
    next(f)
    data = csv.reader(f,delimiter="\n")
    for line in data:
        curr.execute(f"INSERT INTO Sandeep.nanotube VALUES({tuple(line)[0]})")
        # print(tuple(line)[0])
conn.commit()
curr.close()
conn.close()
