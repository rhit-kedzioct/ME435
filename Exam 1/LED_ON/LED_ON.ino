String inputString = "";
bool isStringComplete = false;

int ledPin = 13;

void setup() {
  Serial.begin(19200);
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  inputString.reserve(200);
}

void loop() {
  if (isStringComplete) {
    inputString.trim();

    if (inputString.equals("LED ON")) {
      digitalWrite(ledPin, HIGH);
      Serial.println("LED On");

    } else if (inputString.equals("LED OFF")) {
      digitalWrite(ledPin, LOW);
      Serial.println("LED Off");

    } else if (inputString.startsWith("FLASH")) {
      handleFlash(inputString.substring(5));

    } else {
      Serial.print("Unknown command --> ");
      Serial.println(inputString);
    }

    inputString = "";
    isStringComplete = false;
  }
}

void handleFlash(String params) {
  params.trim();

  int spaceIndex = params.indexOf(' ');

  if (spaceIndex == -1) {
    Serial.print("Unknown command --> ");
    Serial.println(inputString);
    return;
  }

  String flashesParam = params.substring(0, spaceIndex);
  String periodParam = params.substring(spaceIndex + 1);

  flashesParam.trim();
  periodParam.trim();

  int flashes = flashesParam.toInt();
  int periodMs = periodParam.toInt();

  Serial.print("Flashes = ");
  Serial.print(flashes);
  Serial.print(" PeriodMs = ");
  Serial.println(periodMs);

  for (int i = 0; i < flashes; i++) {
    digitalWrite(ledPin, HIGH);
    delay(periodMs / 2);
    digitalWrite(ledPin, LOW);
    delay(periodMs - periodMs / 2);
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();

    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}