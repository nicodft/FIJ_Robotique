/*
 * Cube NxN : besoin de Nx(N+1) GPIO =>
 *  3x3 : 12 GPIO
 *  4x4 : 20 GPIO
 *  5x5 : 30 GPIO
 * 
 * Parallélipipède HxLxl : besoin de H + Lxl GPIO =>
 *  5x3x3 : 14 GPIO
 */

#include "Wire.h"

#define NB_PLANS  5
#define NB_COLS   9


#define LED_DELAI   1
#define IMG_DELAI   500



/* Gère l'affichage d'un cube 5x3x3. 
 *  
 *  Le cube est composé de 5 plans horizontaux et de 9 colonnes verticales
 *  Chaque LED est au croisement d'un plan et d'une colonne.
 *  Les résistances de limitation du courant sont connectées aux colonnes.
 *  Les colonnes sont les anodes (borne +) des LEDs
 *  Les plans sont les cathodes (bornes -) des LEDs
 *  Pour allumer une LED, on doit mettre à HIGH la sortie connectée à sa colonne
 *  et mettre à LOW la sortie connectée à son plan.
 *  
 *  Principe de fonctionnement :
 *   - Par défaut, toutes les colonnes sont à LOW et tous les plans sont à HIGH.
 *   - Pour afficher une image dans un plan, on met les colonnes des LEDs à allumer à HIGH et les autres à LOW,
 *     puis on met le plan à LOW.
 *   - Pour afficher une image 3D complète, on affiche chacun de ses plans pendant 1ms, en boucle.
 *     L'oeil humain n'est pas assez rapide pour voir les LEDs "clignoter" (c'est le mêm principe que le cinéma).
 */


int compteur, pln, col;
int plans[NB_PLANS] = {11, 12, 13, 14, 15};
int colonnes[NB_COLS] = {2, 3, 4, 5, 6, 7, 8, 9, 10};
int img[NB_PLANS][NB_COLS];
int data[NB_PLANS][NB_COLS];
int i, j;

void testCube();
void affiche(int image[NB_PLANS][NB_COLS]);
//void afficheChiffreDansPlanVert(int chiffre[NB_PLANS][TAILLE], int planVert);
void sendData();
void receiveData(int byteCount);




void setup() {
  Wire.begin(8);                //Set up I2C
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  // on initialise les pattes en sortie et on leur donne leur valeur par défaut.
  for (pln=0; pln<NB_PLANS; pln++) {
    pinMode(plans[pln], OUTPUT);
    digitalWrite(plans[pln], HIGH);
  }
  for (col=0; col<NB_COLS; col++) {
    pinMode(colonnes[col], OUTPUT);
    digitalWrite(colonnes[col], LOW);
  }
}


void loop() {
  testCube();

//  for (int planVert=0; planVert<8; planVert++) {
//    for (int t=0; t<IMG_DELAI; t+=LED_DELAI*NB_PLANS) {
//      afficheChiffreDansPlanVert(un, planVert);
//    }
//  }
}



/* test simple des LEDs
 * 
 * La fonction allume successivement chaque LED pendant 1/2 seconde.
 */
void testCube() {
  for (pln=0; pln<NB_PLANS; pln++) {
    digitalWrite(plans[pln], LOW);
    for (col=0; col<9; col++) {
      digitalWrite(colonnes[col], HIGH);
      delay(500);
      digitalWrite(colonnes[col], LOW);
    }
    digitalWrite(plans[pln], HIGH);
  }
}


/* Affiche une image donnée sous la forme d'un tableau de 0/1.
 *  
 */
void affiche(int image[NB_PLANS][NB_COLS]) {
  for (pln=0; pln<NB_PLANS; pln++) {
    for (col=0; col<NB_COLS; col++) {
      digitalWrite(colonnes[col], image[pln][col]);
    }
    digitalWrite(plans[pln], LOW);
    delay(LED_DELAI);
    digitalWrite(plans[pln], HIGH);
  }
}


void receiveData(int byteCount) {
    while(Wire.available()) {
      data[i][j] = Wire.read();
      Serial.print(data[i][j]);
      j++;
      if (j >= NB_COLS) {
        Serial.println("\n");
        j = 0;
        i++;
        if (i >= NB_PLANS) {
          for (i=0; i<NB_PLANS; i++) {
            for (j=0; j<NB_COLS; j++) {
              img[i][j] = data[i][j];
            }
          }
          i = 0;
          j = 0;
        }
      }
    }
 }


// callback for sending data
volatile int ind=0;
void sendData() {
}


/*
void afficheChiffreDansPlanVert(int chiffre[NB_PLANS][TAILLE], int planVert) {
  int image[NB_PLANS][NB_COLS];

  for (pln=0; pln<NB_PLANS; pln++) {
    for (col=0; col<NB_COLS; col++) {
      image[pln][col] = 0;
    }
  }
  if (planVert == 0) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][0] = chiffre[pln][0];
      image[pln][1] = chiffre[pln][1];
      image[pln][2] = chiffre[pln][2];
    }
  } else if (planVert == 1) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][3] = chiffre[pln][0];
      image[pln][4] = chiffre[pln][1];
      image[pln][5] = chiffre[pln][2];
    }
  } else if (planVert == 2) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][6] = chiffre[pln][0];
      image[pln][7] = chiffre[pln][1];
      image[pln][8] = chiffre[pln][2];
    }
  } else if (planVert == 3) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][0] = chiffre[pln][0];
      image[pln][3] = chiffre[pln][1];
      image[pln][6] = chiffre[pln][2];
    }
  } else if (planVert == 4) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][1] = chiffre[pln][0];
      image[pln][4] = chiffre[pln][1];
      image[pln][7] = chiffre[pln][2];
    }
  } else if (planVert == 5) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][2] = chiffre[pln][0];
      image[pln][5] = chiffre[pln][1];
      image[pln][8] = chiffre[pln][2];
    }
  } else if (planVert == 6) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][0] = chiffre[pln][0];
      image[pln][4] = chiffre[pln][1];
      image[pln][8] = chiffre[pln][2];
    }
  } else if (planVert == 7) {
    for (pln=0; pln<NB_PLANS; pln++) {
      image[pln][6] = chiffre[pln][0];
      image[pln][4] = chiffre[pln][1];
      image[pln][2] = chiffre[pln][2];
    }
  }
}

*/
