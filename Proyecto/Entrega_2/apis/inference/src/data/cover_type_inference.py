from pydantic import BaseModel


class CoverType(BaseModel):
    Elevation: int = 2991
    Hillshade_9am: int = 233
    Hillshade_Noon: int = 234
    Horizontal_Distance_To_Fire_Points: int = 1570
    Horizontal_Distance_To_Hydrology: int = 67
    Horizontal_Distance_To_Roadways: int = 1015
    Slope: int = 7
    Soil_Type: int = 22
    Vertical_Distance_To_Hydrology: int = 11
    Wilderness_Area: int = 1