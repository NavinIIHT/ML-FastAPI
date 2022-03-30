import sys, os
sys.path.append("..")
import unittest
from fastapi.testclient import TestClient
from main import app

file_path = os.path.dirname(os.path.realpath(__file__)) + '/../output_revised.txt'

client = TestClient(app)

class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(file_path, "w"):
            pass

    def test_root(self):

        response = client.get("/")
        passed = response.status_code == 200

        if passed:
            with open(file_path, "a") as f:
                f.write("TestRoot=True\n")
                print("TestRoot = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestRoot=False\n")
                print("TestRoot = Failed")
        assert passed

    def test_create_recipe(self):

        response = client.post("/recipe", json = {"recipe" : "potato chips"})
        passed = response.status_code == 200
        #passed = response.json()["recipe"] == "potato chips"
        if passed:
            with open(file_path, "a") as f:
                f.write("TestCreateRecipe=True\n")
                print("TestCreateRecipe = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestCreateRecipe=False\n")
                print("TestCreateRecipe = Failed")
        print(response, response.status_code)
        assert passed

    def test_read_recipe(self):

        response = client.post("/recipe", json = {"recipe" : "potato chips"})
        passed = response.status_code == 200

        if passed:
            id = response.json()["id"]
            recipe = response.json()["recipe"]

            response = client.get("/recipe/"+str(id))
            passed = response.status_code == 200
            if passed:
                passed = response.json() == {"id": id, "recipe": recipe}
        if passed:
            with open(file_path, "a") as f:
                f.write("TestReadRecipe=True\n")
                print("TestReadRecipe = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestReadRecipe=False\n")
                print("TestReadRecipe = Failed")
        assert passed

    def test_update_recipe(self):

        response = client.post("/recipe", json = {"recipe" : "kadai chicken"})
        passed = response.status_code == 200

        if passed:
            id = response.json()["id"]

            response = client.put("/recipe/" + str(id) + "?recipe=chicken nuggets")
            passed = response.status_code == 200
            if passed:
                id = response.json()["id"]
                recipe = response.json()["recipe"]
                passed = response.json() == {"id": id, "recipe": recipe}

        if passed:
            with open(file_path, "a") as f:
                f.write("TestUpdateRecipe=True\n")
                print("TestUpdateRecipe = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestUpdateRecipe=False\n")
                print("TestUpdateRecipe = Failed")

        assert passed


    def test_delete_recipe(self):

        response = client.post("/recipe", json = {"recipe" : "kadai chicken"})
        passed = response.status_code == 200

        if passed:
            id = response.json()["id"]

            response = client.delete("/recipe/" + str(id))
            passed = response.status_code == 200

            if passed:
                response = client.get("/recipe/"+str(id))
                passed = response.status_code == 404

        if passed:
            with open(file_path, "a") as f:
                f.write("TestDeleteRecipe=True\n")
                print("TestDeleteRecipe = Passed")
        else:
            with open(file_path, "a") as f:
                f.write("TestDeleteRecipe=False\n")
                print("TestDeleteRecipe = Failed")
        print(response)
        assert passed