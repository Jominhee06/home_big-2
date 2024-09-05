void setup() {
  // put your setup code here, to run once:
  pinMode(7, INPUT);
  pinMode(4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    int sw = digitalRead(7);
    Serial.println(sw);

    if(sw == HIGH)
    {
      digitalWrite(4,LOW);
      delay(10);
    }
    else
    {
      digitalWrite(4,HIGH);
    }
}
