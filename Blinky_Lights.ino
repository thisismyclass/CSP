#include <Adafruit_CircuitPlayground.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  CircuitPlayground.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  if (CircuitPlayground.rightButton()){
    Serial.println(CircuitPlayground.rightButton());
    for(int i=0; i<11; i=i+1) {
      CircuitPlayground.setPixelColor(i,0,255,0);
    }
    CircuitPlayground.playTone(1000,10);
    CircuitPlayground.clearPixels();
    delay(200);
  }


  if (CircuitPlayground.leftButton()){
    Serial.println(CircuitPlayground.leftButton());
    for(int i=0; i<11; i=i+1) {
      CircuitPlayground.setPixelColor(i,255,0,0);
    }
    CircuitPlayground.playTone(1000,10);
    CircuitPlayground.clearPixels();
    delay(100);
  }   

}
