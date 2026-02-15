class StudioBooking:
    studio_name = "Harmony Studios"
    total_bookings = 0
    def __init__(self,artist_name,session_id,equipment = None):
        self.artist_name = artist_name
        self.session_id = session_id
        if equipment == None:
            self.equipment = []
        else:
            self.equipment = equipment
        StudioBooking.total_bookings += 1
    def book_equipment(self,item_name):
        if item_name is not None and len(item_name) > 0:
            self.equipment.append(item_name)
            print(f"Booked equipment: {item_name}")
    def return_equipment(self,item_name):
        if item_name in self.equipment:
            self.equipment.remove(item_name)
            print(f"Returned equipment: {item_name}")
        else:
            print("Equipment not booked")
    def display_booking(self):
        print(f"Session {self.session_id} for {self.artist_name} at {StudioBooking.studio_name}")

booking_1 = StudioBooking("Daler","M-501")
booking_2 = StudioBooking("Nargiza","M-502")
booking_1.display_booking()
booking_1.book_equipment("Guitar")
booking_1.book_equipment("Microphone")
booking_1.return_equipment("Microphone")
booking_2.display_booking()
booking_2.return_equipment("Drums")
print(f"Total bookings: {StudioBooking.total_bookings}")