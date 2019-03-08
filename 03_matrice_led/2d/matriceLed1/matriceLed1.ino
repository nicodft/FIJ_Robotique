
#define LED_DELAI  1

void led(int ligneNb, int colonneNb);



int compteur, l, c;
int lignes[5] = {2, 3, 4, 5, 6};
int colonnes[5] = {8, 9, 10, 11, 12};


void setup() {
  for (l=0; l<5; l++) {
    pinMode(lignes[l], OUTPUT);
    digitalWrite(lignes[l], LOW);
    pinMode(colonnes[l], OUTPUT);
    digitalWrite(colonnes[l], HIGH);
  }
}


void loop() {
/*
  for (l=0; l<5; l++) {
    for(c=0; c<5; c++) {
      for (compteur=0; compteur<300; compteur+=LED_DELAI) {
        led(l, c);
      }
    }
  }
*/

  for (compteur=0; compteur < 300; compteur+=LED_DELAI) {
    carre(1);
  }
  for (compteur=0; compteur < 300; compteur+=3*LED_DELAI) {
    carre(3);
  }
  for (compteur=0; compteur < 300; compteur+=5*LED_DELAI) {
    carre(5);
  }
  for (compteur=0; compteur < 300; compteur+=3*LED_DELAI) {
    carre(3);
  }
}


void carre(int taille) {
  if (taille == 1) {
    led(2, 2);
  } else if (taille == 3) {
    digitalWrite(lignes[1], HIGH);
    digitalWrite(lignes[2], HIGH);
    digitalWrite(lignes[3], HIGH);
    digitalWrite(colonnes[1], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[1], HIGH);    
    digitalWrite(colonnes[3], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[3], HIGH);    
    digitalWrite(lignes[2], LOW);    
    digitalWrite(colonnes[2], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[2], HIGH);
    digitalWrite(lignes[1], LOW);
    digitalWrite(lignes[3], LOW);
  } else if (taille == 5) {
    digitalWrite(lignes[0], HIGH);
    digitalWrite(lignes[1], HIGH);
    digitalWrite(lignes[2], HIGH);
    digitalWrite(lignes[3], HIGH);
    digitalWrite(lignes[4], HIGH);
    digitalWrite(colonnes[0], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[0], HIGH);
    digitalWrite(colonnes[4], LOW);    
    delay(LED_DELAI);
    digitalWrite(colonnes[4], HIGH);
    digitalWrite(lignes[1], LOW);
    digitalWrite(lignes[2], LOW);
    digitalWrite(lignes[3], LOW);
    digitalWrite(colonnes[1], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[1], HIGH);
    digitalWrite(colonnes[2], LOW);    
    delay(LED_DELAI);
    digitalWrite(colonnes[2], HIGH);
    digitalWrite(colonnes[3], LOW);    
    delay(LED_DELAI);
    digitalWrite(colonnes[3], HIGH);
    digitalWrite(lignes[0], LOW);
    digitalWrite(lignes[4], LOW);
  }
}


void led(int ligneNb, int colonneNb) {
  digitalWrite(lignes[ligneNb], HIGH);
  digitalWrite(colonnes[colonneNb], LOW);
  delay(LED_DELAI);
  digitalWrite(lignes[ligneNb], LOW);
  digitalWrite(colonnes[colonneNb], HIGH);
}

