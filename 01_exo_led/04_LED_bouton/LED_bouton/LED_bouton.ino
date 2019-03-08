/*
  Exemple illustrant l'utilisation d'une patte DIO en entrée
  IL allume une LED lorsqu'on appuie sur un bouton.
  La LED est connectée à D2
  Le bouton est connecté à D7 :
   - si on n'appuie pas sur le bouton, D7 est à 0
   - si on appuie sur le bouton, D7 est à 1
*/

#define LED     2
#define BOUTON  7


void setup() {
  // Initialisation de D2 en sortie et de D7 en entrée
  pinMode(LED, OUTPUT);
  pinMode(BOUTON, INPUT);
}


void loop() {
  digitalWrite(LED, digitalRead(BOUTON));
}
