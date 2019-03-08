#include "Wire.h"

#define LED_DELAI   1
#define NB_LIG      5
#define NB_COL      4



int lig, col;
int lignes[NB_LIG] = {2, 3, 4, 5, 6};
int colonnes[NB_COL] = {8, 9, 10, 11};
int img[NB_LIG][NB_COL];
int data[NB_LIG][NB_COL];
int i, j;

void sendData();
void receiveData(int byteCount);




void setup() {
  Serial.begin(57600);
  Wire.begin(8);                //Set up I2C
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  for (lig=0; lig<NB_LIG; lig++) {
    pinMode(lignes[lig], OUTPUT);
    digitalWrite(lignes[lig], LOW);
    pinMode(colonnes[lig], OUTPUT);
    digitalWrite(colonnes[lig], HIGH);
  }
  for (i=0; i<NB_LIG; i++) {
    for (j=0; j<NB_COL; j++) {
      img[i][j] = 0;
    }
  }
  i = 0;
  j = 0;
  pinMode(LED_BUILTIN, OUTPUT);
}


void loop() {
  affiche(img);
}


void affiche(int image[NB_LIG][NB_COL]) {
  for (col=0; col<NB_COL; col++) {
    for (lig=0; lig<NB_LIG; lig++) {   
      digitalWrite(lignes[lig], image[lig][col]);
      //Serial.print(image[lig][col]);
    }
    //Serial.println("\n");
    digitalWrite(colonnes[col], LOW);
    delay(LED_DELAI);
    digitalWrite(colonnes[col], HIGH);
  }
}


void receiveData(int byteCount) {
  digitalWrite(LED_BUILTIN,HIGH);
    while(Wire.available()) {
      data[i][j] = Wire.read();
      Serial.print(data[i][j]);
      j++;
      if (j >= NB_COL) {
        Serial.println("\n");
        j = 0;
        i++;
        if (i >= NB_LIG) {
          digitalWrite(LED_BUILTIN, HIGH);
          for (i=0; i<NB_LIG; i++) {
            for (j=0; j<NB_COL; j++) {
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


