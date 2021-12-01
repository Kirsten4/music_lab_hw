from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository


# Create and Save Artist
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql,values)
    id = results[0]['id']
    artist.id = id
    return artist

# Delete all Artists
def delete_all():
    sql = "Delete FROM artists"
    run_sql(sql)

# Find Artist by their ID
def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    if result is not None:
        artist = Artist(result['name'],result['id'])
    return artist

# List All Artists
def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

# Edit Artist
def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql,values)

# Delete Artist
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql,values)