song_length = int(input())
ticks_per_revolution = 4

revolutions = song_length / ticks_per_revolution
revolutions = round(revolutions, 2)  # Round to two decimal places

print(revolutions)
