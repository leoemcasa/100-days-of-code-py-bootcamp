"""Class obj user follow"""
class User:
    """Class user attribute"""
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("creating user...")

    def follow(self, user):
        """Method Follow"""
        self.following += 1
        user.followers += 1

usr1 = User("001", "Angela")
print(usr1.id, usr1.username, usr1.following, usr1.followers)

usr2 = User("000", "Leo")
usr2.id = "002"
print(usr2.id, usr2.username, usr2.following, usr2.followers)
usr1.follow(usr2)
print ("After user 1 follow user2")
print(usr1.id, usr1.username, usr1.following, usr1.followers)
print(usr2.id, usr2.username, usr2.following, usr2.followers)
