## Overview
The **Health and Hedons Tracker** is a Python-based simulation that models the relationship between activities, health, and happiness (hedons). Users perform activities like running, carrying textbooks, or resting, while the program tracks the cumulative effects on their health and hedons. The simulation incorporates user states (e.g., tiredness, star bonuses) to provide realistic outcomes and determine the most enjoyable activity at any given time.

## Features
- **Activity Simulation**: Models the effects of activities such as running, resting, and carrying textbooks.
- **State Management**: Tracks user states like "tired" or "not tired" based on activity history.
- **Star Bonuses**: Adds temporary incentives (stars) for specific activities to boost hedons.
- **Health and Hedons Calculation**: Updates metrics dynamically based on activity type and duration.
- **Recommendation System**: Suggests the most enjoyable activity based on current conditions.
- **Extensibility**: Modular design allows for adding new activities or features.

## How It Works
1. **Initialization**:
   - The simulation starts with the `initialize()` function, which sets up global variables for tracking health, hedons, time, activity history, and state.

2. **Performing Activities**:
   - The `perform_activity(activity, duration)` function updates health and hedons based on the type and duration of the activity.
   - States like "tired" influence the outcome, and star bonuses enhance hedons for a limited time.

3. **Star Bonuses**:
   - Stars can be offered to incentivize specific activities using the `offer_star(activity)` function.
   - Stars decay over time or after frequent use, introducing a "boredom" mechanic.

4. **Most Fun Activity**:
   - The `most_fun_activity_minute()` function suggests the most enjoyable activity based on the user's current state and available stars.

5. **Getters**:
   - Functions like `get_cur_health()` and `get_cur_hedons()` allow retrieval of current metrics.

## Example Usage
```python
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)
    print(get_cur_hedons())            # Output: -20
    print(get_cur_health())            # Output: 90
    print(most_fun_activity_minute())  # Output: "resting"
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/health-hedons-tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd health-hedons-tracker
   ```
3. Run the program with Python 3:
   ```bash
   python tracker.py
   ```
