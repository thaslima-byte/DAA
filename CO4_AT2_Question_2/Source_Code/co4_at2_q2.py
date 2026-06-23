# Smart Grid Load Forecasting using Dynamic Programming

import time

# Historical electricity demand (in MW)
historical_load = [120, 135, 150, 145, 160, 170, 180]

# Memoization dictionary
memo = {}

# Dynamic Programming based forecasting
def forecast_load(day):
    if day in memo:
        return memo[day]

    # Base case
    if day < len(historical_load):
        memo[day] = historical_load[day]
        return memo[day]

    # Forecast using previous two days' average
    memo[day] = (forecast_load(day - 1) +
                 forecast_load(day - 2)) / 2

    return memo[day]


print("SMART GRID LOAD FORECASTING")
print("--------------------------------")

print("\nHistorical Load Data (MW):")
print(historical_load)

start = time.perf_counter()

future_days = 3

print("\nForecasted Load:")

for i in range(len(historical_load),
               len(historical_load) + future_days):

    predicted = forecast_load(i)
    print(f"Day {i + 1}: {predicted:.2f} MW")

end = time.perf_counter()

print("\nExecution Time:", end - start, "seconds")

print("\nAnalysis:")
print("- Dynamic Programming avoids redundant calculations.")
print("- Historical demand patterns are reused efficiently.")
print("- The model adapts to changing load conditions.")
print("- Forecasting helps optimize energy distribution.")