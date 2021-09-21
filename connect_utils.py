from credentials.credentials import get_credentials

def connection_string():

    user_name, pass_word, end_point = get_credentials()
  
    port = '3306'
  
    dbname = 'chamber_music'

    estring = 'mysql+pymysql://' \
            + user_name + ':' \
            + pass_word + '@' \
            + end_point + ":" \
            + port \
            + '/' + dbname

    return estring