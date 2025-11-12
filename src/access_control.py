import pandas as pd

class AccessControl:
    def __init__(self, admin_profile):
        """
        Initialize with admin profile containing:
        - allowed_grades: list of integers
        - allowed_classes: list of strings
        - allowed_regions: list of strings
        """
        self.admin_profile = admin_profile
    
    def filter_data(self, df):
        """
        Apply role-based filtering to DataFrame
        Returns only data the admin is authorized to see
        """
        if not self.admin_profile:
            return pd.DataFrame()  # Empty if no admin profile
        
        filtered_df = df.copy()
        
        # Filter by grade
        if 'allowed_grades' in self.admin_profile:
            filtered_df = filtered_df[
                filtered_df['grade'].isin(self.admin_profile['allowed_grades'])
            ]
        
        # Filter by class
        if 'allowed_classes' in self.admin_profile:
            filtered_df = filtered_df[
                filtered_df['class'].isin(self.admin_profile['allowed_classes'])
            ]
        
        # Filter by region
        if 'allowed_regions' in self.admin_profile:
            filtered_df = filtered_df[
                filtered_df['region'].isin(self.admin_profile['allowed_regions'])
            ]
        
        return filtered_df
    
    def get_access_summary(self):
        """Return human-readable access summary"""
        if not self.admin_profile:
            return "No access granted"
        
        summary = []
        if 'allowed_grades' in self.admin_profile:
            summary.append(f"Grades: {', '.join(map(str, self.admin_profile['allowed_grades']))}")
        if 'allowed_classes' in self.admin_profile:
            summary.append(f"Classes: {', '.join(self.admin_profile['allowed_classes'])}")
        if 'allowed_regions' in self.admin_profile:
            summary.append(f"Regions: {', '.join(self.admin_profile['allowed_regions'])}")
        
        return " | ".join(summary)