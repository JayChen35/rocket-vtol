#include <SoftwareSerial.h>

SoftwareSerial xbee(10, 11);
void setup() {
  // put your setup code here, to run once:
  xbee.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  xbee.write("a");
  delay(500);
}
