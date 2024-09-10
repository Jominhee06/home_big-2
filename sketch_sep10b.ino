void setup() {
  // put your setup code here, to run once:
   pinMode(3,INPUT_PULLUP);
   Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
   int data = digitalRead(3);
   Serial.println(data);
}
