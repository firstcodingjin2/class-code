from flask import Flask, request, jsonify
import deptDAO 
import log_test1 as myLog

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello!'

@app.route('/call/<param>') #get api
def get_echo_call(param):
    return jsonify({"param": param})

@app.route('/call', methods=['POST']) #post api
def post_echo_call():
    param = request.get_json()
    return jsonify(param)

@app.route('/api/depts', methods=['GET']) #GET
def get_depts():
    dept_list = deptDAO.selectDept()
    print(jsonify(dept_list))
    #myLog.logger.info('get /api/depts  call')
    return jsonify(dept_list)


@app.route('/api/dept', methods=['POST']) #GET  user = request.get_json()#json 데이터를 받아옴
def post_dept():
    
    dept = request.get_json()   
    print(dept)
    #myLog.logger.info('get /api/depts  call')
    deptDAO.insertDept(dept['dname'], dept['loc'])
    
    return jsonify({'code':200, 'msg' : 'insert ok!'})

if __name__ == "__main__":
    app.run(debug= False)
