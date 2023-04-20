from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

import requests
import os
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics


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