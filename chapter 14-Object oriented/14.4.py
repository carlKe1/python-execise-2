#  Write a class called Time whose only field is a time in seconds. It should have a method called
# convert_to_minutes that returns a string of minutes and seconds formatted as in the following example: if seconds is 230, the method should return '5:50'. It should also have
# a method called convert_to_hours that returns a string of hours, minutes, and seconds
# formatted analogously to the previous method.

class Time:
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        return f"{minutes}:{seconds:02d}"

    def convert_to_hours(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        return f"{hours}:{minutes:02d}:{seconds:02d}"

# Example usage
time = Time(230)
print(time.convert_to_minutes())  # Output: "3:50"
print(time.convert_to_hours())  # Output: "0:03:50"
