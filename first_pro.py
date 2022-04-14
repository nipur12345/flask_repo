import io
import time
from first_flask.boto3_fun import *
# from flask_project import boto3_fun
from flask import Flask, redirect, url_for, request,render_template
from dotenv import load_dotenv
import logging
from first_flask.logger_integration_s3 import put_content_to_s3
from first_flask.string_io_loggerr import get_string_io_logger
from datetime import datetime

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
import atexit
import io


def write_logs(body, bucket, key):
   s3 = boto3.client("s3")
   s3.put_object(Body=body, Bucket=bucket)

log = logging.getLogger("some_log_name")
log_stringio = io.StringIO()
handler = logging.StreamHandler(log_stringio)
log.addHandler(handler)

atexit.register(write_logs, body=log_stringio.getvalue(), bucket="nipur-input-bucket")


load_dotenv()
app = Flask(__name__)

@app.route('/flask/')
def hello_flask():
   log_stringio_obj = io.StringIO()
   log_handler = logging.StreamHandler(log_stringio_obj)
   logger = get_string_io_logger(log_stringio_obj, logger_name='my_s3_logger')
   timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
   s3_log_path = "s3://nipur-input-bucket/test/"
   logger.info("Running my_function4")
   logger.info("Running my_function34")
   logger.info("Running my_function34 Success")
   logger.error("Running my_function Error")
   logger.warning("Running my_function  Warning")
   log.info("Hello S3")
   # s3_store_response = put_content_to_s3(s3_path= s3_log_path+'{0}.txt'.format(timestamp), content=log_stringio_obj.getvalue())
   # assert s3_store_response['success'], "Error Putting logs to S3:\n{0}".format(s3_store_response['data'])
   # assert s3_store_response['success'], "Error Putting logs to S3:\n{0}".format(s3_store_response['data'])
   return 'Hello Flask'

import multiprocessing

@app.route('/python/')
def hello_python():
   start = time.perf_counter()
   def speak_async():
      # for i in range(100):
      time.sleep(5)
      print("Hello I'm nipur, we are in async speak function!")
      return "successfully!"
   p1 = multiprocessing.Process(target = speak_async)
   p1.start()
   # value = speak_async()
   print("<<<<<This is the output of the async function")
   end = time.perf_counter()
   print(start,"<<<<<<<<<<<",end)
   # return render_template("index.html")
   return "value"

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return 'use login successfully %s' %user
   else:
      user = request.args.get('name')
      return 'User not login %s' %user

@app.route('/latest_file_path/')
def get_latest_path():
   if request.method == 'GET':
      s3 = boto_module()
      latest_file_path = s3.latest_file_url(prefix='test/')
      return latest_file_path

import atexit

@app.route('/faltu',methods = ['POST', 'GET'])
def faltu():
   def write_logs(body, bucket, key):
      s3 = boto3.client("s3")
      s3.put_object(Body=body, Bucket=bucket, Key=key)

   log = logging.getLogger("some_log_name")
   log_stringio = io.StringIO()
   handler = logging.StreamHandler(log_stringio)
   log.addHandler(handler)

   atexit.register(write_logs, body=log_stringio.getvalue(), bucket="nipur-input-bucket")

   log.info("Hello S3")
   return 'User not login'










import os
SECRET_KEY = os.getenv("SECURITY")
print(SECRET_KEY,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
if __name__ == '__main__':
   app.run(debug=True)