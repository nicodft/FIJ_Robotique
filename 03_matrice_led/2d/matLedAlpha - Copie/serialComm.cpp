#include "serialComm.h"


SerialComm::SerialComm(void) {
}

SerialComm::begin(void) {
  for (int i=0; i< MAX_SIZE) {
    _tmpData[i] = 0;
    _data[i] = 0;
  }
  _newData = False;
  _length = 0;
  Serial.begin(115200);
}

SerialComm::newData(void) {
  if (Serial.available() >= 4) {


 
 if (_length > 0) {
  return (True); 
 } else {
  return (False);
 }
}

SerialComm::length(void) {
  return (length);
}

SerialComm::getData(int dataNb) {
  if ( (dataNb < length) && (dataNb >= 0) ){
    return (_data[dataNb]);
  } else {
    return (-1);
  }
}

