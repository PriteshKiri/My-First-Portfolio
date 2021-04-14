from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_home(page_name):
    return render_template(page_name)


# def write_file(data):
# 	with open('database.txt', mode='a') as database:

# 		email = data["email"]
# 		subject = data["subject"] 
# 		message = data["message"]
# 		file = database.write(f'\n{email},{subject},{message}')

def write_csvfile(data):
	with open('database2.csv', mode='a',  newline='' ) as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_file = csv.writer(database2, delimiter=','  , quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_file.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_csvfile(data)
		return redirect('/thankyou.html')
	else:

		return 'something went wrong!'


