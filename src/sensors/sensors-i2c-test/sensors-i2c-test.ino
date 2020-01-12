#include <Wire.h>
#define SLAVE_ADDRESS 0x40

int trigPinX = 11;    // Trigger
int echoPinX = 12;    // Echo
int trigPinY = 10;    // Trigger
int echoPinY = 9;    // Echo
String cmd;
String reply;
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPinX, OUTPUT);
  pinMode(echoPinX, INPUT);
  pinMode(trigPinY, OUTPUT);
  pinMode(echoPinY, INPUT);
  // Begin i2c
  Wire.begin(SLAVE_ADDRESS);
  // Define method to call when something is recieved
  Wire.onReceive(receiveData);
  // Wire.onRequest(requestData);
}
 
void loop() {
  // nothing
}

void receiveData(int byteCount) {
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPinX, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinX, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinX, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPinX, INPUT);
  float durationX = pulseIn(echoPinX, HIGH);
  float cmX = (durationX/2) / 74;
  float inchesX = (durationX/2) / 74;   // Divide by 74 or multiply by 0.0135

  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPinY, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPinY, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPinY, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPinY, INPUT);
  float durationY = pulseIn(echoPinY, HIGH);
  float cmY = (durationY/2) / 74;
  float inchesY = (durationY/2) / 74;   // Divide by 74 or multiply by 0.0135

  while (Wire.available()) {
    cmd = (char)Wire.read();
  }
  if (cmd == "send_ultrasonic_data") {
    union cvt {
      float val;
      unsigned char byte_array[4];
    } x;
    x.val = cmX;
    Wire.write(x.byte_array, 4);
  }
  else {
    Wire.send("Command failed.");
  }
}
