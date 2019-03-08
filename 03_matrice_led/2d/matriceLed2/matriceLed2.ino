
#define LED_DELAI  1
#define IMG_DELAI  200

void led(int ligneNb, int colonneNb);



int compteur, l, c;
int lignes[5] = {2, 3, 4, 5, 6};
int colonnes[5] = {8, 9, 10, 11, 12};

int carre1[5][5] = {{0, 0, 0, 0, 0},
                    {0, 0, 0, 0, 0},
                    {0, 0, 1, 0, 0},
                    {0, 0, 0, 0, 0},
                    {0, 0, 0, 0, 0}};
int carre3[5][5] = {{0, 0, 0, 0, 0},
                    {0, 1, 1, 1, 0},
                    {0, 1, 0, 1, 0},
                    {0, 1, 1, 1, 0},
                    {0, 0, 0, 0, 0}};
int carre5[5][5] = {{1, 1, 1, 1, 1},
                    {1, 0, 0, 0, 1},
                    {1, 0, 0, 0, 1},
                    {1, 0, 0, 0, 1},
                    {1, 1, 1, 1, 1}};

void setup() {
  for (l=0; l<5; l++) {
    pinMode(lignes[l], OUTPUT);
    digitalWrite(lignes[l], LOW);
    pinMode(colonnes[l], OUTPUT);
    digitalWrite(colonnes[l], HIGH);
  }
}


void loop() {
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(carre1);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(carre3);
  }
  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
    affiche(carre5);
  }
//  for (compteur=0; compteur < IMG_DELAI; compteur+=5*LED_DELAI) {
//    affiche(carre3);
//  }
}


void affiche(int image[5][5]) {
  for (c=0; c<5; c++) {
    for (l=0; l<5; l++) {   
      digitalWrite(lignes[l], image[l][c]);
    }
    digitalWrite(colonnes[c], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[c], HIGH);
  }
}


