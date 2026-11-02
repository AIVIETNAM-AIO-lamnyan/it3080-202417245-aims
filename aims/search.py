def search_by_title(items, title):
    """Return DVDs whose titles contain the given text, ignoring case."""
    normalized_title = title.lower()
    return [dvd for dvd in items if normalized_title in dvd.title.lower()]
