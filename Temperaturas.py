from CassandraConexion import getCluster
from ArduinoConexion import getMedicion

cursor = getCluster()

while True:
    medicion = getMedicion()
    print(medicion)
    if medicion == "nan":
        continue
    query = "INSERT INTO Temperatura(IdTemperatura, Medicion, Hora) VALUES (UUID(), %s, toUnixTimestamp(now()))"
    cursor.execute(query, ( str(medicion), ))