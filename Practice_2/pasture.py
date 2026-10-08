def pasture_area(wire, w):
    l = (wire - 2 * w) / 3.0
    if l < 0:
        return 0.0
    return w * l

def best_pasture(wire):
    w_opt = wire / 4.0
    l_opt = (wire - 2 * w_opt) / 3.0
    area_opt = w_opt * l_opt
    return (w_opt, l_opt, area_opt)
