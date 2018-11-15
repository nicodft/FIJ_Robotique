#include <Wire.h>
#include <motor.h>
#include <I2C_comm.h>

Motor m1(10, 7, 8);
Motor m2(9, 11, 12);
I2C_comm comm;

#define GPIO_NB  8
int gpio[GPIO_NB] = {2, 3, 4, 5, 13, 14, 15, 16};

#define LIGNE_G  6
#define LIGNE_D  7

int i, j;


void setup() {
  
  Serial.begin(9600);
  // Initialisation des moteurs
  m1.begin();
  m2.begin();
  // Active la patte STBY du TB6612
  pinMode(6, OUTPUT);
  digitalWrite(6,HIGH);
  
  // Initialisation de la communication
  comm.begin();
  
  // Initialisation des utres GPIO
  for (i=0; i<GPIO_NB; i++) {
    pinMode(gpio[i], OUTPUT);
  }
  
  for (j = 0; j<3; j++) {
    for (i=0; i<GPIO_NB; i++) {
      digitalWrite(gpio[i], HIGH);
    }
    delay(500);
    for (i=0; i<GPIO_NB; i++) {
      digitalWrite(gpio[i], LOW);
    }
    delay(500);
  }
}


void loop() {
  float vit;
  
  Serial.print("Ligne gauche : ");
  Serial.print(analogRead(LIGNE_G));
  Serial.print(" Ligne droite : ");
  Serial.println(analogRead(LIGNE_D));
  for (vit=-1; vit<=1; vit+=0.25) {
    m1.actuate(vit);
    m2.actuate(vit);
    delay(100);
  }
  Serial.print("Ligne gauche : ");
  Serial.print(analogRead(LIGNE_G));
  Serial.print(" Ligne droite : ");
  Serial.println(analogRead(LIGNE_D));
  for (vit=1; vit>=-1; vit-=0.25) {
    m1.actuate(vit);
    m2.actuate(vit);
    delay(100);
  }
}
