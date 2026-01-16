flights = [
    {"Date": "9/6/25", "hours": 1.5, "solo": False, "landings": 3},
    {"Date": "3/5/25", "hours": 1.2, "solo": False, "landings": 5},
    {"Date": "1/25/26", "hours": 2.0, "solo": False, "landings": 2}
]


def calc_flt_time(flight_list, required_hours):
    """
    Calculates total hours and progress toward license
    Has sequencing, selection, and iteration
    """

    total_hours = 0
    solo_hours = 0
    total_landings = 0


    for flight in flight_list:
        total_hours += flight["hours"]
        total_landings += flight["landings"]


        if flight["solo"]:
            solo_hours += flight["hours"]


    progress = (total_hours / required_hours) * 100


    if total_hours >= required_hours:
        status = "Ready for license!"
    elif total_hours >= required_hours * 0.75:
        status = "3/4ths of the way there!"
    elif total_hours >= required_hours * 0.5:
        status = "Halfway"
    else:
        status = "Keep practicing!"


    remaining = required_hours - total_hours
    if remaining < 0:
        remaining = 0

    return total_hours, solo_hours, total_landings, progress, status, remaining



print("=" * 50)
print("      Flight School Logbook")
print("=" * 50)
while True:
    print("\n1. Add New Flight")
    print("2. View Progress")
    print("3. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":

        print("\n--- ADD NEW FLIGHT ---")
        date = input("Date: ")
        hours = float(input("Hours flown: "))
        landings = int(input("Number of landings: "))
        solo_input = input("Solo flight? (Y/N): ")

        solo = True if solo_input == "Y" else False

        new_flight = {"date": date, "hours": hours, "solo": solo, "landings": landings}
        flights.append(new_flight)

        print("\nFlight added!")

    elif choice == "2":

        total, solo, landings, percent, message, left = calc_flt_time(flights, 40)


        print("\n" + "=" * 50)
        print("Flight Time Report")
        print("=" * 50)
        print(f"Total Hours:      {total}")
        print(f"Solo Hours:       {solo}")
        print(f"Total Landings:   {landings}")
        print(f"Progress:         {percent:.1f}%")
        print(f"Hours Remaining:  {left}")
        print(f"Status:           {message}")
        print("=" * 50)

    elif choice == "3":
        print("\nThanks for using Flight Logbook!")
        break

    else:
        print("\n Invalid choice")

