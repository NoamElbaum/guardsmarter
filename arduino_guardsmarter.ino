#include <Servo.h>
#define intPin 2

Servo gate;

char command = 'c';
int gate_pos = 90;

void setup() 
{
  Serial.begin(9600);
  gate.attach(9);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
  attachInterrupt(digitalPinToInterrupt(intPin), help, RISING)
}

void loop() 
{
  gate.write(gate_pos);
  if(Serial.available())
  { 
    command = Serial.read();
    Serial.println(command);
  }
  if(command == 'c')
  {
    digitalWrite(13, LOW);
    gate_pos = 90;
  }
  else if(command == 'o')
  {
   digitalWrite(13,HIGH);
   gate_pos = 180; 
  }
}

void help()
{
  while(!Serial.available())
  {
    Serial.ptintln('h');
  }
  char val = Serial.read();
  if(val != 'g')
    help();
}
