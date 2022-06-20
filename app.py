from flask import Flask,jsonify,request

app=Flask(_name_)


tasks=[
        {
             'id':1,
             'title':u'buy groceries',
             'description':u'Milk,Chesse,Pizza,Fruit,Vegatable',
             'done':False
        },
          {
             'id':2,
             'title':u'learn python',
             'description':u'need to learn python frmo whitehatjr',
             'done':False
        }
      ]

@app.route('/')
def hello_world():
    return "hello world"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    task={
             'id':task[-1]['id']+1,
             'title':request.json['title'],
             'description':request.json.get('description',""),
             'done':False
         }

    tasks.append(task)
    return jsonify({
              "status":"success",
              "message":"Task Added sucessfully"
         })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(_name_=="_main_"):
    app.run(debug=True)