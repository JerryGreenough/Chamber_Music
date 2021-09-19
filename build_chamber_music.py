import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, Date, Sequence

from connect_chamber_music import connection_string

import csv
import sys

def main():
    estring = connection_string()

    print("Connecting to ", estring, "...")

    engine = create_engine(estring)

    # Create a Session class.

    Session = sessionmaker(bind=engine)

    # Create a session by instantiating the Session class.

    session = Session()
    
    Base = declarative_base()
    Base.metadata.reflect(engine)
    
    print("Building the Chamber_Music DB ...")
    
    csv_file_name = './data/Composers.csv'
    createComposers(Base, session, engine, csv_file_name)
    
    csv_file_name = './data/Work_Types.csv'
    createWork_Types(Base, session, engine, csv_file_name)
    
    csv_file_name = './data/Works.csv'
    createWorks(Base, session, engine, csv_file_name)
    
    session.close()
    engine.dispose()

    sys.exit(0)


def createComposers(Base, session, engine, csv_file_name):

    # Drop the Composers table if necessary.
    
    if "Composers" in Base.metadata.tables:
        table = Base.metadata.tables.get("Composers")
    
        Base.metadata.drop_all(engine, [table])
        Base.metadata.remove(table)
    
        session.flush()
        session.commit()

    # Create the metadata for the Composers table.
 
    class Composer(Base):
        __tablename__ = 'Composers'
        composer_id = Column(Integer, Sequence('composer_id_seq'), primary_key = True)
        era         = Column(String(50))
        nationality = Column(String(20))
        last_name   = Column(String(50))
        first_name  = Column(String(50))  
        birth_date  = Column(Date)
        death_date  = Column(Date)
                
    Base.metadata.create_all(engine)
   
    session.flush()
    session.commit()
    
    # Create a list of Composer instances.
   
    instances = []
    
    with open(csv_file_name, encoding="utf-8") as csvfile:
    
        reader = csv.reader(csvfile)
        next(reader) # Read the header line.
        for row in reader:
        
            # Note that death_rate should appear as NULL if the composer
            # is not yet dead. If the null string "" were used, MySQL would
            # turn it into the zero date.
        
            cmpsr = Composer(composer_id = int(row[0])+1, \
                             era = row[1], \
                             nationality = row[2], \
                             last_name = row[3], \
                             first_name = row[4], \
                             birth_date = row[5], \
                             death_date = row[6] if row[6]!="" else None)
            instances.append(cmpsr)
     
    # Add the istances to the Composers table and then flush.
    
    session.add_all(instances)
    session.flush()
    session.commit()
    
    
def createWorks(Base, session, engine, csv_file_name):

    # Drop the Composers table if necessary.
    
    if "Works" in Base.metadata.tables:
        table = Base.metadata.tables.get("Works")
    
        Base.metadata.drop_all(engine, [table])
        Base.metadata.remove(table)
    
        session.flush()
        session.commit()

    # Create the metadata for the Composers table.
 
    class Work(Base):
        __tablename__    = 'Works'
        work_id          = Column(Integer, Sequence('work_id_seq'), primary_key = True)
        composer_id      = Column(Integer)
        work_type_id     = Column(Integer)
        title            = Column(String(50))
        key              = Column(String(20))
        opus_no          = Column(String(50))  
        work_no          = Column(Integer)
        name             = Column(String(50))  
        completion_year  = Column(Integer)
                
    Base.metadata.create_all(engine)
   
    session.flush()
    session.commit()
    
    # Create a list of Composer instances.
   
    instances = []
    
    with open(csv_file_name, encoding="utf-8") as csvfile:
    
        reader = csv.reader(csvfile)
        next(reader) # Read the header line.
        for row in reader:
        
            work = Work( composer_id = row[0], \
                         work_type_id = row[1], \
                         title = row[2], \
                         key = row[3] if row[3]!="" else None, \
                         opus_no = row[4] if row[4]!="" else None, \
                         work_no = row[5] if row[5]!="" else None, \
                         name = row[6], \
                         completion_year = row[7] if row[7]!="" else None)
            instances.append(work)
     
    # Add the istances to the Composers table and then flush.
    
    session.add_all(instances)
    session.flush()
    session.commit()
    
    
    
def createWork_Types(Base, session, engine, csv_file_name):

    # Drop the Composers table if necessary.
    
    if "Work_Types" in Base.metadata.tables:
        table = Base.metadata.tables.get("Work_Types")
    
        Base.metadata.drop_all(engine, [table])
        Base.metadata.remove(table)
    
        session.flush()
        session.commit()

    # Create the metadata for the Composers table.
 
    class Work_Type(Base):
        __tablename__ = 'Work_Types'
        work_type_id = Column(Integer, Sequence('work_type_id_seq'), primary_key = True)
        description  = Column(String(50))
                
    Base.metadata.create_all(engine)
   
    session.flush()
    session.commit()
    
    # Create a list of Composer instances.
   
    instances = []
    
    with open(csv_file_name, encoding="utf-8") as csvfile:
    
        reader = csv.reader(csvfile)
        next(reader) # Read the header line.
        for row in reader:
        
            wktype = Work_Type(work_type_id = int(row[0])+1, \
                              description  = row[1])
            instances.append(wktype)
     
    # Add the istances to the Work_Types table and then flush.
    
    session.add_all(instances)
    session.flush()
    session.commit()
    
    
if __name__ == "__main__":
    main()