/*
 * Exemple illustrant l'utilisation d'une variable.
 * 
 * Ce programme est une amélioration de LED_bouton :
 *  - Une LED et un bouton sont connectés à l'Arduino 
 *  - La LED Change d'état chaque fois que le bouton est enfoncé
 *  Une variable est nécessaire pour retenir l'état actuel de la LED.
 */


#define LED     2
#define BOUTON  7


// Déclaration de la variable
int etatLed;


void setup() {
  // Configuration des pattres de la LED et du bouton
  pinMode(LED, OUTPUT);
  pinMode(BOUTON, INPUT);
  // Initialisation de la variable
  etatLed = LOW;
}


void loop() {

  /* Lecture du bouton :
   *  Si le bouton est enfoncé :
   *   - on cahnge l'état de la variable et de la LED
   *   - on attend que le bouton soit relaché (pour éviter de réagir plusieurs fois pour un seul appui sur le bouton)
   *   - on ajoute un délai pour éviter les rebonds
   */
  if (digitalRead(BOUTON)) {
    if (etatLed == LOW) {
      etatLed = HIGH;
    } else {
      etatLed = LOW;
    }
    digitalWrite(LED, etatLed);
    while(digitalRead(BOUTON));
    delay(100);
  }
}
