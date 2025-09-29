# Q3
hourly_views = [12, 34, 7, 50, 21, 5, 9, 0, 15, 40, 8, 26]


total_views = 0
for v in hourly_views:
    total_views += v


revenue = 0.0

if total_views <= 10:
    revenue = total_views * 0.50
elif total_views <= 30:
    revenue = 10 * 0.50 + (total_views - 10) * 0.30
else:
    revenue = 10 * 0.50 + 20 * 0.30 + (total_views - 30) * 0.10

print("Total Daily Views:", total_views)
print("Total Revenue: $", revenue)
