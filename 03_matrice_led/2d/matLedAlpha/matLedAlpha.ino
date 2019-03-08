#include "alphabet.h"


#define LED_DELAI  1
#define IMG_DELAI  1500



int compteur, lig, col;
int lignes[5] = {2, 3, 4, 5, 6};
int colonnes[5] = {8, 9, 10, 11, 12};



void setup() {
  for (lig=0; lig<5; lig++) {
    pinMode(lignes[lig], OUTPUT);
    digitalWrite(lignes[lig], LOW);
    pinMode(colonnes[lig], OUTPUT);
    digitalWrite(colonnes[lig], HIGH);
  }
}


void loop() {
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(a);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(b);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(c);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(d);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(e);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(f);
  }
}


void affiche(int image[5][5]) {
  for (col=0; col<5; col++) {
    for (lig=0; lig<5; lig++) {   
      digitalWrite(lignes[lig], image[lig][col]);
    }
    digitalWrite(colonnes[col], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[col], HIGH);
  }
}


