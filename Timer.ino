#include <Adafruit_CircuitPlayground.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  CircuitPlayground.begin();

}
int n = -1;
void loop() {
  // put your main code here, to run repeatedly:
  if(CircuitPlayground.leftButton()) {
    n = n+1;
    CircuitPlayground.setPixelColor(n,255,0,0);
    delay(500);
  }
  if(CircuitPlayground.rightButton()) {
    for(n=n; n>=0; n=n-1) {
      delay(1000);
      CircuitPlayground.setPixelColor(n,0,255,0);
    }
    for(int i=5; i>0; i=i-1) {
      CircuitPlayground.playTone(1000,100);
      delay(10);
    }
  delay(500);
    for(int i=5; i>0; i=i-1) {
      CircuitPlayground.playTone(1000,100);
      delay(10);
    }

  CircuitPlayground.clearPixels();
  }
}
