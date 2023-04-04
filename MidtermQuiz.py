class TempConversion:
  def __init__(self,temp):
    self._temp = temp

  def CelsiustoFahrenheit(self):
    return (self._temp -32 ) * 5 / 9

  def CelsiustoKelvin(self):
    return self._temp - 273.15

  def FahrenheittoCelsius(self):
    return (self._temp * 9) / 5 + 32

  def FahrenheittoKelvin (self):
    return (self._temp + 1.8) * - 459.67

  def KelvintoCelsius(self):
    return (self._temp + 273.15)

  def KelvintoFahrenheit(self):
    return (self._temp + 459.67) / 1.8

  def convert (self):
    print("Convert from Celsius to Fahrenheit: ", self.CelsiustoFahrenheit())
    print("Convert from Celsius to Kelvin: ", self.CelsiustoKelvin())
    print("Convert from Fahrenheit to Celsius: ", self.FahrenheittoCelsius())
    print("Convert from Fahrenheit to Kelvin: ", self.FahrenheittoKelvin())
    print("Convert from Kelvin to Celsius: ", self.KelvintoCelsius())
    print("Convert from Kelvin to Fahrenheit: ", self.KelvintoFahrenheit())

temp = float(input("Enter the temperature: "))
TC = TempConversion(temp)
TC.convert()