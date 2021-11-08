from flask import Flask, jsonify, make_response
app = Flask(__name__)
@app.route('/')
def home():
    return 'Home Page'
@app.route('/interfaces')

def interfaces(line):
  d = {}
  res = make_response(jsonify(d), 200)
  return res
f = open("interfaces.txt", "r")
for line in f:
    words = line.split()
    if words:
         print(words[0])
         print("Routes per Interface:")
def getipaddress():
words = line.split("Bcast:")
if len(words) > 1:
    return words[1].split()[0]
    return ""
f = open("interfaces.txt", "r")
d = {}
print("ComputerInterfaces")
for key in d:
    print(key + ":", end="")
for i in range(len(d[key])):
    if i < (len(d[key]) - 1):
        print(d[key][i] + ", ", end="")
        else:
        print(d[key][i], end="")
f.close()
if __name__  ==  '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


