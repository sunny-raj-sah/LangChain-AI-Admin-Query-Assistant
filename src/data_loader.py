import json
import pandas as pd
from pathlib import Path

class DataLoader:
    def __init__(self, students_path='data/students_data.json', 
                 admins_path='data/admins_data.json'):
        self.students_path = Path(students_path)
        self.admins_path = Path(admins_path)
    
    def load_students(self):
        """Load student data into pandas DataFrame"""
        with open(self.students_path, 'r') as f:
            data = json.load(f)
        return pd.DataFrame(data)
    
    def load_admins(self):
        """Load admin data"""
        with open(self.admins_path, 'r') as f:
            return json.load(f)
    
    def get_admin_by_id(self, admin_id):
        """Get specific admin details"""
        admins = self.load_admins()
        for admin in admins:
            if admin['admin_id'] == admin_id:
                return admin
        return None