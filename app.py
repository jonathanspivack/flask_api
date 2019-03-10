from flask import Flask
import sqlite3
import json
from flask_cors import CORS, cross_origin
from flask import request


app = Flask(__name__)
CORS(app)


@app.route("/getjobs")
def get_jobs():
    connection = sqlite3.connect('muse.db')
    cursor = connection.cursor()

    jobs = []
    select_query = "SELECT * FROM jobs"

    for row in cursor.execute(select_query):

        job = {
                    "id":row[0],
                    "company":row[1],
                    "logo":row[2],
                    "location":row[3],
                    "job_title":row[4],
                    "job_description":row[5],
                    "link":row[6],
                    "views":row[7]

        }

        jobs.append(job)

    connection.close()

    return json.dumps(jobs)

@app.route("/jobview/<job_id>")
def increament_job_views(job_id):
    connection = sqlite3.connect('muse.db')
    cursor = connection.cursor()

    insert_query = "UPDATE jobs SET views = views + 1  WHERE id = " + job_id

    cursor.execute(insert_query)
    connection.commit()
    connection.close()

    return "added view to job"

@app.route("/addjob",methods = ['POST'])
def update_job():
    job = request.get_json()

    connection = sqlite3.connect('muse.db')
    cursor = connection.cursor()

    insert_query = "INSERT INTO jobs" \
                   "(company_name,company_logo,location,job_title,job_description,link,views) VALUES (?,?,?,?,?,?,?)"

    job = (
                job['company'],
                job['logoId'],
                job['location'],
                job['jobTitle'],
                job['description'],
                job['link'],
                0
            )

    cursor.execute(insert_query, job)

    connection.commit()
    connection.close()


    return "added job"




if __name__ == "__main__":
    app.run()