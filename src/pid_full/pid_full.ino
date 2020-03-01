#include <Wire.h>
#include <Servo.h>

#define SLAVE_ADDRESS 0x04
Servo motor;

// Sensor definitions
int echoPinX = 10;
int trigPinX = 11;
int echoPinY = 12;
int trigPinY = 13;
float inchesX = 0;
float inchesY = 0;

byte send_data[4];




void setup() {
  // put your setup code here, to run once:
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  motor.attach(9);
  pinMode(trigPinX, OUTPUT);
  pinMode(echoPinX, INPUT);
  pinMode(trigPinY, OUTPUT);
  pinMode(echoPinY, INPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  inchesX = readUltrasonic(trigPinX, echoPinX);
  inchesY = readUltrasonic(trigPinY, echoPinY);
  delay(100);
}

float readUltrasonic(int trigPin, int echoPin){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  pinMode(echoPin, INPUT);
  float duration = pulseIn(echoPin, HIGH);
  float inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135
  return inches;
}

void ingest(int data){
  motor.write(data);
//  Serial.println(data);
}

void receiveData(int byteCount){
  while(Wire.available()){
    int data = Wire.read();
    ingest(data);
  }
}

void float_to_bytes(float v){
  Serial.print("Value: ");
  Serial.println(v);
}

void edit_send_array(byte to_add[], int s, int e){
  Serial.print("Length: ");
  Serial.println(sizeof(to_add) / sizeof(to_add[0]));
  for(int i = s; i < e; i++){
    send_data[i] = to_add[i-s];
  }
}

void sendData(){
    Serial.print("Data:");
    Serial.println(inchesX);

    union cvt {
      float val;
      unsigned char byte_array[4];
    } x;
    x.val = inchesX;
    union cvt2 {
      float val;
      unsigned char byte_array[4];
    } y;
    y.val = inchesY;
    
    byte data[8];
    for(int i = 0; i < 4; i++){ data[i] = x.byte_array[i];}
    for(int i = 4; i < 8; i++){ data[i] = y.byte_array[i-4];}

//    unsigned char ultra1 = float_to_bytes(inchesX);
//    unsigned char ultra2 = float_to_bytes(inchesY);
//    edit_send_array(ultra1, 0, 4);
//    edit_send_array(ultra2, 4, 8);
    Wire.write(data, 8);
}

