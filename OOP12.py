# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    


c1 = TemperatureConverter.celsius_to_fahrenheit(20)

print(f"20C is {c1}F")








