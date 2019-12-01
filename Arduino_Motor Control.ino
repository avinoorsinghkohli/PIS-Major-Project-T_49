const int left0=2;
const int left1=3;
const int right0=8;
const int right1=9;
const int led=13;
int incomingByte;


void setup() {
  Serial.begin(9600);
   pinMode(led,OUTPUT);
  // put your setup code here, to run once:
pinMode(left0,OUTPUT);
pinMode(left1,OUTPUT);
pinMode(right0,OUTPUT);
pinMode(right1,OUTPUT);
}

void loop() {
  if(Serial.available()>0)
  {
    incomingByte=Serial.read();
    if(incomingByte=='G')
    {digitalWrite(led,HIGH);
  
  // put your main code here, to run repeatedly:
digitalWrite(left0,HIGH);
digitalWrite(left1,LOW);
pinMode(right0,HIGH);
pinMode(right1,LOW);
}
if (incomingByte =='S'){
  digitalWrite(led,LOW);
  digitalWrite(left0,LOW);
digitalWrite(left1,LOW);
pinMode(right0,LOW);
pinMode(right1,LOW);
delay(3000);
digitalWrite(led,HIGH);
digitalWrite(left0,HIGH);
digitalWrite(left1,LOW);
pinMode(right0,HIGH);
pinMode(right1,LOW);}
  
}
}
