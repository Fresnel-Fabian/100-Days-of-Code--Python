class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
    def __str__(self):
        return f"user_id: {self.user_id}\nuser_name: {self.user_name}"


user1 = User("01", "Fresnel")
user2 = User("02", "Maria")
print(user1)
print(user1.user_id)
print(user2.user_name)
print(user2.user_name)
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
