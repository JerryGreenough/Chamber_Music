# Chamber_Music
<strong>Purpose:</strong> Creation and querying of a database of chamber music using MySQL and SQLAlchemy.

The purpose of this project is to provide a simple demonstration of how the ORM functionality provided by Flask SQLAlchemy can be used to create and query a relational database. Once constructed, the database contains references to works of "chamber music", a genre of classical music that requires a samll number of performers - typcially 2-10 musicians. A chamber music work involves a variety of instruments, the most popular form of which is the "String Quartet" which requires 4 performers that invariably consist of: a viola player, a cello player and two violin players. Other forms of chamber music exist, the most popular of which are listed in one of the database tables ("Work_Types").

<p align="center">
    <img src="https://raw.githubusercontent.com/JerryGreenough/Chamber_Music/master/images/schubert_piano_trio.JPG" width="782" height="444">  
</p>

<p align="center">
    <strong><small>The introductory bars of Schubert's Piano Trio No. 1 in B flat major</small></strong>
</p>

The enitre repertoire of chamber music contains thousands of works, only a few of which are currently represented by the SQL scripts presented in this project. However, it is hoped that at a later date a more complete representation of the repertoire will be made available. Every effort has been made to ensure accuracy of the database content - however the purpose of the project is not to provide a tool for musical research, but rather as means to demonstrate SQLAlchemy as a means to perform SQL join and query operations that potentially answer questions such as:

- How many string quartets did Franz Joseph Haydn write ?
- List all the piano quartets composed during the romantic era.
- How many chamber works were composed after 1910, and who composed them ?


# Database Structure

* data - holds the .csv files that contain the data from which the database is built
* images - holds the image you see above

# Project Directories

More to follow.

# Acknowledgements

The Customers table was largely constructed from data scraped from the following website:
www.famouscomposers.net/list


