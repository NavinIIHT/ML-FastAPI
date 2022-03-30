import unittest
import sys, os
sys.path.append("..")
from fastapi.testclient import TestClient
from main import app

file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_exception_revised.txt'

client = TestClient(app)

class ExceptionalTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(file_path,"w"):
            pass

    def test_get_recipe_id_string(self):

        response = client.get("/recipe/abc")
        passed = response.status_code == 422
        passed = response.json()["detail"][0]["msg"] == "value is not a valid integer"

        if passed:
            with open(file_path, "a") as f:
                f.write("TestGetRecipeIdString=True\n")
                print("TestGetRecipeIdDatatype = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestGetRecipeIdString=False\n")
                print("TestGetRecipeIdDatatype = Failed")
        assert passed

    def test_read_NA_recipe(self):


        response = client.get("/recipe/"+str(999999232399923))
        passed = response.status_code == 404

        if passed:
            with open(file_path, "a") as f:
                f.write("TestReadNArecipe=True\n")
                print("TestReadNArecipe = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestReadNArecipe=False\n")
                print("TestReadNArecipe = Failed")
        assert passed


    def test_update_NA_recipe(self):


        response = client.put("/recipe/" + str(999999232399923) + "?recipe=chicken nuggets")
        passed = response.status_code == 404

        if passed:
            with open(file_path, "a") as f:
                f.write("TestUpdateNArecipe=True\n")
                print("TestUpdateNArecipe = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestUpdateNArecipe=False\n")
                print("TestUpdateNArecipe = Failed")
        assert passed
