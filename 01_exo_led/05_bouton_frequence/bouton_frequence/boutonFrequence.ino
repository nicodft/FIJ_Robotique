/*
 * Exemple illustrant l'utilisation d'une variable.
 * 
 * Ce programme est une amélioration de Blink :
 *  - Une LED et un bouton sont connectés à l'Arduino 
 *  - La LED clignote avec un délai initial de 1 seconde
 *  - Ce délai est stocké dans une variable 
 *  - Lorsqu'on appuie sur le bouton, on divise le délai par 2.
 */


#define LED     2
#define BOUTON  7


// Déclaration de la variable
int delai;


void setup() {
  // Configuration des pattres de la LED et du bouton
  pinMode(LED, OUTPUT);
  pinMode(BOUTON, INPUT);
  // Initialisation de la variable
  delai = 1000;
}


void loop() {
  // Clignotement de la LED
  digitalWrite(LED, HIGH);
  delay(delai);
  digitalWrite(LED, LOW);
  delay(delai);

  /* Lecture du bouton :
   *  Si le bouton est enfoncé :
   *   - on divise le délai par 2
   *   - on attend que le bouton soit relaché (pour éviter de réagir plusieurs fois pour un seul appui sur le bouton)
   *   - on ajoute un délai pour éviter les rebonds
   */
  if (digitalRead(BOUTON)) {
    delai = delai/2;
    while(digitalRead(BOUTON));
    delay(100);
  }
}
