#define TRIG 10 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 9 //ECHO 핀 설정 (초음파 받는 핀)
int Buzzer = 13;    // 버저 핀을 13번에 연결
int SORI_PIN = 12;
int numTones = 61;
//int Sensor = 9;    // 센서핀은 9번에 연결
int tones[16] = {0, 261, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 783, 880, 987, 1046};
//int tones1[20] = {};//연주음악 번호입력
int times[] = {500,1000, 1500, 3000}; // 8분읍표, 4분음표, 점4분음표, 점2분음표
int val;
int i;

int arr_eum[] = {
    5,8,7,6, 8,5,3,5, 8,9,10,11,10,9,0,
    12,11,10,9, 8,7,6,5,3, 5,8,9,9,10,8,0,
    7,8,9,7, 10,11,12,10, 9,8,7,8,9,0,
    12,11,10,9, 8,7,6,5,3, 5,8,9,9,10,8,0};

int arr_time[] = {
    1,2,0,1, 1,1,1,1, 1,0,0,2,0,3,1,
    2,0,1,1, 1,0,0,1,1, 1,1,0,0,1,3,1,
    2,0,1,1, 2,0,1,1, 1,1,1,1,3,1,
    2,0,1,1, 1,0,0,1,1, 1,1,0,0,1,2,1};

void setup() {

  Serial.begin(9600); //PC모니터로 센서값을 확인하기위해서 시리얼 통신을 정의해줍니다. 

                       //시리얼 통신을 이용해 PC모니터로 데이터 값을 확인하는 부분은 자주사용되기 때문에

                       //필수로 습득해야하는 교육코스 입니다.

  
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT); //초음파센서
  pinMode(Buzzer, OUTPUT);   // 버저를 출력으로 설정
}


void loop()

{

  long duration, distance;
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn (ECHO, HIGH); //물체에 반사되어돌아온 초음파의 시간을 변수에 저장합니다.
 //34000*초음파가 물체로 부터 반사되어 돌아오는시간 /1000000 / 2(왕복값이아니라 편도값이기때문에 나누기2를 해줍니다.)
 //초음파센서의 거리값이 위 계산값과 동일하게 Cm로 환산되는 계산공식 입니다. 수식이 간단해지도록 적용했습니다.
  distance = duration * 17 / 1000; 
  //PC모니터로 초음파 거리값을 확인 하는 코드 입니다.
  Serial.println(duration ); //초음파가 반사되어 돌아오는 시간을 보여줍니다.
  Serial.print("\nDIstance : ");
  Serial.print(distance); //측정된 물체로부터 거리값(cm값)을 보여줍니다.
  Serial.println(" Cm");
  delay(500); //1초마다 측정값을 보여줍니다.
//val = digitalRead(Sensor);  // 센서값 읽어옴
  if (distance < 10) {          // 장애물 감지가 안되면
    for(numTones = 0; numTones < 10; numTones++)  {
    noTone(7);                // 버저가 울리지 않는다
    delay(50);
    }
  } 
  else if (distance > 20 &&distance < 40) {          // 장애물 감지가 안되면
    for(numTones = 25; numTones >= 0; numTones--) {                  // 장애물이 감지되면
        tone(Buzzer, tones[numTones]);
        delay(100);
    }
  }
  else if(distance > 60){
    for(numTones = 30; numTones >= 0; numTones--) {                  // 장애물이 감지되면
        tone(Buzzer, tones[numTones]);
        delay(200);
    }
  }
  else{
    for(i=0; i<numTones; i++)
    {
      if(tones[arr_eum[i]]==0) noTone(SORI_PIN); // 쉼표
      else tone(SORI_PIN, tones[arr_eum[i]]); // 음표
      delay(times[arr_time[i]]/2);
    
      noTone(SORI_PIN);
      delay(50);
      // noTone(8);  
  }
    noTone(Buzzer);
    delay(1000);
  }
}

