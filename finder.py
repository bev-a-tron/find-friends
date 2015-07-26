from birdy.twitter import UserClient
import secrets as s

client = UserClient(s.API_KEY,
                    s.API_SECRET,
                    s.ACCESS_TOKEN,
                    s.ACCESS_TOKEN_SECRET)

resource = client.api.users.show
r1 = resource.get(user_id='20257992')
print(r1)

resource = client.api.friends.ids
r = resource.get(user_id='20257992')
ids = r.data['ids']

print(r)
