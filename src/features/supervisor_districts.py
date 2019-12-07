import numpy as np
import pandas as pd
import re
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class __SupervisorDistricts:

  def __init__(self):
    self.__shapes = self.__gen_shapes()

  def __gen_shapes(self):
    df = pd.read_csv("../../data/raw/Current_Supervisor_Districts.csv").sort_values(by="supervisor")
    shapes = []
    # test_df = [["Test1", "MULTIPOLYGON (((1 1, 1 2, 2 2, 2 1)))"],
    #            ["Test2", "MULTIPOLYGON (((1 1, 1 2, 2 2, 2 1)), ((-1 -1, -1 -2, -2 -2, -2 -1)))"]]
    # for i, row in enumerate(test_df):
    for i, row in enumerate(df.values):
      coords_str = re.compile(r"MULTIPOLYGON \(\(\((.+)\)\)\)").match(row[1]).group(1)
      coords_list = []
      if coords_str.find(")") != -1:
        coords_list = re.compile(r"(.+)\)\), \(\((.+)").match(coords_str).groups()
      else:
        coords_list = [coords_str]
      for coords in coords_list:
        coords_split = coords.split(", ")
        list_of_coords = []
        for coord in coords_split:
          coord = coord.split(" ")
          list_of_coords.append((float(coord[0]), float(coord[1])))
        if len(shapes) == i:
          shapes.append((row[0], Polygon(list_of_coords)))
        else:
          shapes[i] = (shapes[i][0], shapes[i][1].union(Polygon(list_of_coords)))
    return shapes

  def get_district(self, lat, lon):
    p = Point(lat, lon)
    for i, (name, shape) in enumerate(self.__shapes):
      if shape.contains(p):
        return {"district_num": i + 1, "name": name}
    raise Exception("District not found for point ({}, {})".format(lat, lon))

sd = __SupervisorDistricts()