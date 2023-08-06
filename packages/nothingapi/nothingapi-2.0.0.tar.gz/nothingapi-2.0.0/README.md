# NothingAPI - The Official Python API Wrapper for the Nothing Currency!
## Basic Syntax
### Installing the API using pip:
```
pip install nothingapi
```

### Fetching a User's object and printing it's balance:
```
import nothingapi as api
user = api.get_user(user_id)
print(user.balance)
```

### Fetching a Guild's object and printing it's total value:
```
import nothingapi as api
user = api.get_guild(guild_id)
print(guild.total_value)
```