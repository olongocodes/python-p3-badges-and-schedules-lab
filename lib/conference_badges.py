def badge_maker(name):
    name = "Guido van Rossum"
    return (f"Hello, my name is {name}.")
    return None

def batch_badge_creator(names):
    messages = [] 
    for name in names:
        messages.append(f"Hello, my name is {name}.")
    return messages
    return None

def assign_rooms(names):
    rooms = []
    for i, name in enumerate(names, start=1):
        rooms.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return rooms
    return None

def printer(names):
    badges = batch_badge_creator(names)
    for badge in badges:
        print(badge)
    

    room_assignments = assign_rooms(names)
    for assignment in room_assignments:
        print(assignment)
