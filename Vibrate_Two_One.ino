int vib_pin = 3;

void setup() 
{
  pinMode(vib_pin, OUTPUT);

}

void nVibrate(int numOfVib, int nInterval, int Intensity)
{
   for(int i = 0; i < numOfVib; ++i)
   {
    //write to the pin to start vibration with specified intensity
    analogWrite(vib_pin, Intensity);
    delay(nInterval);
    //stop vibration but giving it 0 intensity
    analogWrite(vib_pin, 0);
    delay(nInterval);
   }
}
void loop() 
{
  delay(1000);
  //vibrate twice every second at an intensity of
  //255
  nVibrate(2, 1000, 255);
}
