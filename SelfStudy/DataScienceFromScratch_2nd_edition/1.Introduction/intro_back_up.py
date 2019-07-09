# import module
from collections import defaultdict

# make dictionary setting
user_ids_by_interest = defaultdict(list) # dictionary such that the key will be mapped to a list : defaultdict(list)

for user_id,interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
# user_ids mapped to a list of his/her interests
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
print(user_ids_by_interest)
interests_by_user_id

#user_ids_by_interest
#interests_by_user_id
def most_common_interests_with(user):
    
    sharer_freq = []
    
    for i in interests_by_user_id[user]:
          sharer_freq.extend(user_ids_by_interest[i])
    
    sharer_freq = [k for k in sharer_freq if not k == user]
    return Counter(sharer_freq)


# Test the usage
print("for user {0}, recommend {1}.".format(2, most_common_interests_with(2).most_common()[0][0]))


# textbook implementation : compare and learn

def most_common_interests_with(user):
    return Counter(
    interested_user_id
    for interest in interests_by_user_id[user['id']]
    for interested_user_id in user_ids_by_interest[interest]
    if interested_user_id != user['id']
    )