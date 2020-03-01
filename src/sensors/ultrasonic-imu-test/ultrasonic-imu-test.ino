int echoPin = 10;    // Echo
int trigPin = 11;    // Trigger

float inchesX = 0;
float inchesY = 0;

void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  // Define method to call when something is recieved
}
 
void loop() {

  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  float durationX = pulseIn(echoPin, HIGH);
  inchesX = (durationX/2) / 74;   // Divide by 74 or multiply by 0.0135

  Serial.println(inchesX);
  delay(250);
}
