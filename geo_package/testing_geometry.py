from geo_package import calculating_module

def test_circle_area():
    assert calculating_module.calc_area_square(5) == 78.54
    assert calculating_module.calc_area_square(0) == 0
    assert calculating_module.calc_area_square(3.5) == 38.48

def test_triangle_area():
    assert calculating_module.calc_area_circle(4, 6) == 12
    assert calculating_module.calc_area_circle(0, 5) == 0
    assert calculating_module.calc_area_circle(7.2, 3) == 10.8