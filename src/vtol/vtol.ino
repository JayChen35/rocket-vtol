#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;

int trigPin1 = 11;    // Trigger
int echoPin1 = 12;    // Echo
int trigPin2 = 10;    // Trigger
int echoPin2 = 9;    // Echo

float ultrasonic1 = 0.0;
float ultrasonic2 = 0.0;
int callnum = 0;

void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  pinMode(13, OUTPUT);
  // initialize i2c as slave
  Wire.begin(SLAVE_ADDRESS);
  
  // define callbacks for i2c communication
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  
  Serial.println("Ready!");
}
 
void loop() {

  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin1, INPUT);
  float duration1 = pulseIn(echoPin1, HIGH);

  float inches1 = (duration1/2) / 74;   // Divide by 74 or multiply by 0.0135

  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin2, INPUT);
  float duration2 = pulseIn(echoPin2, HIGH);

  float inches2 = (duration2/2) / 74;   // Divide by 74 or multiply by 0.0135

  // Convert the time into a distance
//  return cm;
//  float cm = getCm();
//  float inches = getInches();
  ultrasonic1 = inches1;
  ultrasonic2 = inches2;
  Serial.print("Ultrasonic 1: ");
  Serial.println(ultrasonic1);
  Serial.print("Ultrasonic 2: ");
  Serial.println(ultrasonic2);  
//  sendData();
  delay(250);
}

// callback for sending data
void sendData(){
  /*
  if(callnum % 5 == 0){
    Wire.write(0);
  }
  else if(callnum % 5 == 1){
    Wire.write((int)ultrasonic1);
    float a = ultrasonic1 * 100;
    a -= (float)((int)(ultrasonic1 * 100));
    Wire.write((int)a);
    callnum += 1;
  }
  else if(callnum % 5 == 3){
    Wire.write((int)ultrasonic2);
    float b = ultrasonic2 * 100;
    b -= (float)((int)(ultrasonic2 * 100));
    Wire.write((int)b);
    callnum += 1;
  }
  */
  float a = ultrasonic1 * 100;
  a -= (float)(((int)ultrasonic1) * 100);
  float b = ultrasonic2 * 100;
  b -= (float)(((int)ultrasonic2) * 100);
  byte output[] = {(byte)((int)ultrasonic1),(int)a,(byte)((int)ultrasonic2),(int)b};
  Wire.write(output, 4);
//  Serial.print(a);
//  Serial.print("in, ");
//  Serial.println();  
//  Serial.print(b);
//  Serial.print("in, ");
//  Serial.println();
//  Wire.write((int)val1);
//  Wire.write((int)val2);
  callnum += 1;
}

// callback for received data
void receiveData(int byteCount){

  Serial.println("HI");
  while(Wire.available()) {
    Serial.println(Wire.read());
  }
}


