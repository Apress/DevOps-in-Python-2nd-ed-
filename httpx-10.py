def to_canonical_url(raw_url):
    url = urlparse(raw_url)
    path = url.path or "/"
    query = canonical_query_string(url.query)
    return (
        url.scheme +
        "://" +
        url.netloc +
        path +
        query
    )
