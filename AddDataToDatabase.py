import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendencerealtime-d46f2-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "0808DS201027":
        {
            "name": "Lokesh Birle",
            "major": "Data Science",
            "starting_year": 2020,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2023-08-18 00:54:34"
        },
    "0808DS201059":
        {
            "name": "Sumit Singh Gour",
            "major": "Data Science",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-08-18 00:54:34"
        },
    "0808DS201061":
        {
            "name": "Utsav Patni",
            "major": "Data Science",
            "starting_year": 2020,
            "total_attendance": 3,
            "standing": "VG",
            "year": 4,
            "last_attendance_time": "2023-08-18 00:54:34"
        },
    "0808DS201063":
        {
            "name": "Yash Barfa",
            "major": "Data Science",
            "starting_year": 2020,
            "total_attendance": 6,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-08-18 00:54:34"
        }

}

for key, value in data.items():
    ref.child(key).set(value)
