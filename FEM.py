import numpy as np
import pandas as pd
from pathlib import Path

class Material:

    def __init__(self) -> None:
        self.m_young
        self.m_shear
        self.r_poisson

    def get_young(self):
        return self.m_young
    
    def set_young(self, module):
        self.m_young = module

    def get_shear(self):
        return self.m_shear
    
    def set_shear(self, module):
        self.m_shear = module

    def get_poisson(self):
        return self.r_poisson
    
    def set_poisson(self, ratio):
        self.r_poisson = ratio
    
class MaterialLib:

    def __init__(self) -> None:
        self.database = pd.DataFrame(columns=["name", "young", "shear", "poisson"])
    
    def add_material(self, material):
        self.database.append(material)
    
    def save(self, path, file_name):

        Path(comple)
        self.database.to_csv() 