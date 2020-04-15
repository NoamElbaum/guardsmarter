#include <Servo.h>
#include <MFRC522.h>

#define gate_servo 6
#define intPin     2
#define RST_PIN    9           // Configurable, see typical pin layout above
#define SS_PIN     10          // Configurable, see typical pin layout above

Servo gate;
MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

char command = 'c';
int gate_pos = 90;

void setup() 
{
  Serial.begin(9600);
  SPI.begin();                                           // Init SPI bus
  mfrc522.PCD_Init();                                    // Init MFRC522 card
  
  gate.attach(gate_servo);
  pinMode(13,OUTPUT);
  digitalWrite(13,LOW);
  attachInterrupt(digitalPinToInterrupt(intPin), help, RISING);
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
  else if(command == 'r')
    RFID_read();
}

void help()
{
  while(!Serial.available())
  {
    Serial.println('h');
  }
  char val = Serial.read();
  if(val != 'g')
    help();
}

void RFID_read() 
{  
  // Reset the func if no new card present on the sensor/reader.
  if ( ! mfrc522.PICC_IsNewCardPresent())
    RFID_read();

  // Select one of the cards 
  if ( ! mfrc522.PICC_ReadCardSerial())   
    RFID_read();

  //send the info from the card to the Serial bus
  mfrc522.PICC_DumpToSerial(&(mfrc522.uid)); 
}
