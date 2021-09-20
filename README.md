# Chamber_Music
<strong>Purpose:</strong> Creation and querying of a database of chamber music using MySQL and SQLAlchemy.

The purpose of this project is to provide a simple demonstration of how the ORM functionality provided by Flask SQLAlchemy can be used to create and query a relational database. Once constructed, the database contains references to works of "chamber music", a genre of classical music that requires a samll number of performers - typcially 2-10 musicians. A chamber music work involves a variety of instruments, the most popular form of which is the "String Quartet" which requires 4 performers that invariably consist of: a viola player, a cello player and two violin players. Other forms of chamber music exist, the most popular of which are listed in one of the database tables ("Work_Types").

<p align="center">
    <img src="https://raw.githubusercontent.com/JerryGreenough/Chamber_Music/master/images/schubert_piano_trio.JPG" width="782" height="444">  
</p>

<p align="center">
    <strong><small>The introductory bars of Schubert's Piano Trio No. 1 in B flat major</small></strong>
</p>

The enitre repertoire of chamber music contains thousands of works, only a few of which are currently represented by the SQL scripts presented in this project. However, it is hoped that at a later date a more complete representation of the repertoire will be made available. Every effort has been made to ensure accuracy of the database content - however the purpose of the project is not to provide a tool for musical research, but rather to demonstrate SQLAlchemy as a means to perform SQL join and query operations that potentially answer questions such as:

- How many string quartets did Franz Joseph Haydn write ?
- List all the piano quartets composed during the romantic era.
- How many chamber works were composed after 1910, and who composed them ?


# Database Structure

When built, the Chamber_music database contains three simple tables:

* Composers - contains a list of composers along with pertinent fields such as:
    * first name(s)
    * last name
    * birth year
    * death year
    * nationality
    * era (e.g. "Romantic", "Classical", "20th Century")
* Work_Types - contains a list of possible chamber work types, each of which has a field:
    * description (e.g. "Piano Trio", "Violin Sonata", "Nonet"
* Works - contains a list of chamber music works with relecant feaures plus two foreign keys that link to the Composers and Work_Types tables.
    * composer_id (foreign key pointing to the primary key in the Composers table)
    * work_type_id (foreign key pointing to the primary key in the Work_Types table)
    * title
    * key - the musical key in which the work is deemed to have been written (not always present)
    * opus_no
    * work_no
    * name - sometimes the work is given a nick-name that represents the character of the work
    * completion_year

# Project Directories

* credential - holds a single python script to return the useranme, password and end-point for the database connection
* data - holds the .csv files that contain the data from which the database is built
* images - holds the image of musical text from the previous section (see above)
* sql - contains the SQL scripts that can be used to build the database without using SQLAlchemy

# Database Creation

A simple, free-of-charge localhost database can be created using a visual database design tool such as MySQL Workbench or pgAdmin (for postgreSQL) to name but two. The following YouTube tutorial from Mosh Hamedani contains particaularly clear instructions on how to do this:

http://www.youtube.com/watch?v=7S_tz1z_5bA

An alternative approach would be to set up a database using the RDS service from Amazon Web Services. Neal Davis' introduction to AWS provides easily digestible instructions on how to create a relational database in the cloud.

http://www.youtube.com/watch?v=ulprqHHWlng


## Prerequisites

The following libraries should be installed:

* SQLAlchemy

# Acknowledgements

The Customers table was largely constructed from data scraped from the following website:
www.famouscomposers.net/list


