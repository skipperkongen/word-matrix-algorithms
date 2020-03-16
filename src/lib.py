def get_neighbors(x, y, maxval=3):
    ns = []
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            nx = max(0, min(maxval, x + dx))
            ny = max(0, min(maxval, y + dy))
            if (nx,ny) != (x,y):
                ns.append((nx, ny))
    return set(ns)
