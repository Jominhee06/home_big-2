#include <SoftwareSerial.h>

int tx = 12;
int rx = 13;

char ary[10]; // 입력을 저장할 배열
static int i = 0; // 배열의 인덱스

SoftwareSerial pad_serial(tx, rx);

void setup() {
    Serial.begin(9600);
    pad_serial.begin(9600);
}

void loop() {
    if (pad_serial.available()) {
        char input = pad_serial.read(); // 소프트웨어 시리얼에서 입력 읽기

        if (input == '#') {
            ary[i] = '\0'; // 문자열 종료
            int key = atoi(ary); // 문자열을 정수로 변환
            i = 0; // 인덱스 초기화

            if (key == 1234) {
                Serial.println("Success");
            } else {
                Serial.println("FALL");
            }
        } else {
            if (i < sizeof(ary) - 1) { // 배열의 크기를 넘지 않도록 체크
                ary[i++] = input; // 입력을 배열에 저장하고 인덱스 증가
            }
        }
    }
}

//       Serial.write(pad_serial.read());
//     if(Serial.available())
//       pad_serial.write(Serial.read());
// }