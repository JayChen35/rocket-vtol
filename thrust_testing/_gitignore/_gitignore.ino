#include <Servo.h>

Servo motor;

void setup ()
{
  motor.attach(6);
  Serial.begin(9600);
  int i = 0;

  //Give some time before you start anything like switching on your ESC / Motor
  delay(1000);
  motor.write(52);
  Serial.println("a");
  delay(500);
  motor.write(53);
  Serial.println("a");
  delay(500);
  motor.write(54);
  Serial.println("a");
  delay(500);
  motor.write(55);
  Serial.println("a");
  delay(500);
  motor.write(56);
  Serial.println("a");
  delay(500);
  motor.write(57);
  Serial.println("a");
  delay(500);
  motor.write(58);
  Serial.println("a");
  delay(500);
  motor.write(59);
  Serial.println("a");
  delay(500);
  //13 oz dry weight
}

void loop()
{
  motor.write(150);
}
