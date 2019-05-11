import os
import configparser
import io
configfile_name = "config.ini"

# Check if there is already a configurtion file
if not os.path.isfile(configfile_name):
    # Create the configuration file as it doesn't exist yet
    cfgfile = open(configfile_name, 'w')

    # Add content to the file
    Config = configparser.ConfigParser()
    Config['MYSQL'] = {'host': 'dapproject.db.10836946.188.hostedresource.net',
                        'user': 'dapproject',
                        'passwd': 'ptsmProject123!',
                        'database': 'dapproject',
                        'auth_plugin': 'mysql_native_password'}

    Config['TWITTER'] = {'consumer_key': '49yh2KepopldjN9rf2a20isGj',
                        'consumer_secret': 'Ryz1caenzOTPVod7RVYUOhFS8nMQHWAHw791EF3vtwyd17ChQY',
                        'access_token': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                        'access_token_secret': 'XXXXXXXXXXXXXXXXXXXXXXXXX'}
    
    Config['IBMWATSON'] = {'iam_apikey': 'dnby4_Q9Wx54inSunQ-6xdO2CNIfsVhlatzopCIOsRbR',
                        'url': 'https://gateway-wdc.watsonplatform.net/natural-language-understanding/api',
                        'version': '2018-12-19'}

    Config['OTHER'] = {'use_anonymous':True}            
    Config.write(cfgfile)
    cfgfile.close()