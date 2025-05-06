from flask import Flask, jsonify, request

app = Flask(__name__)

#mock data
students = [
  {
    "rollNo": 1,
    "name": "Abhinav Singh",
    "marks": {
      "Unit Test - 1": { "SST": 83, "MATHS": 88, "Science": 76 },
      "Unit Test - 2": { "SST": 81, "MATHS": 78, "Science": 74 },
      "Mid Sem": { "SST": 73, "MATHS": 63, "Science": 96 },
      "Final Exam": { "SST": 55, "MATHS": 90, "Science": 84 }
    }
  },
  {
    "rollNo": 2,
    "name": "Riya Sharma",
    "marks": {
      "Unit Test - 1": { "SST": 79, "MATHS": 82, "Science": 69 },
      "Unit Test - 2": { "SST": 76, "MATHS": 74, "Science": 72 },
      "Mid Sem": { "SST": 70, "MATHS": 67, "Science": 89 },
      "Final Exam": { "SST": 58, "MATHS": 85, "Science": 80 }
    }
  },
  {
    "rollNo": 3,
    "name": "Aarav Patel",
    "marks": {
      "Unit Test - 1": { "SST": 75, "MATHS": 81, "Science": 65 },
      "Unit Test - 2": { "SST": 73, "MATHS": 76, "Science": 71 },
      "Mid Sem": { "SST": 72, "MATHS": 61, "Science": 90 },
      "Final Exam": { "SST": 56, "MATHS": 83, "Science": 79 }
    }
  },
  {
    "rollNo": 4,
    "name": "Isha Gupta",
    "marks": {
      "Unit Test - 1": { "SST": 70, "MATHS": 77, "Science": 64 },
      "Unit Test - 2": { "SST": 68, "MATHS": 72, "Science": 69 },
      "Mid Sem": { "SST": 65, "MATHS": 58, "Science": 88 },
      "Final Exam": { "SST": 52, "MATHS": 81, "Science": 76 }
    }
  },
  {
    "rollNo": 5,
    "name": "Karan Mehta",
    "marks": {
      "Unit Test - 1": { "SST": 82, "MATHS": 85, "Science": 75 },
      "Unit Test - 2": { "SST": 79, "MATHS": 77, "Science": 70 },
      "Mid Sem": { "SST": 69, "MATHS": 64, "Science": 91 },
      "Final Exam": { "SST": 60, "MATHS": 88, "Science": 82 }
    }
  },
  {
    "rollNo": 6,
    "name": "Nisha Verma",
    "marks": {
      "Unit Test - 1": { "SST": 68, "MATHS": 74, "Science": 60 },
      "Unit Test - 2": { "SST": 65, "MATHS": 70, "Science": 65 },
      "Mid Sem": { "SST": 62, "MATHS": 55, "Science": 83 },
      "Final Exam": { "SST": 50, "MATHS": 79, "Science": 75 }
    }
  },
  {
    "rollNo": 7,
    "name": "Rohan Das",
    "marks": {
      "Unit Test - 1": { "SST": 69, "MATHS": 75, "Science": 61 },
      "Unit Test - 2": { "SST": 66, "MATHS": 71, "Science": 67 },
      "Mid Sem": { "SST": 64, "MATHS": 57, "Science": 85 },
      "Final Exam": { "SST": 51, "MATHS": 80, "Science": 78 }
    }
  },
  {
    "rollNo": 8,
    "name": "Simran Kaur",
    "marks": {
      "Unit Test - 1": { "SST": 78, "MATHS": 83, "Science": 73 },
      "Unit Test - 2": { "SST": 75, "MATHS": 76, "Science": 68 },
      "Mid Sem": { "SST": 67, "MATHS": 62, "Science": 87 },
      "Final Exam": { "SST": 59, "MATHS": 86, "Science": 81 }
    }
  },
  {
    "rollNo": 9,
    "name": "Tina Roy",
    "marks": {
      "Unit Test - 1": { "SST": 74, "MATHS": 80, "Science": 70 },
      "Unit Test - 2": { "SST": 71, "MATHS": 73, "Science": 66 },
      "Mid Sem": { "SST": 66, "MATHS": 60, "Science": 86 },
      "Final Exam": { "SST": 53, "MATHS": 84, "Science": 77 }
    }
  },
  {
    "rollNo": 10,
    "name": "Vikram Singh",
    "marks": {
      "Unit Test - 1": { "SST": 85, "MATHS": 89, "Science": 77 },
      "Unit Test - 2": { "SST": 83, "MATHS": 80, "Science": 73 },
      "Mid Sem": { "SST": 75, "MATHS": 66, "Science": 94 },
      "Final Exam": { "SST": 61, "MATHS": 91, "Science": 85 }
    }
  }
]



@app.route('/students', methods=['GET'])
def get_students():
    min_marks = request.args.get('minMarks', type=int)
    if min_marks is not None:
        # Filter students based on average marks across all subjects
        filtered = []
        for student in students:
            total_marks = sum(
                sum(subject_marks.values()) for subject_marks in student['marks'].values()
            )
            num_subjects = sum(len(subject_marks) for subject_marks in student['marks'].values())
            avg_marks = total_marks / num_subjects  # Calculate average marks
            if avg_marks >= min_marks:
                filtered.append(student)
        return jsonify(filtered), 200
    return jsonify(students), 200

# Get student by roll number
@app.route('/students/<int:roll_no>', methods=['GET'])
def get_student_by_roll_no(roll_no):
    student = next((s for s in students if s["rollNo"] == roll_no), None)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)