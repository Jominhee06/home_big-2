void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int i;
  
  for(i = 0; i < 256; i++)
  {
    analogWrite(10, i);
    delay(10);
  }
  
  for(i; i > 0; i--)
  {
    analogWrite(10, i);
    delay(10);
  }
}
