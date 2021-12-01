from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository

# Create and Save Album
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    album.id =id
    return album

# Delete all Albums
def delete_all():
    sql = "Delete FROM albums"
    run_sql(sql)

# Find Album by their ID
def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
        return album

# List All Albums
def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist,row['id'])
        albums.append(album)
    return albums

# List all the albums by an artist
def select_all_albums_by_artist(artist):
    albums = []
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [artist.id]
    results = run_sql(sql,values)
    for row in results:
        album = Album(row['title'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums

# Edit Album
def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s,%s,%s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql,values)

# Delete Album
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql,values)