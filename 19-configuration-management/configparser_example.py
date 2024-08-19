import configparser

# create a ConfigParser object
config = configparser.ConfigParser()

# read configuration from a file
config.read('config.ini')

# access a value
database_host = config.get('Database', 'host')
database_port = config.getint('Database', 'port')

print(f"Database Host: {database_host}")
print(f"Database Port: {database_port}")

# write to a configuration file
config['Database']['host'] = 'localhost'
config['Database']['port'] = '5432'

with open('config.ini', 'w') as configfile:
    config.write(configfile)
