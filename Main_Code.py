from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
import serial
ser1=serial.Serial('COM7',115200,timeout=.1)


# we are able to make 2 different requests on our webpage
# GET = we just type in the url
# POST = some sort of form submission like a button
@app.route('/', methods=["POST", "GET"])
def hello_world():
    # variables for template page (templates/index.html)
    author = "Space Concordia Task"
    # if we make a post request on the webpage aka press button then do stuff
    if request.method == "POST":
         if request.form["submit"] == 'Rate+':
            ser1.write('d'.encode())

         elif request.form["submit"] == 'Rate-':
            ser1.write('i'.encode())

         elif request.form["submit"] == 'Start':
            ser1.write('g'.encode())

         elif request.form["submit"] == 'Stop':
            ser1.write('s'.encode())

         else:
            pass

    readval = ser1.readline().decode().strip()


    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, value=readval)


if __name__ == "__main__":
    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later

    app.run()

