import configparser
import io

config = configparser.ConfigParser()
config.read('config.ini')
print(config['TWITTER']['consumer_key'])