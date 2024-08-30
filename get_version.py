
import toml
 
with open('pyproject.toml', 'r') as f:
    config = toml.load(f)
 
# Access values from the config
print(config['server']['host'])
print(config['server']['port'])
print(config['database']['username'])