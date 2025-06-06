# Room Allocation System with Availability and Charges

# Sample room data: Room Number : [Room Type, Availability (True=Available), Charge per Night]
rooms = {
    101: ["Single", True, 3000],
    102: ["Single", True, 3000],
    201: ["Double", True, 4500],
    202: ["Double", True, 4500],
    301: ["Deluxe", True, 6000],
    302: ["Deluxe", True, 6000],
}

# Store bookings: Room Number : visitor Name
bookings = {}

def show_available_rooms():
    print("\nAvailable Rooms:")
    found = False
    for room_no, details in rooms.items():
        if details[1]:  # Available
            print(f"Room {room_no} | Type: {details[0]} | Charge: KES {details[2]}")
            found = True
    if not found:
        print("No rooms are currently available.")

def book_room():
    show_available_rooms()
    try:
        room_no = int(input("\nEnter room number to book: "))
        if room_no in rooms and rooms[room_no][1]:
            visitor = input("Enter visitor name: ")
            nights = int(input("Enter number of nights: "))
            total_cost = rooms[room_no][2] * nights
            bookings[room_no] = visitor
            rooms[room_no][1] = False
            print(f"\nRoom {room_no} successfully booked for {visitor}. Total charge: KES {total_cost}")
        else:
            print("Room is not available or doesn't exist.")
    except ValueError:
        print("Invalid input. Please enter a valid room number and number of nights.")

def view_bookings():
    if not bookings:
        print("\nNo bookings yet.")
    else:
        print("\nCurrent Bookings:")
        for room, visitor in bookings.items():
            print(f"Room {room} booked by {visitor} | Type: {rooms[room][0]} | Charge per night: KES {rooms[room][2]}")

def main():
    while True:
        print("\n=== Room Allocation System ===")
        print("1. Show Available Rooms")
        print("2. Book a Room")
        print("3. View All Bookings")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            show_available_rooms()
        elif choice == '2':
            book_room()
        elif choice == '3':
            view_bookings()
        elif choice == '4':
            print("Exiting Room Allocation System.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
