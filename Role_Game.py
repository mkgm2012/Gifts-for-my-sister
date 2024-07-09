def start_game():
    print("Welcome to the Americana Hotel!")
    print("You are working as a hostess, server, and housekeeper.")
    print("Your decisions will influence the plot and guest experiences.")
    main_menu()

def main_menu():
    print("\nMain Menu:")
    print("1. Hostess")
    print("2. Server")
    print("3. Housekeeper")
    print("4. Quit")
    choice = input("Choose your role (1-4): ")

    if choice == '1':
        hostess_role()
    elif choice == '2':
        server_role()
    elif choice == '3':
        housekeeper_role()
    elif choice == '4':
        print("Thank you for playing!")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def hostess_role():
    scenarios = [
        ("A family arrives at the hotel.", 
         "1. Greet them warmly and offer a welcome drink.", 
         "2. Ignore them and continue checking your phone.",
         "3. Greet them but make a mistake with their reservation.",
         "The family appreciates your hospitality and leaves a positive review.",
         "The family feels unwelcome and leaves a negative review.",
         "The family is frustrated but accepts your apology after the mistake is corrected."),
        ("A VIP guest arrives unexpectedly without a reservation.", 
         "1. Try to find a room for the VIP guest.", 
         "2. Politely inform the guest that the hotel is fully booked.",
         "3. Suggest a nearby hotel for accommodation.",
         "The VIP guest is impressed by your effort and praises your service.",
         "The VIP guest is disappointed and decides to leave.",
         "The VIP guest appreciates your suggestion and thanks you for your help."),
        ("An elderly couple needs assistance with their luggage.", 
         "1. Help them with their luggage.", 
         "2. Ignore them and let them struggle.",
         "3. Call a bellboy to assist them.",
         "The couple is grateful and compliments your helpfulness.",
         "The couple is upset and complains about the poor service.",
         "The couple is pleased with the bellboy's assistance and leaves a positive review."),
        ("A guest asks for recommendations on local attractions.", 
         "1. Provide detailed and enthusiastic recommendations.", 
         "2. Brush them off with a vague answer.",
         "3. Give them a brochure with information.",
         "The guest appreciates your help and enjoys their stay more.",
         "The guest feels neglected and leaves an average review.",
         "The guest finds the brochure helpful and leaves a positive review."),
        ("A guest checks in late at night and looks exhausted.", 
         "1. Offer them a complimentary drink and quick check-in.", 
         "2. Take your time and follow standard procedures.",
         "3. Offer them an upgrade to a better room.",
         "The guest is thankful and leaves a positive review.",
         "The guest is frustrated and leaves a negative review.",
         "The guest is delighted with the upgrade and leaves an excellent review.")
    ]
    process_scenarios(scenarios, "hostess")

def server_role():
    scenarios = [
        ("A guest complains about their meal.", 
         "1. Apologize and offer to replace the meal.", 
         "2. Tell them there’s nothing wrong with the meal and refuse to replace it.",
         "3. Offer them a complimentary dessert.",
         "The guest is satisfied with the new meal and leaves a good tip.",
         "The guest is unhappy and leaves a bad review.",
         "The guest appreciates the gesture and leaves a positive review."),
        ("A group of guests arrives just before closing time.", 
         "1. Serve them quickly and politely.", 
         "2. Tell them the kitchen is closed and refuse service.",
         "3. Offer to serve them drinks but no food.",
         "The guests appreciate your service and leave a generous tip.",
         "The guests are disappointed and leave a negative review.",
         "The guests enjoy the drinks and leave a decent tip."),
        ("A child spills their drink all over the table.", 
         "1. Clean it up quickly and bring a new drink.", 
         "2. Ignore it and let the parents handle it.",
         "3. Apologize and offer a free replacement.",
         "The parents are grateful and leave a good tip.",
         "The parents are upset and complain about the service.",
         "The parents appreciate the free replacement and leave a positive review."),
        ("A guest has dietary restrictions and needs a special menu.", 
         "1. Accommodate their needs and suggest suitable dishes.", 
         "2. Tell them to choose from the regular menu.",
         "3. Offer to speak with the chef for special preparations.",
         "The guest appreciates your help and leaves a positive review.",
         "The guest feels unwelcome and leaves a negative review.",
         "The guest is impressed by the effort and leaves an excellent review."),
        ("A couple celebrates their anniversary at the restaurant.", 
         "1. Offer them a complimentary dessert.", 
         "2. Ignore their celebration.",
         "3. Congratulate them and offer a free drink.",
         "The couple is delighted and leaves a great review.",
         "The couple feels unappreciated and leaves an average review.",
         "The couple is happy with the gesture and leaves a positive review.")
    ]
    process_scenarios(scenarios, "server")

def housekeeper_role():
    scenarios = [
        ("You find a wallet in one of the rooms.", 
         "1. Turn it into lost and found.", 
         "2. Keep it for yourself.",
         "3. Try to contact the guest directly to return it.",
         "The guest is grateful and leaves a positive review.",
         "The guest reports the missing wallet, and you get in trouble.",
         "The guest is very grateful and leaves an excellent review."),
        ("You notice a guest left their room in a mess.", 
         "1. Clean the room thoroughly despite the extra work.", 
         "2. Do a quick clean and move on to the next room.",
         "3. Leave a note asking the guest to be tidier.",
         "The guest is pleased with the clean room and leaves a big tip.",
         "The guest is disappointed with the cleanliness and complains to management.",
         "The guest is slightly annoyed by the note but leaves a neutral review."),
        ("A guest asks for extra towels and toiletries.", 
         "1. Bring them extra towels and toiletries promptly.", 
         "2. Tell them to use what they have.",
         "3. Bring them only extra towels but no toiletries.",
         "The guest is happy with your service and leaves a positive review.",
         "The guest is unhappy and leaves a negative review.",
         "The guest appreciates the extra towels and leaves a neutral review."),
        ("You find a broken item in one of the rooms.", 
         "1. Report it to maintenance immediately.", 
         "2. Ignore it and hope no one notices.",
         "3. Try to fix it yourself.",
         "The item is fixed quickly, and the guest is satisfied.",
         "The guest discovers it and complains about the broken item.",
         "The item is partially fixed, and the guest leaves a neutral review."),
        ("A guest leaves a generous tip for you in their room.", 
         "1. Take the tip and thank the guest if you see them.", 
         "2. Ignore the tip, thinking it might be a mistake.",
         "3. Report the tip to your manager.",
         "The guest is glad you took the tip and appreciates your service.",
         "The guest is confused why the tip wasn't taken and feels awkward.",
         "The manager confirms the tip is for you, and the guest is pleased.")
    ]
    process_scenarios(scenarios, "housekeeper")

def process_scenarios(scenarios, role):
    for scenario in scenarios:
        print(f"\nYou are the {role}. {scenario[0]}")
        print(scenario[1])
        print(scenario[2])
        print(scenario[3])
        choice = input("What do you do? (1-3): ")

        if choice == '1':
            print(scenario[4])
        elif choice == '2':
            print(scenario[5])
        elif choice == '3':
            print(scenario[6])
        else:
            print("Invalid choice. Please try again.")
            process_scenarios([scenario], role)

    main_menu()

start_game()
