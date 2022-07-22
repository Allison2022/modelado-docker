import psycopg2

# Connect to an existing database
conn = psycopg2.connect(
    "host=model2.postgres.database.azure.com dbname=accidentalidad-2017-2021 user=model2@model2 password=M0d3l4m13nt0")

conn.autocommit = True
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this create table fecha_accidente
'''cur.execute(
    "CREATE TABLE IF NOT EXISTS volumetria_accidentalidad_dia.fecha_accidente (id serial PRIMARY KEY UNIQUE, fecha date, dia_semana_acc character varying(50), hora_acc integer);")
'''

# Execute a command: this create table condicion_meteor
'''cur.execute(
    "CREATE TABLE IF NOT EXISTS volumetria_accidentalidad_dia.condicion_meteor (id serial PRIMARY KEY UNIQUE, condicion character varying(20));")
'''

# Execute a command: this create table terreno
'''cur.execute(
    "CREATE TABLE IF NOT EXISTS volumetria_accidentalidad_dia.terreno (id serial PRIMARY KEY UNIQUE, terreno character varying(50), estado_superficie character varying(50));")
'''

# Execute a command: this create table accidentalidad_diaria
cur.execute(
    "CREATE TABLE IF NOT EXISTS volumetria_accidentalidad_dia.accidentalidad_diaria (id serial PRIMARY KEY UNIQUE, idCondicionMeteor integer REFERENCES volumetria_accidentalidad_dia.condicion_meteor (id), idTerreno integer REFERENCES volumetria_accidentalidad_dia.terreno (id), idFechaAcc integer REFERENCES volumetria_accidentalidad_dia.fecha_accidente (id));")


print("TABLA CREADA CON EXITO")

conn.commit()

# Close the cursor
cur.close()
# Close communication with the database
conn.close()