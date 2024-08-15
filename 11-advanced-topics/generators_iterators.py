from datetime import datetime, timedelta

class UserRecords:
    def __init__(self):
        self.users = [
            {"name": "Alice", "last_login": datetime.now() - timedelta(days=500)},
            {"name": "Bob", "last_login": datetime.now() - timedelta(days=800)},
            {"name": "Charlie", "last_login": datetime.now() - timedelta(days=100)},
            {"name": "David", "last_login": datetime.now() - timedelta(days=1200)},
        ]
        self.index = 0  #  keep track of the current position in the iteration

    def __iter__(self):
        # resetting index when a new iterator is created
        self.index = 0
        return self

    def __next__(self):
        #  if there are more items to return
        if self.index < len(self.users):
            user = self.users[self.index]
            self.index += 1
            return user
        else:
            # No more items, stop the iteration
            raise StopIteration

class InactiveUserFilter:
    def __init__(self, user_records, threshold_days):
        self.user_records = user_records
        self.threshold_date = datetime.now() - timedelta(days=threshold_days)

    def __iter__(self):
        # return an iterator that filters inactive users
        return self

    def __next__(self):
        while True:
            try:
                user = next(self.user_records)
                if user["last_login"] < self.threshold_date:
                    return user
            except StopIteration:
                # no more items, stop the iteration
                raise StopIteration

user_records = UserRecords()
inactive_user_filter = InactiveUserFilter(iter(user_records), threshold_days=365)

print("Inactive Users:")
for user in inactive_user_filter:
    print(f"Name: {user['name']}, Last Login: {user['last_login']}")
