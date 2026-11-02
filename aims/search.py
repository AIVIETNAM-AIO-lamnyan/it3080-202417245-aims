def search_by_category(items, category):
    """Return DVDs that belong to the given category."""
    return [dvd for dvd in items if dvd.category == category]


def search_by_title(items, title):
    """Return DVDs whose titles contain the given case-sensitive text."""
    return [dvd for dvd in items if title in dvd.title]
