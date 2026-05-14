int echoPin = 10; // echo
int trigPin = 9; // trigger
int echoValue = 0;

void setup() {
  pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  // Clears the trigger
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  // Sets the trigger on HIGH state for 10 seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  // Set back trigger to LOW state
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  echoValue = pulseIn(echoPin, HIGH);

  if(echoValue > 0){
    Serial.println(echoValue);
  } else if(echoValue < 0) {
    Serial.println("invalid_distance");
  } else {
    // do nothing
  }
}
