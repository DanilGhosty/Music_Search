#-*- coding: utf-8 -*-
from sql_interface import DbChinook

class Search_engine():
    def __init__(self, db=DbChinook()):
        self.db = db

    def select_all_tracks(self):
        """Вибрати всі записи про треки та вивести їх"""
        res = self.db.select("""SELECT * FROM tracks;
        """)
    def search_track(self,search_text):
        search_text = '%'+search_text+'%'
        res=self.db.select('''SELECT Name FROM tracks
            WHERE Name LIKE ?
        ''', search_text)
        return res

    def search_track_by_author(self,search_text):
        search_text = '%'+search_text+'%'
        print(search_text)
        res=self.db.select('''SELECT Name FROM tracks
                                WHERE albumId=(SELECT albumId FROM albums WHERE ArtistId=(SELECT ArtistId FROM artists WHERE name LIKE ?))
        ''', search_text)
        print(res)
        return res

    def search_track_by_ganre(self,search_text):
        search_text = '%' + search_text + '%'
        res = self.db.select('''SELECT Name FROM tracks
                                        WHERE genreId=(SELECT genreId FROM genres WHERE name LIKE ?);
                ''', search_text)
        return res


    def seearch_album(self,text):
        res=self.db.select("""SELECT title FROM albums WHERE albumId =(SELECT albumId FROM tracks WHERE name = ?)
        """,text)
        return res[0]

    def search_artist(self,text):
        res=self.db.select("""SELECT name FROM artists WHERE artistId=(SELECT artistId FROM albums WHERE albumId=(SELECT albumId FROM tracks WHERE name = ?));
        """,text)
        return res[0]

    def search_long(self,text):
        res=self.db.select("""SELECT milliseconds FROM tracks WHERE name=?
        """,text)
        return res






if __name__=="__main__":
   from sql_interface import DbChinook
   db = DbChinook()
   engine = Search_engine(db)
   engine.select_all_tracks()

