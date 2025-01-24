class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no
        self.__seats = {} 
        self.__show_list = [] 
        Star_Cinema.entry_hall(self) 

    def entry_show(self, show_id, movie_name, time):
        show_tuple = (show_id, movie_name, time)
        self.__show_list.append(show_tuple)

        # Initialize seat layout (2D list)
        seats_layout = [['F' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seats_layout

    def book_seats(self, show_id, seat_list):
       
        if show_id not in self.__seats:
            print("Error: Invalid Show ID")
            return

        for row, col in seat_list:
            if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
                print(f"Error: Invalid seat ({row}, {col})")
                continue
            if self.__seats[show_id][row][col] == 'B':
                print(f"Error: Seat ({row}, {col}) is already booked")
            else:
                self.__seats[show_id][row][col] = 'B'
                print(f"Seat ({row}, {col}) booked successfully")

    def view_show_list(self):
        
        print("\nRunning Shows:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        
        if show_id not in self.__seats:
            print("Error: Invalid Show ID")
            return

        print(f"\nAvailable seats for show ID {show_id}:")
        for row in range(self.__rows):
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == 'F':
                    print(f"({row}, {col})", end=" ")
            print()


# # Testing the System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
# hall1 = Hall(5, 5, 101)  # Hall with 5x5 seats and hall_no 101
# hall1.entry_show("S1", "Avatar", "18:00")
# hall1.entry_show("S2", "Inception", "21:00")

# hall1.view_show_list()

# hall1.view_available_seats("S1")

# hall1.book_seats("S1", [(0, 1), (2, 2), (3, 4)])
# hall1.view_available_seats("S1")

# # Viewing all halls in the Star_Cinema
# print("\nAll Halls in Star_Cinema:")
# for hall in Star_Cinema.hall_list:
#     print(f"Hall No: {hall.hall_no}")
    
