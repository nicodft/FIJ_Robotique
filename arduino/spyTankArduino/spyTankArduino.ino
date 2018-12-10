#include <motor.h>
#include <Wire.h>
#include <I2C_comm.h>


Motor m1(10, 7, 8);
Motor m2(9, 11, 12);
I2C_comm comm;

// Définition des numéros des DIO connectées aux LEDS
#define LED0     2
#define LED1     3
#define LED2     4
#define LED3     5
// Définition des numéros des AIO connectées aux capteurs de ligne
#define LIGNE_G  6
#define LIGNE_D  7
// Définiton des pins du capteur de distance 
#define TRIGGER  15
#define ECHO     16


// Définition des commandes reçues du Rpi
#define CMD_AVANCE  1
#define CMD_RECULE  2
#define CMD_DROITE  3
#define CMD_GAUCHE  4
#define CMD_STOP    5
#define CMD_MOTORS_SPEED  6

#define CMD_LED0   10
#define CMD_LED1   11
#define CMD_LED2   12
#define CMD_LED3   13

#define CMD_LIGNE_D	    20
#define CMD_LIGNE_G	    21
#define CMD_ANALOG_READ 22
#define CMD_DISTANCE    23



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
  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  int cmd;
  int data;

  if (comm.newMessage()==true) {
    cmd = comm.readCmd();
    Serial.print("Cmd received:");
    Serial.println(cmd);
    if(cmd == CMD_LED0) {
      digitalWrite(LED0, comm.readParam1());
    }
    if(cmd == CMD_LED1) {
      digitalWrite(LED1, comm.readParam1());
    }
    if(cmd == CMD_LED2) {
      digitalWrite(LED2, comm.readParam1());
    }
    if(cmd == CMD_LED3) {
      digitalWrite(LED3, comm.readParam1());
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
    if (cmd == CMD_MOTORS_SPEED) {
      m1.actuate(comm.readParam1()/100.0);
      m2.actuate(comm.readParam2()/100.0);
    }

    
  	if (cmd == CMD_LIGNE_D) {
      data = analogRead(LIGNE_D);
  		comm.sendMessage(CMD_LIGNE_D, data);
  	}
  	if (cmd == CMD_LIGNE_G) {
      data = analogRead(LIGNE_G);
  		comm.sendMessage(CMD_LIGNE_G, data);
  	}

    if (cmd == CMD_ANALOG_READ) {
      data = analogRead(comm.readParam1());
      comm.sendMessage(CMD_ANALOG_READ, data);
    }

    if (cmd == CMD_DISTANCE) {
      long duration;
      digitalWrite(TRIGGER, LOW);
      delayMicroseconds(2);
      digitalWrite(TRIGGER, HIGH);
      delayMicroseconds(10);
      digitalWrite(TRIGGER, LOW);
      duration = pulseIn(ECHO, HIGH);
      data = (duration/2) / 29.1;
      comm.sendMessage(CMD_DISTANCE, data);
    }
  }
}




