int trigPin1 = 11;    // Trigger
int echoPin1 = 12;    // Echo
int trigPin2 = 10;    // Trigger
int echoPin2 = 9;    // Echo
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
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
  Serial.println(duration1);

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
  sendData(inches1, inches2);
  delay(250);
}

float sendData(float val1, float val2){
  Serial.print(val1);
  Serial.print("in, ");
  Serial.println();  
  Serial.print(val2);
  Serial.print("in, ");
  Serial.println();  
}
