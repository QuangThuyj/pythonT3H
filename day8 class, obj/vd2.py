class Person:
    def __init__(self, name):
        self.name = name
        self.friendList = []
        self.friendRequestList = []

    def __repr__(self):
        return self.name

    def senRequest(self, person):
        person.friendRequestList.append(self)

    def acceptRequest(self, person):
        if person in self.friendRequestList:
            self.friendList.append(person)
            person.friendList.append(self)
            self.friendRequestList.remove(person)

    def isFriendWith(self, person):
        return self in person.friendList

    def isFriendOfFriendWith(self, person):
        for p in self.friendList:
            if p.isFriendWith(person):
                return True
            return False

    def getCommonFriends(self, person):
        return [p for p in self.friendList if p.isFriendWith(person)]
        # lst = []
        # for p in self.friendList:
        #     if p.isFriendWith(person):
        #         lst.append(p)
        # return lst

p1 = Person('A')
p2 = Person('B')
p3 = Person('C')

p1.senRequest(p2)
p2.acceptRequest(p1)

p2.senRequest(p3)
p3.acceptRequest(p2)

print(p1.friendList)
print(p2.friendList)
print(p3.friendList)

print(p1.isFriendWith(p2))
print(p1.isFriendWith(p3))

print(p1.getCommonFriends(p3))
