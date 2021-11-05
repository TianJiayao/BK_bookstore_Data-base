"""Incomplete tests for AlbumCollection class."""

from album import Album
from albumcollection import AlbumCollection

ALBUMS_FILE = 'albums.csv'


def run_tests():
    """Test empty AlbumCollection."""
    print("Test empty album collection")
    album_collection = AlbumCollection()
    assert not album_collection.albums  # An empty list is considered False
    print(album_collection)

    # Test loading albums
    print("Test loading albums")
    album_collection.load_albums(ALBUMS_FILE)
    assert album_collection.albums  # assuming CSV file is not empty, list will not be considered False
    print(album_collection)

    # Test sorting albums
    print("Test sorting - artist")
    album_collection.sort()

    # Test adding a new Album
    print("Test adding a new Album")
    album_collection.add_album(Album("How Can It Be", "Lauren Daigle", 2015, False))

    # TODO: Complete these tests and add any more as needed to test all methods of your class


run_tests()
