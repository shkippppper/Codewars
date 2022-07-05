def find_routes(routes: list) -> str:
    d = dict(routes)
    res = list(d.keys() - d.values())
    while res[-1] in d: res.append(d[res[-1]])
    return ', '.join(res)