from flask import render_template, redirect, Flask, request
from cisco import router

app = Flask(__name__)

@app.route('/')
def redirect_to_index():
    return redirect('/index', code=302)

@app.route('/index',methods = ['POST', 'GET'])
def index():
	if request.method == 'POST':
		result = request.form.to_dict()
		cisco = router('cisco_ios', result['hostname'], result['username'], result['password'] , result['port'])
		return render_template('index.html',result=cisco.connect())
	else:
		return render_template('index.html')

@app.errorhandler(500)
def connection_time_out(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
