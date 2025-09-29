# Q2: Hourly views graph using '*'

# Example hourly views data (you can change it)
hourly_views = [12, 34, 7, 50, 21, 5, 9, 0, 15, 40, 8, 26]

for hour in range(len(hourly_views)):
    stars = ""
    count = hourly_views[hour] // 5
    for _ in range(count):
        stars += "*"
    print("Hour", hour, ":", stars)
