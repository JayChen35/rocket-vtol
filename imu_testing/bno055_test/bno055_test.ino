#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define SLAVE_ADDRESS 0x04

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)
  
Adafruit_BNO055 bno = Adafruit_BNO055(55);
 
void setup(void) 
{
  // pinMode(12, OUTPUT);
  Serial.begin(9600);
  Serial.println("Orientation Sensor Test.");
  
  /* Initialize the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  
  delay(1000);
  bno.setExtCrystalUse(true);

  /* Initialize i2c */
  Wire.begin(SLAVE_ADDRESS);

  /* Define callbacks for i2c communication */
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);

  Serial.println("I2C is ready.");
  
}

void receiveData()
{
  if(Wire.available())
  {
    data = Wire.read();
    Serial.print("Data received: ");
    Serial.println(data);
  }
}

/* MORE TO DO HERE */
 
void loop(void) 
{
  /* Get a new sensor event */ 
  sensors_event_t event; 
  bno.getEvent(&event);
  
  /* Display the floating point data */
  Serial.print("X: ");
  Serial.print(event.orientation.x, 4);
  Serial.print("\tY: ");
  Serial.print(event.orientation.y, 4);
  Serial.print("\tZ: ");
  Serial.print(event.orientation.z, 4);
  Serial.println("");
  
  delay(BNO055_SAMPLERATE_DELAY_MS);
}
