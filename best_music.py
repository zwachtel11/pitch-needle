import requests
import sqlite3
from sqlite3 import Error
from bs4 import BeautifulSoup

""" create a database connection to a SQLite database """
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

class Database:
    def __init__(self):
        self.connection = create_connection("test5.db")
        self.cursor = self.connection.cursor()

    def create_table(self, create_sql):
        try:
            c = self.cursor
            c.execute(create_sql)
            self.connection.commit()
        except Error as e:
            print(e)

    def insert(self, query, data):
        try:
            self.cursor.execute(query, data)
            self.connection.commit()
        except Error as e:
            print(e)
            self.connection.rollback()

def get_itunes(record):
    link = 'https://itunes.apple.com/search?term='
    for word in record['artist'].split(" "):
        link += word + "+"
    for word in record['title'].split(" "):
        link += word + "+"
    link = link[:-1]

    link += '&entity=album&limit=1'
    test = requests.get(link)
    if test:
        test = test.json()
        if len(test['results']) > 0:
            cover = test['results'][0]['artworkUrl100'][:-13]
            cover += '/512x512bb.jpg'
            date = test['results'][0]['releaseDate']
            genre = test['results'][0]['primaryGenreName']
            link = test['results'][0]['collectionViewUrl']   
            return cover, date, genre, link
    return '', '', '', ''
    

def theneedledrop(records):

    page = requests.get('http://www.theneedledrop.com/loved-list/')
    soup = BeautifulSoup(page.text, 'html.parser')
    artist_name_list = soup.find(class_='entry-content')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
        fields = artist_name.contents[0].split(" - ")
        record = {}
        record['artist'] = fields[0]
        record['title'] = fields[1]
        record['provider'] = 'The Needle Drop'

        record['cover'], record['date'], record['genre'], record['link'] = get_itunes(record)

        records.append(record)
    return records

def pitchfork(records):

    for i in xrange(5):
        if i is 0:
            continue
        url = 'https://pitchfork.com/reviews/best/albums/?page=' + str(i)
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')

        artist_name_list = soup.find(class_='fragment-list')
        album_titles = artist_name_list.find_all('h2')
        album_artists = artist_name_list.find_all('ul', class_='artist-list review__title-artist')

        for artist_name, album_name in zip(album_artists, album_titles):
            record = {}
            record['artist'] = artist_name.find('li').contents[0]
            record['title'] = album_name.contents[0]
            record['provider'] = 'Pitchfork'
            record['cover'], record['date'], record['genre'], record['link']  = get_itunes(record)
            records.append(record)

    return records

if __name__ == '__main__':
    records = []
    records = theneedledrop(records)

    records = pitchfork(records)

    db = Database()
    sql_create_records_table = """ CREATE TABLE IF NOT EXISTS records (
                                        id integer PRIMARY KEY,
                                        album text NOT NULL,
                                        artist text,
                                        provider text,
                                        cover text,
                                        genre text,
                                        releasedate DATETIME,
                                        applelink text
                                    ); """

    db.create_table(sql_create_records_table)


    sql = ''' INSERT INTO records(album,artist,provider, cover, genre, releasedate, applelink) VALUES($title,$artist,$provider, $cover, $genre, $releasedate, $applelink);'''

    for record in records:
        try:
            data = (str(record['title']),
                    str(record['artist']), 
                    str(record['provider']), 
                    str(record['cover']), 
                    str(record['genre']),
                    str(record['date']),
                    str(record['link']))
        except:
            continue
        db.insert(sql, {'title': str(record['title']), 
                        'artist': str(record['artist']), 
                        'provider': str(record['provider']),
                        'cover': str(record['cover']),
                        'genre': str(record['genre']),
                        'releasedate': str(record['date']),
                        'applelink': str(record['link'])
                        })

    
