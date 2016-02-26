from myapp import app
from flask import render_template

template = {
	'menu': { 'Home': '/' }
}

@app.route('/')
def skeleton_template():
    user = { 'name': 'rgooler' }
    page = { 'name': 'Skeleton App'}
    return render_template("skeleton_template.html", 
    	                   template = template,
    	                   page = page, 
    	                   user = user)