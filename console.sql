CREATE TABLE Temperatura (
    IdTemperatura UUID,
    Medicion TEXT,
    Hora TIMESTAMP,
    PRIMARY KEY(IdTemperatura)
);


SELECT * FROM Temperatura LIMIT 1;

SELECT IdTemperatura, Medicion FROM temperatura
WHERE Hora >= '2019-11-21 15:00:00' AND Hora <= '2019-11-21 16:00:00' ALLOW FILTERING;