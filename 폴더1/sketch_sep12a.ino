//#define SORI 5
int SORI_PIN = 4;

int tones[] = {0, 261, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 783, 880, 987, 1046}; // NULL,도,레,레,미, ..., 도
int times[] = {500,1000, 1500, 3000}; // 8분읍표, 4분음표, 점4분음표, 점2분음표

// 부저의 주파수로 각 각 "도레미파솔라시도" 이다.
//int um[8] = {262,294,330,340,392,440,494,523};

// // 음과 음의 길이를 표현하는 구조체
// typedef struct
// {
//   int t;            // 음
//   unsigned long d;  // 음의길이
// }MAD;


// MAD music[]={
//   {G,100},{G,100},{A,100},{A,100},{G,100},{G,100},{E,200},
//   {G,100},{G,100},{E,100},{E,100},{D,200},
//   {G,100},{G,100},{A,100},{A,100},{G,100},{G,100},{E,200},
//   {G,100},{E,100},{C,200}
// };
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

int numTones = 61;

//int musicLen; // music 배열의 길이

void setup() {
  // put your setup code here, to run once:
    //pinMode(SORI,OUTPUT);
    //musicLen = sizeof(music) / sizeof(MAD);
}

void loop() {
  // put your main code here, to run repeatedly:
  //for(int hz = 0; hz < 8; hz++)
  // for(int i = 0; i < musicLen; i++)
  // {
  //     //tone(SORI, um[hz], 200); // 해당 주파수를 200은 길이
  //     tone(SORI, music[i].t);
  //     //digitalWrite(SORI,hz);

  //     delay(music[i].d*5);

    int i;
    for(i=0; i<numTones; i++)
    {
      if(tones[arr_eum[i]]==0) noTone(SORI_PIN); // 쉼표
      else tone(SORI_PIN, tones[arr_eum[i]]); // 음표
      delay(times[arr_time[i]]/2);
    
      noTone(SORI_PIN);
      delay(50);
      // noTone(8);  
  }
  
  // for(int hz = 750; hz >= 300; hz--)
  // {
  //     digitalWrite(SORI,hz);
      
  //     delay(150);
  // }
  // 한 곡이 끝나고 1초 쉬자
  delay(5000);
}
