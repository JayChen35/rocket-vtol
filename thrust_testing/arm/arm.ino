#include <Servo.h>

Servo motor;

void setup ()
{
  motor.attach(3);
  Serial.begin(9600);

  //Give some time before you start anything like switching on your ESC / Moto
  delay(3000);
  for(int i = 40; i < 50; i++){
    motor.write(i);
    Serial.println(i);
    delay(500);
  }
}

void loop()
{
  motor.write(0);
}
