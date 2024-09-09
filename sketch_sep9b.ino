// 푸시버튼을 슬라이드 스위치처럼 사용하기

int flag = 0;    //  상태 구분하기 위한 변수

void setup() {
  // put your setup code here, to run once:
  pinMode(8,OUTPUT);
  pinMode(6,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  int inputValue = digitalRead(6);   

  if(inputValue == HIGH){    // 푸시버튼이 눌렸을 때
    if(flag == 0)            // 꺼짐상태이면 켜짐상태로 변경
      flag = 1;
  
  }else{                                // 푸시버튼이 떼어졌을 때
    if(flag == 1){
      int ledStatus = digitalRead(8);   // 현재 LED의 상태를 읽음
      if(ledStatus == HIGH)             // LED의 상태가 켜지이면 꺼짐으로 변경  
          digitalWrite(8, LOW);    
      else                              // LED의 상태가 꺼짐이면 켜짐으로 변경
          digitalWrite(8, HIGH);
      flag = 0;                         // 상태 구분 변수를 초기화
    }
  }
  delay(100);
}

