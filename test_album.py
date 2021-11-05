"""Incomplete tests for Album class."""

from album import Album


def run_tests():
    """Test Album class."""

    # Test empty album (defaults)
    print("Test empty album:")
    empty_album = Album()
    print(empty_album)
    assert empty_album.title == ""
    assert empty_album.artist == ""
    assert empty_album.year == 0
    assert not empty_album.is_completed

    # Test initial-value album
    print("Test initial value album:")
    new_album = Album("Unleashed", "Skillet", 2016, False)
    # TODO: Write tests to show this initialisation works

    # Test mark_completed()
    # TODO: Write tests to show the mark_completed() method works

    # TODO: Add tests for any untested methods (and more tests as needed)


run_tests()
