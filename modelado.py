# library for python/postgres communication
import psycopg2

# Connect to an existing database
conn = psycopg2.connect(
    "host=model2.postgres.database.azure.com dbname=accidentalidad-2017-2021 user=model2@model2 password=M0d3l4m13nt0")

conn.autocommit = True
# Open a cursor to perform database operations
cur = conn.cursor()

# ------------------------------ table creation block -----------------------------------------------------

# Execute a command: this create table calendar
'''cur.execute("create table volumetria_accidentalidad_dia.calendar(id_calendar SERIAL primary key unique,date_actual date,day_name varchar (20),day_of_week int,month_name varchar(20),year int);")'''

# Execute a command: this create table territorio
'''cur.execute("create table volumetria_accidentalidad_dia.territorio(id_territorio SERIAL primary key unique, territorial varchar(50));")'''

# Execute a command: this create table condicion_meteorologica
'''cur.execute("create table volumetria_accidentalidad_dia.condicion_meteorologica(id_cond_meteor SERIAL primary key unique,condic_meteor varchar(20));")'''


# Execute a command: this create table estado_carretera
'''cur.execute("create table volumetria_accidentalidad_dia.estado_carretera(id_estado_carretera SERIAL primary key unique,id_cond_meteor int REFERENCES volumetria_accidentalidad_dia.condicion_meteorologica(id_cond_meteor),estado_super varchar(50),terreno varchar(50));")'''

# Execute a command: this create table ubicacion
'''cur.execute("create table volumetria_accidentalidad_dia.ubicacion(id_ubicacion SERIAL primary key unique,id_terrotirio int REFERENCES volumetria_accidentalidad_dia.territirio(id_territirio),ruta_id varchar(20));")'''

# Execute a command: this create table detalle_accidente
'''cur.execute("create table volumetria_accidentalidad_dia.detalle_accidente(id_detalle_accidente SERIAL primary key unique,id_estado_carretera int REFERENCES volumetria_accidentalidad_dia.estado_carretera(id_estado_carretera),id_ubicacion int REFERENCES volumetria_accidentalidad_dia.ubicacion(id_ubicacion),fecha_acc int REFERENCES volumetria_accidentalidad_dia.calendar(id_calendar),dia_semana_acc varchar(20),hora_acc int);")'''


# ------------------------------ inserted block -----------------------------------------------------

 
'''# filling table calendar
cur.execute("insert into volumetria_accidentalidad_dia.calendar(id_calendar, date_actual, day_name, day_of_week, month_name, year) select id_calendar, date_actual, day_name, day_of_week, month_name, extract(year from date_actual) FROM dwh.calendar")

# filling table territorio
cur.execute("insert into volumetria_accidentalidad_dia.territorio(id_territorio, territorial) select id_territorio, territorial FROM dwh.territorio")

# filling table condicion_meteorologica
cur.execute("insert into volumetria_accidentalidad_dia.condicion_meteorologica(id_cond_meteor,condic_meteor) select id_cond_meteor,condic_meteor FROM dwh.condicion_metereologica")

# filling table estado_carretera
cur.execute("insert into volumetria_accidentalidad_dia.estado_carretera(id_estado_carretera,id_cond_meteor,estado_super,terreno) select id_estado_carretera,id_cond_meteor,estado_super,terreno FROM dwh.estado_carretera")

# filling table ubicacion
cur.execute("insert into volumetria_accidentalidad_dia.ubicacion(id_ubicacion,id_territorio,ruta_id) select id_lugar_accidente,id_territorio,ruta_id FROM dwh.lugar_accidente")

# filling table detalle_accidente
cur.execute("insert into volumetria_accidentalidad_dia.detalle_accidente(id_detalle_accidente,id_estado_carretera,id_ubicacion,dia_semana_acc,hora_acc) select id_accidentes,id_estado_carretera,id_lugar_accidente,dia_semana_acc,hora_acc FROM dwh.accidentes")
'''
# ---------------------------- Update ---------------------------------------------------------------------
'''
# Update table detalle_accidente
cur.execute(
    """update volumetria_accidentalidad_dia.detalle_accidente as ta set fecha_acc = c.id_calendar from (select id_calendar, TB.id_accidentes from volumetria_accidentalidad_dia.calendar as TA join dwh.accidentes as TB on TA.date_actual = TB.fecha_acc) as c where c.id_accidentes = ta.id_detalle_accidente;""")
'''

# test message
print("DATOS INSERTADOS CON EXITO")

# Close the cursor
cur.close()
# Close communication with the database
conn.close()