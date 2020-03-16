#include <Servo.h>
#include <SoftwareSerial.h>

Servo motor;
SoftwareSerial xbee(10, 11);
boolean armed;
int sped;

void setup ()
{
  xbee.begin(9600);
  motor.attach(3);
  Serial.begin(9600);

  //Give some time before you start anything like switching on your ESC / Moto
  armed = false;
}

void arm(){
  if(armed){
    return;
  }
  delay(3000);
  for(int i = 40; i < 50; i++){
    motor.write(i);
    Serial.println(i);
    delay(300);
  }
  motor.write(0);
  armed = true;
}

void setSped(int s){
  int val = map(s, 0, 10, 0, 100);
  Serial.print("Speed: ");
  Serial.println(s);
  Serial.print("Val: ");
  Serial.println(val);
  sped = s;
  motor.write(val);
}

void ingest(String str){
  if(str == ""){
    return;
  }
  Serial.print("Received: ");
  Serial.println(str);
  if(str == "a"){
    Serial.println("Arming");
    arm();
  }
  if(str.charAt(0) == 't'){
    int s = str.charAt(1) - '0';
    setSped(s);
  }
}

void loop()
{
  String ret = "";
  while(xbee.available()){
    ret += (char)(xbee.read());
  }
  ingest(ret);
  delay(100);
//  motor.write(0);
}
