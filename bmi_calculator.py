import pandas as pd
import unittest 

class ProcessData():
    def __init__(self, json_string):
        self.dataFrame = pd.read_json(json_string)
    
    def category(self, bmi):
        if bmi<=18.4:
            return "Underweight"
        elif 18.5<=bmi<=24.9:
            return "Normal weight"
        elif 25.0<=bmi<=29.9:
            return "Overweight"
        elif 30.0<=bmi<=34.9:
            return "Moderately obese"
        elif 35.0<=bmi<=39.9:
            return "Severely obese"
        elif 40.0<=bmi:
            return "Very severely obese"
        else:
            return "Something went wrong"

    def risk(self, bmi):
        if bmi<=18.4:
            return "Malnutrition risk"
        elif 18.5<=bmi<=24.9:
            return "Low risk"
        elif 25.0<=bmi<=29.9:
            return "Enhanced risk"
        elif 30.0<=bmi<=34.9:
            return "Medium risk"
        elif 35.0<=bmi<=39.9:
            return "High risk"
        elif 40.0<=bmi:
            return "Very high risk"
        else:
            return "Something went wrong"
            
    def execute(self):
        self.dataFrame['BMI(kg/m2)'] = round(self.dataFrame.WeightKg/(self.dataFrame.HeightCm/100)**2,2)
        self.dataFrame=self.dataFrame.assign(BMICategory=self.dataFrame['BMI(kg/m2)'].apply(self.category), HealthRisk=self.dataFrame['BMI(kg/m2)'].apply(self.risk))
        self.overweight = self.dataFrame['BMICategory'].value_counts()['Overweight']
        # self.dataFrame['BMI Category'] = self.dataFrame['BMI(kg/m2)'].apply(self.category)
        # self.dataFrame['Health risk'] = self.dataFrame['BMI(kg/m2)'].apply(self.risk)
        return (self.dataFrame.to_json(orient='records'), self.overweight)
        
class OutputTest(unittest.TestCase):
    def test(self):
        self.maxDiff = None
        json_string = '''[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
             { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
             { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
             { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
             {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
             {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'''
        out_str = '''[{"Gender":"Male","HeightCm":171,"WeightKg":96,"BMI(kg\/m2)":32.83,"BMICategory":"Moderately obese","HealthRisk":"Medium risk"},{"Gender":"Male","HeightCm":161,"WeightKg":85,"BMI(kg\/m2)":32.79,"BMICategory":"Moderately obese","HealthRisk":"Medium risk"},{"Gender":"Male","HeightCm":180,"WeightKg":77,"BMI(kg\/m2)":23.77,"BMICategory":"Normal weight","HealthRisk":"Low risk"},{"Gender":"Female","HeightCm":166,"WeightKg":62,"BMI(kg\/m2)":22.5,"BMICategory":"Normal weight","HealthRisk":"Low risk"},{"Gender":"Female","HeightCm":150,"WeightKg":70,"BMI(kg\/m2)":31.11,"BMICategory":"Moderately obese","HealthRisk":"Medium risk"},{"Gender":"Female","HeightCm":167,"WeightKg":82,"BMI(kg\/m2)":29.4,"BMICategory":"Overweight","HealthRisk":"Enhanced risk"}]'''
        ProcessDataObj = ProcessData(json_string)
        output = ProcessDataObj.execute()
        self.assertEqual(output[0], out_str)
        self.assertEqual(output[1], 1)
        
     
if __name__ == "__main__":
    unittest.main()
    # json_string = '''[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
     # { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
     # { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
     # { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
     # {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
     # {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'''
    
    # ProcessDataObj = ProcessData(json_string)
    # print(ProcessDataObj.execute()[0])
    # print(ProcessDataObj.execute()[1])
    