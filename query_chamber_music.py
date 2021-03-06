import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from sqlalchemy import Column, Integer, String, Date, Sequence
from sqlalchemy_utils import database_exists, create_database

from connect_chamber_music import connection_string
from utils_chamber_music import classical_work_string

import csv
import sys

def main():
    estring = connection_string()

    print("Connecting to ", estring, "...")
    
    # Create an engine object - seomthing containing all the data needed to
    # connect to the database.

    engine = create_engine(estring)
    
    if not database_exists(engine.url):
        print("The chamber_music DB does not exist on the endpoint.")
        sys.exit(1)

    # Create a Session class.

    Session = sessionmaker(bind=engine)

    # Create a session by instantiating the Session class. This will connect
    # us to the database in accordance with the parameters of the engine.

    session = Session()
    
    # Create the ORM base class, which will result in an AutomapBase class. This class 
    # enables the generation of a quick and easy mapping from an existing SQL database.
    
    Base = automap_base()
    
    # Reflect the database's schema and produce mappings of the database tables 
    # via the previously defined engine. The classes that are produced by prepare()
    # load information about the corresponding table's schema into a dedicated
    # class (reflection).
    
    Base.prepare(engine, reflect = True)
    
    # These are the classes that represent the mapped database tables. 
    # The assignements produce an easy-to-read alias for each class.
     
    Composers   = Base.classes.composers
    Works       = Base.classes.works
    Work_Types  = Base.classes.work_types
    
    # Some queries ....
    
 
    # QUERY: 
    print("\nList all septets ...\n")
    
    stmt = select(Works, Composers, Work_Types) \
            .join(Composers, Composers.composer_id == Works.composer_id) \
            .join(Work_Types, Work_Types.work_type_id == Works.work_type_id) \
            .where(Work_Types.description=='Septet')

    res = session.execute(stmt)

    for rr in res.fetchall():
        print(classical_work_string(rr)) 
                           
    # QUERY: 
    print("\nList all string quintets using raw SQL ...\n")
    
    selstr = 'SELECT \
                Composers.first_name, \
                Composers.last_name, \
                Works.title,\
                Works.opus_no,\
                Works.work_no \
                FROM Works \
                JOIN Work_Types ON Work_Types.work_type_id = Works.work_type_id \
                JOIN Composers ON Composers.composer_id = Works.composer_id \
                WHERE Work_Types.description = "String Quintet"' 

    res = session.execute(selstr)

    for rr in res.fetchall():
        print(rr)
    
    # QUERY: 
    print("\nList all piano quartets by composers from the romantic era and ordered by the composer's last name ...\n")   
        
    stmt = select(Works, Composers, Work_Types) \
            .join(Composers, Composers.composer_id == Works.composer_id) \
            .join(Work_Types, Work_Types.work_type_id == Works.work_type_id) \
            .where(Work_Types.description=='Piano Quartet') \
            .where(Composers.era=='Romantic') \
            .order_by(Composers.last_name)   
            
    res = session.execute(stmt)

    for rr in res.fetchall(): 
        print(classical_work_string(rr))
    
    # QUERY:     
    print("\nList all quartets by composers from the romantic era and ordered by the composer's last name ...\n")   
        
    stmt = select(Works, Composers, Work_Types) \
            .join(Composers, Composers.composer_id == Works.composer_id) \
            .join(Work_Types, Work_Types.work_type_id == Works.work_type_id) \
            .filter(Work_Types.description.op('regexp')('Quartet')) \
            .where(Composers.era=='Romantic') \
            .order_by(Composers.last_name)   
            
    res = session.execute(stmt)

    for rr in res.fetchall(): 
        print(classical_work_string(rr))
        
        
    # QUERY:     
    print("\nCount the works (for each work type) composed during the Classical era ...\n")   
    
    from sqlalchemy import func
        
    stmt = select(Works, Composers, Work_Types, func.count(Works.work_type_id)) \
            .join(Composers, Composers.composer_id == Works.composer_id) \
            .join(Work_Types, Work_Types.work_type_id == Works.work_type_id) \
            .order_by(Work_Types.work_type_id, Composers.last_name, Works.title) \
            .group_by(Work_Types.work_type_id) \
            .where(Composers.era=='Classical')
            
    res = session.execute(stmt)
    
    for rr in res.fetchall(): 
        print(rr.work_types.description, rr.count)
        
        
    # QUERY:     
    print("\nList the works completed by composers from the Classical era on or after 1780 ...\n")  
            
    stmt = select(Works, Composers, Work_Types) \
            .join(Composers, Composers.composer_id == Works.composer_id) \
            .join(Work_Types, Work_Types.work_type_id == Works.work_type_id) \
            .where(Composers.era=='Classical') \
            .where(Works.completion_year >= 1780)
            
    res = session.execute(stmt)

    for rr in res.fetchall(): 
        print(classical_work_string(rr))
 
    # QUERY:     
    print("\nList the 20th century works completed during or after 1910 ...\n")   
  
    stmt = select(Works, Composers, Work_Types) \
            .join(Composers, Composers.composer_id == Works.composer_id) \
            .join(Work_Types, Work_Types.work_type_id == Works.work_type_id) \
            .where(Composers.era=='20th Century') \
            .where(Works.completion_year >= 1910)
            
    res = session.execute(stmt)

    for rr in res.fetchall(): 
        print(classical_work_string(rr))
        
    session.close()
    engine.dispose()

    sys.exit(0)


    
if __name__ == "__main__":
    main()
    
