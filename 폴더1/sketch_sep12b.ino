int R_LED_pin = 12;  // 아두이노의 12번 핀을 빨간 LED핀으로 사용
int G_LED_pin = 13;  // 13번 핀을 초록 LED핀으로 사용
int SW_pin1 = 7;     // 4번 핀을 첫번째 스위치 핀으로 사용
int SW_pin2 = 8;     // 5번 핀을 두번째 스위치 핀으로 사용

void setup() {  
  pinMode(R_LED_pin, OUTPUT);     // 빨간 LED핀을 출력으로 사용
  pinMode(G_LED_pin, OUTPUT);     // 초록 LED핀을 출력으로 사용
  pinMode(SW_pin1, INPUT_PULLUP); // 1번스위치 핀을 풀업저항이 있는 입력으로 사용
  pinMode(SW_pin2, INPUT_PULLUP); // 2번스위치 핀을 풀업저항이 있는 입력으로 사용
}
void loop() {  
  if ((digitalRead(SW_pin1) == LOW) && (digitalRead(SW_pin2) == LOW)){   
    // 1번 스위치와 2번 스위치를 동시에 눌렀을 때 
    digitalWrite(R_LED_pin, HIGH);      // 빨간 LED 점등                  
    digitalWrite(G_LED_pin, HIGH);      // 초록 LED 점등
  }else if (digitalRead(SW_pin1) == LOW) {  // 1번 스위치를 눌렀을 때
    digitalWrite(R_LED_pin, HIGH);      // 빨간 LED 점등
    digitalWrite(G_LED_pin, LOW);       // 초록 LED 소등
  }else if (digitalRead(SW_pin2) == LOW){   // 2번 스위치를 눌렀을 때 
    digitalWrite(R_LED_pin, LOW);       // 빨간 LED 소등
    digitalWrite(G_LED_pin, HIGH);      // 초록 LED 점등
  }else {                                   // 이외(아무 스위치를 누르지 않으면)
    digitalWrite(R_LED_pin, LOW);       // 빨간 LED 소등
    digitalWrite(G_LED_pin, LOW);       // 초록 LED 소등
  }
}
