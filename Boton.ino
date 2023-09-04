// constants won't change
const int buttonPin = 25; // ESP32connected to button's pin
const int LEDPin    = 26; // ESP32 pin connected to LED's pin
// variables will change:
int ledState = LOW;     // the current state of LED
int lastButtonState;    // the previous state of button
int currentButtonState; // the current state of button
void setup() {
  Serial.begin(9600);                // initialize serial
  pinMode(buttonPin, INPUT_PULLUP); // set ESP32 pin to input pull-up mode
  pinMode(LEDPin, OUTPUT);          // set ESP32 pin to output mode
  currentButtonState = digitalRead(buttonPin);
}
void loop() {
  lastButtonState    = currentButtonState;      // save the last state
  currentButtonState = digitalRead(buttonPin); // read new state
  if(lastButtonState == HIGH && currentButtonState == LOW) {
    Serial.println("The button is pressed");
    // toggle state of LED
    ledState = !ledState;
    // control LED arccoding to the toggled state
    digitalWrite(LEDPin, ledState); 
  }
  delay(100);
}