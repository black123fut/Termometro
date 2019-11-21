#include "DHT.h"

#define DHTPIN 7

#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}
void loop() {
  float t = dht.readTemperature(); //Lee la temperatura
  Serial.println(t);
}
