#include <Wire.h>
#include <Servo.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define SLAVE_ADDRESS 0x04

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)

#define SERVO_X_PIN 9
#define SERVO_Y_PIN 10
  
Adafruit_BNO055 bno = Adafruit_BNO055(55);
/* 
BNO data structure: 
{
  [0] euler_x,
  [1] euler_y,
  [2] euler_z,
  [3] acc_x,
  [4] acc_y,
  [5] acc_z,
  [6] omega_x,
  [7] omega_y,
  [8] omega_z,
  [9] temperature
}
*/

double bno_data[10] = {0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0};
Servo servo_x;
Servo servo_y;

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

  servo_x.attach(SERVO_X_PIN, 544, 2400); // pin, min, max
  servo_y.attach(SERVO_Y_PIN, 544, 2400);
  
}

void receiveData()
{
  if(Wire.available())
  {
    data = Wire.read();
    Serial.print("Data received: ");
    Serial.println(data);
    switch (data) 
    {
      // Data
      case 0:
        break;
        
      // Status
      case 1:
        break;

      // Servo  
      case 2:
        break;

      // Shutdown
      case 3:
        break;
        
    }
  }
}

void sendData()
{
  if(Wire.available())
  {
    Wire.write(data);
  }
}
 
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
