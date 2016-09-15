#include <DigiCDC.h>
void setup() {                
  // initialize the digital pin as an output.
  SerialUSB.begin(); 
  pinMode(5,OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  
  //turns led on and off based on sending 0 or 1 from serial terminal
  if (SerialUSB.available()) {
    char input = SerialUSB.read();
    if(input == '1'){
      digitalWrite(5, HIGH);    // Turn the relay on
      delay(1000);              // Wait for a second
      digitalWrite(5, LOW);     // Turn the relay off
      delay(1000);              // Wait for a second
    }
      
  }
  
   SerialUSB.delay(100);               // keep usb alive // can alos use SerialUSB.refresh();
}
