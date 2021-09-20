from credentials.credentials import get_credentials

def connection_string():

    user_name, pass_word, end_point = get_credentials()

    # Connection string for a MySQL version of the chamber music database.
    port = '3306'

    dbname = 'Chamber_Music'

    estring = 'mysql+pymysql://' \
            + user_name + ':' \
            + pass_word + '@' \
            + end_point + ":" \
            + port + '/' + dbname

    return estring