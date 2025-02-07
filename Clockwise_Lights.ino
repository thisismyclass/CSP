#include <Adafruit_CircuitPlayground.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  CircuitPlayground.begin();
}
int n = 10;
int l = 25;

void loop() {
  // put your main code here, to run repeatedly:
  if (CircuitPlayground.rightButton()){
    n = n+10;
    l = l+5;
    for(int i=9; i>=0; i--) {
      CircuitPlayground.setPixelColor(i,0,255,0);
      delay(30);
      CircuitPlayground.playTone(1000,1);
      CircuitPlayground.setPixelColor(i,255,0,0);
    }
  }

}
