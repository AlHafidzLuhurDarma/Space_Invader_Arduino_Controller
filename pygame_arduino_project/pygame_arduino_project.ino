int buttonRight = 7;
int buttonLeft = 8;
int buttonShot = 9;
int buttonUp = 10;
int rightVal;
int leftVal;
int shotVal;
int upVal;
int buttonVal;
int dt = 100;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(buttonRight, INPUT);
pinMode(buttonLeft, INPUT);
pinMode(buttonShot, INPUT);
pinMode(buttonUp, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
rightVal = digitalRead(buttonRight);
leftVal = digitalRead(buttonLeft);
shotVal = digitalRead(buttonShot);
upVal = digitalRead(buttonUp);

if (rightVal == 0){
  Serial.println("Kanan");
  }
if (leftVal == 0){
  Serial.println("Kiri");
  }
if (shotVal == 0){
  Serial.println("Shot");
  }
if (upVal == 0){
  Serial.println("Up");
  }

else{
  Serial.println('1');
  }
delay (dt);
}
