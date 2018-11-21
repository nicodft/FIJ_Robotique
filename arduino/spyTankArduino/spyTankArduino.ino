#include <motor.h>
#include <Wire.h>
#include <I2C_comm.h>


Motor m1(10, 7, 8);
Motor m2(9, 11, 12);
I2C_comm comm;

#define LED1     2
#define LED2     3
#define LED3     4
#define LED4     5
#define LIGNE_G  6
#define LIGNE_D  7


#define CMD_AVANCE  1
#define CMD_RECULE  2
#define CMD_DROITE  3
#define CMD_GAUCHE  4
#define CMD_STOP    5

#define CMD_LED1   10
#define CMD_LED2   11
#define CMD_LED3   12
#define CMD_LED4   13

#define CMD_LIGNE_D	20
#define CMD_LIGNE_G	21



void setup() {
  Serial.begin(9600);
  // Initialisation des moteurs
  m1.begin();
  m2.begin();
  // Active la patte STBY du TB6612
  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);
  
  // Initialisation de la communication
  comm.begin();
  // 
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
}

void loop() {
  int cmd;
  int data;

  if (comm.newMessage()==true) {
    cmd = comm.readCmd();
    Serial.print("Cmd received:");
    Serial.println(cmd);
    if(cmd == CMD_LED1) {
      digitalWrite(LED1, comm.readParam1());
    }
    if(cmd == CMD_LED2) {
      digitalWrite(LED2, comm.readParam1());
    }
    if(cmd == CMD_LED3) {
      digitalWrite(LED3, comm.readParam1());
    }
    if(cmd == CMD_LED1) {
      digitalWrite(LED4, comm.readParam1());
    }
	
    if(cmd == CMD_AVANCE) {
      m1.actuate(comm.readParam1()/100.0);
      m2.actuate(comm.readParam1()/100.0);
    }
    if(cmd == CMD_RECULE) {
      m1.actuate(-comm.readParam1()/100.0);
      m2.actuate(-comm.readParam1()/100.0);
    }
    if(cmd == CMD_GAUCHE) {
      m1.actuate(comm.readParam1()/100.0);
      m2.actuate(-comm.readParam1()/100.0);
    }
    if(cmd == CMD_DROITE) {
      m1.actuate(-comm.readParam1()/100.0);
      m2.actuate(comm.readParam1()/100.0);
    }
    if(cmd == CMD_STOP) {
      m1.actuate(0);
      m2.actuate(0);
    }
  	if (cmd == CMD_LIGNE_D) {
      data = analogRead(LIGNE_D);
      Serial.print("Ligne droite - data = ");
      Serial.println(data);
  		comm.sendMessage(CMD_LIGNE_D, data);
  	}
  	if (cmd == CMD_LIGNE_G) {
      data = analogRead(LIGNE_G);
      Serial.print("Ligne gauche - data = ");
      Serial.println(data);
  		comm.sendMessage(CMD_LIGNE_G, data);
  	}
  }
}




