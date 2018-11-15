#include <motor.h>

Motor m1(10, 11, 12);
Motor m2(9, 8, 7);
void setup() {
  // put your setup code here, to run once:
  m1.begin();
  m2.begin();
  pinMode(6, OUTPUT);
  digitalWrite(6,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  m1.actuate(0.5);
  m2.actuate(0.5);
  delay(1000);
  m1.actuate(0);
  m2.actuate(0);
  delay(500);
  m1.actuate(-0.5);
  m2.actuate(-0.5);
  delay(1000);
  m1.actuate(0);
  m2.actuate(0);
  delay(500);
}
