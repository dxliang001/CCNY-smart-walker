int vib_pin = 3;

void setup() 
{
  // put your setup code here, to run once:
  pinMode(vib_pin, OUTPUT);

}

void nVibrate(int numOfVib, int nInterval, int Intensity)
{
   for(int i = 0; i < numOfVib; ++i)
   {
    analogWrite(vib_pin, Intensity);
    delay(nInterval);
    analogWrite(vib_pin, 0);
    delay(nInterval);
   }
}
void loop() 
{
  // put your main code here, to run repeatedly:
  nVibrate(1, 2000, 100);
  delay(2000);
}
