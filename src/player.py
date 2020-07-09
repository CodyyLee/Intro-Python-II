# Write a class to hold player information, e.g. what room they are in
# currently.

class player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items

    def move(self, room):
        self.room = room

    def get(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)