from globals import spy, friends
from spy_details import Spy


def add_friend():
    # Adding a new friend
    new_friend = Spy('', '', 0, 0)
    new_friend.name = input("Add your friend : Name : ")
    new_friend.salutation = input("Are they Mr. or Mrs. : ")
    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(input("Age: "))
    new_friend.rating = float(input("Spy Rating: "))

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print("Friend Added \n")

    else:
        print("Sorry!! invalid entry ")

    return len(friends)
