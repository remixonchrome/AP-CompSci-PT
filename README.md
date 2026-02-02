# Flight School Logbook

A Python program to track flight training hours and progress toward getting your pilot's license.

## About This Project

This is a command-line flight logbook that helps student pilots keep track of their training. You need 40 hours to get your license, so this calculates your total time, solo hours, landings, and shows you exactly how close you are to that goal.

### Main Menu
1. **Add New Flight** - enter a new flight into your logbook
2. **View Progress** - see a full report of your training stats
3. **Exit** - close the program

### Adding a Flight
When you select option 1, you'll be prompted for:
- **Date**: enter in any format (ex: "9/6/25")
- **Hours flown**: decimal number (ex: 1.5)
- **Number of landings**: whole number (ex: 3)
- **Solo flight?**: type Y for yes, N for no

### Viewing Progress
Option 2 shows you a detailed report with:
- Total flight hours
- Solo hours
- Total landings
- Progress percentage (out of 40 hours)
- Hours remaining
- Status message

## Technical Specifications

### The `calc_flt_time()` Function

This is the main function that does all the calculations. It takes your flight list and the required hours (40), then returns everything you need to know.

**What it demonstrates:**
- **Sequencing** - instructions execute in order
- **Selection** - uses if/elif/else to determine status messages
- **Iteration** - loops through the flight list with a for loop

**Returns:** (total_hours, solo_hours, total_landings, progress, status, remaining)

### Progress Messages

The program gives you different messages based on completion:
- **0-49%**: "Keep practicing!"
- **50-74%**: "Halfway"
- **75-99%**: "3/4ths of the way there!"
- **100%+**: "Ready for license!"

## Structure

```python
# Flight data stored as list of dictionaries
flights = [
    {"Date": "9/6/25", "hours": 1.5, "solo": False, "landings": 3},
    # more flights...
]

# Main calculation function
calc_flt_time(flight_list, required_hours)

# Menu loop with user input
while True:
    # menu options
```

## Future Ideas

Things I might add later:
- Save data to a file so flights persist between sessions
- Track different flight types (cross-country, night, etc.)
- Add instructor names
- Export logbook to PDF or CSV
- Visual progress bar

## Sample Output

```
==================================================
      Flight School Logbook
==================================================

1. Add New Flight
2. View Progress
3. Exit

Choose option: 2

==================================================
Flight Time Report
==================================================
Total Hours:      4.7
Solo Hours:       0
Total Landings:   10
Progress:         11.8%
Hours Remaining:  35.3
Status:           Keep practicing!
==================================================
```