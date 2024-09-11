int trigPin1 = 10;
int echoPin1 = 9;
int buzzer = 12;

//변수를 설정합니다. 
long duration1, distance1;

void setup() {
  pinMode(trigPin1, OUTPUT); // trigPin을 출력으로 
  pinMode(echoPin1, INPUT); // echoPin을 입력이다.
  Serial.begin(9600); // 시리얼 포트를 시작합니다.
}

void loop() {
  //초음파 센서를 한번 초기화 하는 과정입니다. 마치 껏다 켯다를 하면서 거리를 초기화합니다.
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  duration1 = pulseIn(echoPin1, HIGH);
  distance1= duration1*0.034/2;


//여기에서부터 거리에 따른 소리의 크기를 코딩합니다.
  if (distance1 >= 100 || distance1 <= 0){ // 만일 거리가 100cm보다 크고 0보다 작다면, 즉 측정 범위를 넘어간 경우
    tone(buzzer, 100, 10);    // 부저 음의크기 100, 시간 10
    Serial.println("장애물이 없습니다."); //시리얼 프린트에 표시되는 부분 입니다.
    }
  else if(distance1 <= 60 && distance1 >= 51){ // 만일 거리가 60cm보다 작거나 같고 51cm보다 크거나 같다면
    tone(buzzer, 500, 50);    // 음 500, 시간 50
    Serial.println("60cm내에 장애물이있습니다.");
  }
  else if(distance1 <= 50 && distance1 >= 41){ // 만일 거리가 50cm보다 작거나 같고 41cm보다 크거나 같다면
    tone(buzzer, 1000, 100);    // 음 1000, 시간 100
    Serial.println("50cm내에 장애물이있습니다.");
  }
  else if(distance1 <= 40 && distance1 >= 31){ // 만일 거리가 40cm보다 작거나 같고 31cm보다 크거나 같다면
    tone(buzzer, 1500, 200);    // 음 1500, 시간 200
    Serial.println("40cm내에 장애물이있습니다.");
  }
  else if(distance1 <= 30 && distance1 >= 21){ // 만일 거리가 30cm보다 작거나 같고 21cm보다 크거나 같다면
    tone(buzzer, 2000, 400);    // 음 2000, 시간 400
    Serial.println("30cm내에 장애물이있습니다.");
  }
  else if(distance1 <= 20 && distance1 >= 11){ //  만일 거리가 20cm보다 작거나 같고 11cm보다 크거나 같다면
    tone(buzzer, 2500, 600);    // 음 2500, 시간 600
    Serial.println("20cm내에 장애물이있습니다.");
  }
  else if (distance1 <= 10 && distance1 >= 1){ //  만일 거리가 10cm보다 작거나 같고 1cm보다 크거나 같다면
    tone(buzzer, 3000, 1000);    // 음 3000, 시간 1000
    Serial.println("조심하세요!!");
  }
  
  delay(1000); // 1초마다 다시 실행합니다.1000이 일초를 뜻합니다. 

}


