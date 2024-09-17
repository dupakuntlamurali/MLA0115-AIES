class VacuumCleaner:
    def __init__(self, initial_state):
        # Initial state: [(Room_A, Room_B), vacuum_position]
        # Room_A, Room_B can be 'dirty' or 'clean'
        # vacuum_position can be 'A' or 'B'
        self.state = initial_state
        self.moves = 0

    def display_state(self):
        print(f"Room A: {self.state[0][0]}, Room B: {self.state[0][1]}, Vacuum Position: {self.state[1]}")

    def clean(self):
        # Check where the vacuum is and clean the room if dirty
        if self.state[1] == 'A' and self.state[0][0] == 'dirty':
            print("Cleaning Room A...")
            self.state[0][0] = 'clean'
            self.moves += 1
        elif self.state[1] == 'B' and self.state[0][1] == 'dirty':
            print("Cleaning Room B...")
            self.state[0][1] = 'clean'
            self.moves += 1

    def move_left(self):
        if self.state[1] == 'B':
            print("Moving vacuum to Room A...")
            self.state[1] = 'A'
            self.moves += 1

    def move_right(self):
        if self.state[1] == 'A':
            print("Moving vacuum to Room B...")
            self.state[1] = 'B'
            self.moves += 1

    def is_clean(self):
        return self.state[0] == ['clean', 'clean']

    def solve(self):
        # Display initial state
        print("Initial state:")
        self.display_state()

        # Continue until both rooms are clean
        while not self.is_clean():
            # If vacuum is in Room A, clean or move
            if self.state[1] == 'A':
                if self.state[0][0] == 'dirty':
                    self.clean()
                else:
                    self.move_right()

            # If vacuum is in Room B, clean or move
            elif self.state[1] == 'B':
                if self.state[0][1] == 'dirty':
                    self.clean()
                else:
                    self.move_left()

        # Display final state
        print("\nFinal state:")
        self.display_state()
        print(f"Total moves: {self.moves}")

# Test the Vacuum Cleaner Problem
initial_state = [['dirty', 'dirty'], 'A']  # Both rooms dirty, vacuum starts in Room A
vacuum = VacuumCleaner(initial_state)
vacuum.solve()
