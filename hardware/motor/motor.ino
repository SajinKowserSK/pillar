
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int dispense = 0;
void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  Serial.begin(9600); // set the baud rate
  Serial.println("Ready"); // print "Ready" once
 }

void loop() {
  char inByte = ' ';
  if(Serial.available()){
    if (dispense == 0) {
      up();
      dispense = 1;
    } else {
      down();
      dispense = 0;
    }
   }
  delay(2000); // delay for 1/10 of a second
}


void down() {
  for (pos = 150; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(1);                       // waits 15ms for the servo to reach the position
  }
}

void up() {
   for (pos = 0; pos <= 150; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
