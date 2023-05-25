def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    room = list()
    # for name in names:
    #     room.append(f"Hello, {name}! You'll be assigned to room {names.index(name) +1}!" )
    for index, name in enumerate(names):
        room.append(f"Hello, {name}! You'll be assigned to room {index +1}!" )
    return room

def printer(names):
    [print(item) for item in batch_badge_creator(names)]
    [print(item) for item in assign_rooms(names)]
