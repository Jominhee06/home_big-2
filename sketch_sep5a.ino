#define RED 2
#define GREEN 4
#define BLUE 7

enum test{red,blue,green,white};

void setup() {
  // put your setup code here, to run once:
    pinMode(RED,OUTPUT);
    pinMode(GREEN,OUTPUT);
    pinMode(BLUE,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
    print_rgb(red);
    delay(1000);
    print_rgb(green);
    delay(1000);
    print_rgb(blue);
    delay(1000);
}
void print_rgb(int rgb)
{
    switch(rgb){
    case red:
        digitalWrite(RED,HIGH);
        digitalWrite(GREEN,LOW);
        digitalWrite(BLUE,LOW);
        delay(1000);
        break;
    case blue:
        digitalWrite(RED,LOW);
        digitalWrite(GREEN,LOW);
        digitalWrite(BLUE,HIGH);
        delay(1000);
        break;
    case green:
        digitalWrite(RED,LOW);
        digitalWrite(GREEN,HIGH);
        digitalWrite(BLUE,LOW);
        delay(1000);
        break;
    }
} 
