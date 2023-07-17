from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/report')
def report():
        username=request.args.get('username')
        password=request.args.get('password')
        lc_flag=0
        uc_flag=0
        len_flag=0
        num_flag=0
        for char in password:
            if(lowercase(char)):
                lc_flag=1
            if(uppercase(char)):
                uc_flag=1
        if password[-1].isnumeric():
            num_flag=1
        if len(password)>7:
            len_flag=1
        res=''
        if lc_flag==1 and uc_flag==1 and len_flag==1 and num_flag==1:
            res= "<p> All requirements passed</p>"
        else:
            if lc_flag==0:
                res=res+"<p>In your password you dont have lowercase</p>"
            if uc_flag==0:
                res=res+"<p>In your password you dont have uppercase</p>"
            if num_flag==0:
                res=res+"<p>In your password it did not end with number</p>"
            if len_flag==0:
                res=res+"<p>In your password the length of the number is less than 8</p>"    
        
        
        return render_template("report.html",res=res)
        
    

def lowercase(pasword):
    if pasword.islower():
        return True
    return False


def uppercase(uppercase):
    if uppercase.isupper():
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True ,  port=8007)
