String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(19200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  pinMode(13,OUTPUT);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    if (inputString.equals("RESET")){
      delay(500);
      Serial.println("READY, SAGAIN PE Loader, ROM Ver. 1.1.6, 12APR2001");
    } else if (inputString.startsWith("MOVE")){
      delay(3000);
      Serial.println("READY");
      } else if (inputString.equals("GRIPPER OPEN")){
      delay(500);
      Serial.println("READY, OPEN");
      } else if (inputString.equals("GRIPPER CLOSED")){
      delay(500);
      Serial.println("READY, CLOSED, NOPLATE");
      } else if (inputString.equals("Z-AXIS EXTEND")){
      delay(500);
      Serial.println("READY, EXTENDED");
      } else if (inputString.equals("Z-AXIS RETRACT")){
      delay(500);
      Serial.println("READY, RETRACTED");
    } else {
      Serial.print("Unkown command --> ");
      Serial.println(inputString);
    }
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } else {
        inputString += inChar;
    }
  }
}
