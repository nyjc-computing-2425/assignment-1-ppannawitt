seconds = input('Enter the number of seconds (integer): ')
seconds = int(seconds)
hours, seconds = divmod(seconds, 3600)
minutes, seconds = divmod(seconds, 60)

print("The duration is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")