import pdb
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Biffy Clyro")
artist_repository.save(artist_1)

artist_2 = Artist("Queen")
artist_repository.save(artist_2)

album_1 = Album("Blackened Sky","Alternative Rock",artist_1)
album_repository.save(album_1)

album_2 = Album("A Night At The Opera", "Glam Rock", artist_2)
album_repository.save(album_2)

album_3 = Album("Only Revolutions", "Rock", artist_1)
album_repository.save(album_3)

print(artist_repository.select(artist_2.id).name)

print(album_repository.select(album_3.id).title)

album_3.genre = "Pop"
album_repository.update(album_3)

artist_1.name = "Clyro Biffy" 
artist_repository.update(artist_1)

album_repository.delete(album_2.id)

artist_repository.delete(artist_2.id)

artists = artist_repository.select_all()
albums = album_repository.select_all()

for artist in artists:
    print(artist.__dict__)

for album in albums:
    print(album.__dict__)

pdb.set_trace()