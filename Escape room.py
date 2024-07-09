import time
import threading

class Room:
    def __init__(self, name, description, puzzle, solution, clue):
        self.name = name
        self.description = description
        self.puzzle = puzzle
        self.solution = solution
        self.clue = clue

    def solve(self, answer):
        return answer.lower() == self.solution.lower()

class EscapeRoom:
    def __init__(self):
        self.rooms = [
            Room("The Enigma Entryway", "A room filled with strange symbols and cryptic messages.", 
                 "Decipher the code to unlock the next door.", "enigma",
                 "Decipher the wingdings message."),
            Room("The Whispering Library", "Bookshelves line the walls, and a mysterious breeze seems to whisper clues.", 
                 "Find the right book to progress.", "whisper",
                 "Listen carefully to the breeze, it might be spelling something."),
            Room("The Illusionist's Chamber", "Nothing is as it seems in this room of optical illusions.", 
                 "Uncover the hidden path forward.", "mirage",
                 "Lets play some hangman."),
            Room("The Clockwork Conundrum", "Gears and cogs cover the walls.", 
                 "Solve the mechanical puzzle to set the correct time and open the door.", "15:00",
                 "When did you get off your plane? I forgot."),
            Room("The Alchemist's Laboratory", "Bubbling potions and ancient formulae surround you.", 
                 "Mix the right ingredients to create the key.", "red",
                 "What was the most used color when making your room?"),
            Room("The Musical Maze", "A room that responds to sound.", 
                 "Play the correct melody on various instruments to find your way out.", "si si",
                 "What do I call you?"),
            Room("The Gravity Defying Gallery", "Art pieces float in mid-air.", 
                 "Rearrange them in the correct order to restore normal gravity and proceed.", "mona lisa",
                 "The most famous smile in art history might be the key."),
            Room("The Time-Warped Theatre", "Scenes from different eras play out before you.", 
                 "Oh look, one of them was the one we always watched together before it got taken off Netflix.", "Rick and Morty",
                 "Remember our favorite show?"),
            Room("The Botanical Baffler", "A lush indoor garden with plants from around the world.", 
                 "Find and nurture the rare bloom that holds the key.", "night bloom",
                 "Some flowers only show their true beauty under the moon's glow."),
            Room("The Quantum Quandary", "A room that seems to exist in multiple states at once.", 
                 "Solve quantum puzzles to collapse the wavefunction and reveal the door.", "4d",
                 "What dimension is impossible to reach?"),
            Room("The Memory Vault", "Fragments of your journey flash around you.", 
                 "Recall and arrange your experiences correctly to access the final chamber.", "deja vu",
                 "The feeling of having experienced something before has a French name."),
            Room("The Celebration Chamber", "The room is festively decorated, with a table of serving equipment and a Windex bottle.", 
                 "Reflect on your journey and the mysterious Windex bottle.", "clean",
                 "What did you do with the Windex bottle?")
        ]
        self.current_room = 0

    def play(self):
        print("Welcome to The Grand Escape: Twelve Chambers of Mystery! (just so you know, the names don't make sense so just ignore that)")
        
        while self.current_room < len(self.rooms):
            room = self.rooms[self.current_room]
            print(f"\n--- {room.name} ---")
            print(room.description)
            print(f"Challenge: {room.puzzle}")
            
            start_time = time.time()
            clue_timer = threading.Timer(5, lambda: print(f"Here's a clue: {room.clue}"))
            clue_timer.start()
            
            attempts = 0
            while attempts < 3:
                answer = input("Enter your solution: ")
                if room.solve(answer):
                    print("Correct! The door unlocks, allowing you to proceed.")
                    clue_timer.cancel()
                    self.current_room += 1
                    break
                else:
                    attempts += 1
                    if attempts < 3:
                        print("That's not quite right. Try again!")
            
            if attempts == 3:
                print("You've run out of attempts. Game over!")
                clue_timer.cancel()
                return
        
        self.celebration_chamber()

    def celebration_chamber(self):
        print("\n--- The Celebration Chamber ---")
        print("As you solve the final puzzle and step through the door, you're greeted by an unexpected sight.")
        print("The room is festively decorated, and in the center stands a table with serving equipment and a mysterious Windex bottle.")
        print("\nCongratulations! You've completed 'The Grand Escape: Twelve Chambers of Mystery'.")
        print("But what does this surprising final room mean? Is the Windex bottle a clue to an even greater mystery?")
        
        print("\nAs you ponder this, you notice a small engraving on the Windex bottle:")
        print("'The key to clarity lies within. Your next adventure awaits...'")

if __name__ == "__main__":
    game = EscapeRoom()
    game.play()
