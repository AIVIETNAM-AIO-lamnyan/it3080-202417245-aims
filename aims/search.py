def search_by_title(items, title):
    """Return DVDs whose titles contain the given case-sensitive text."""
    return [dvd for dvd in items if title in dvd.title]
