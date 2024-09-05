void setup() {
  // put your setup code here, to run once:
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

static int bar = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()) // available -> 수신버퍼에 있는지 없는지를 확인한다. 
  {
    char rx = Serial.read();
    Serial.println(rx);
    if(rx == '+')  
    {
      bar += 10;
      analogWrite(10,bar);
      delay(10);
      if(bar > 255)
      {
        analogWrite(10,250);
      }
    }
    else if (rx == '-') 
    {
      bar -= 10;
      analogWrite(10,bar);
      delay(10);
      if(bar < 0)
      { 
        analogWrite(10,0);       
      }
    }
    else 
    {
      analogWrite(10,0);
    }
  }
}

