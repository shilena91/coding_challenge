import subprocess
from app import *

def testAPI():
	url = "http://127.0.0.1:5000/analyze"
	header = "Content-Type: application/json"
	with app.app_context():
		file = open("expected_results.txt", "r")
		jsonInput = json.loads(file.read())
		jsonOutput = []
		for i in jsonInput:
			jsonData = { "text": i["input"] }
			jsonData = json.dumps(jsonData)
			cmd = ['curl', '-H', header, '--request', 'POST', '-d', jsonData, url]
			a = subprocess.run(cmd, stdout=subprocess.PIPE)
			result = a.stdout.decode('utf-8')
			result = json.loads(result)
			if result != i["expected_result"]:
				j = {}
				j["input"] = i["input"]
				j["expected_result"] = i["expected_result"]
				j["your_result"] = result
				jsonOutput.append(j)

		if len(jsonOutput) > 0:
			newFile = open("trace.txt", "w")
			json.dump(jsonOutput, newFile)
			print("\033[1;31m" + "SOMETHING WRONG, please check file trace.txt")

testAPI()
