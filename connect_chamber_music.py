from credentials.credentials import get_credentials

def connection_string():

    user_name, pass_word, end_point = get_credentials()

    # Connection string for a MySQL version of the chamber music database.
    #unm = 'admin'
    #pwd = 'wankbuster44at'
    port = '3306'
    #ept = 'jdg1-pg.cthxmreqvlpk.us-east-1.rds.amazonaws.com' + ":" + port

    dbname = 'Chamber_Music'

    estring = 'mysql+pymysql://' \
            + user_name + ':' \
            + pass_word + '@' \
            + end_point + ":" \
            + port + '/' + dbname

    return estring