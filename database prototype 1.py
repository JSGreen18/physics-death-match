import sqlite3

def newUser():
    #user choose unique name 
    cont = True
    while cont == True:
        user = input('choose username ')
        score = int(input('what score? '))
        # tries to add record with that username but will cause an error if the username is taken
        try:
            # creates record for new user
            conn.execute('''INSERT INTO highscore(Username,score)
                        VALUES(?,?)''',(user,score))
            conn.commit()

            cont = False

        # if error happens then code will say username is not valid instead and let user try again
        except:
            print('username is not valid')


def existingUser():
    # user gives their name
    cont = True
    while cont == True:
        try:
            user = input('What is your username? ')

            # will get the players score for that game from player class
            # but for this prototype made up test data will be used by input

            score = int(input('What Score? '))

            #get users previous highscore 
            cursor.execute('SELECT score FROM highscore WHERE Username=?',(user,))
            userHighscore = cursor.fetchall()
            #print(userHighscore[0])
            userHighscore = int(userHighscore[0][0])

            # see if user beat thier previous highscore 
            if score > userHighscore:
                userHighscore = score

            # update user's record with new highscore 
            conn.execute('UPDATE highscore SET score=? WHERE Username=?',(userHighscore, user))
            conn.commit()

            # break loop
            cont = False

        except:
            print('Invalid Username')


def outputDatabse():
    # gets all records from the database in order
    cursor.execute('SELECT * from highscore ORDER BY score DESC')
    scoresList = cursor.fetchall()

    # prints each record in turn 
    for record in scoresList:
        print('Score: {0}, {1}'.format(record[0], record[1]))


#create highscore databse
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute(''' create table if not exists highscore
        (Username text,
        score int,
        primary key(Username))''')
    

# check if player has played before 
new = input('new player? ')
if new == 'yes':
    # run function for new user
    newUser()

elif new == 'no':
    # run function for existing user
    existingUser()

# used to delete the table so it can be reset if needed when testing 
elif new == 'reset':
    cursor.execute('DROP TABLE IF EXISTS highscore') 
    quit()

outputDatabse()

# close connection to database
conn.close()            

        
