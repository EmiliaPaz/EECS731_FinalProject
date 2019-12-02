import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class __SupervisorDistricts:

  def __init__(self):
    self.__shapes = self.__gen_shapes()

  def __gen_shapes(self):
    df = pd.read_csv("../../data/raw/Current_Supervisor_Districts.csv").sort_values(by="supervisor")
    shapes = []
    for row in df.values:
      coords = row[1][len("MULTIPOLYGON ((("):]
      coords = coords[:len(coords)-len(")))")]
      coords_split = coords.split(", ")
      list_of_coords = []
      for coord in coords_split:
        coord = coord.split(" ")
        try:
          list_of_coords.append((float(coord[0]), float(coord[1])))
        except Exception as e: # TODO This should be changed to allow for multiple polygons
          if coord[0][0] == "(":
            list_of_coords.append((float(coord[0][len("(("):]), float(coord[1])))
          elif coord[1][len(coord[1])-1] == ")":
            list_of_coords.append((float(coord[0]), float(coord[1][:len(coord[1])-len("))")])))
      shapes.append((row[0], Polygon(list_of_coords)))
    return shapes

  def get_district(self, lat, lon):
    p = Point(lat, lon)
    for i, (name, shape) in enumerate(self.__shapes):
      if shape.contains(p):
        return {"district_num": i + 1, "name": name}
    raise Exception("District not found for point ({}, {})".format(lat, lon))

sd = __SupervisorDistricts()