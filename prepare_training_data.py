import json

with open("students_dataset.json") as f:
    students = json.load(f)

training_data = []

for s in students:

    name = s["name"]
    cgpa = s["cgpa"]
    skills = ", ".join(s["skills"])

    sports = s["uploaded_certificates"]["sports"][0]["event"]
    cultural = s["uploaded_certificates"]["cultural"][0]["event"]
    hackathon = s["uploaded_certificates"]["hackathons"][0]["event"]

    training_data.append({
        "text": f"<s>[INST] Tell me about {name} [/INST] {name} has a CGPA of {cgpa}. Skills include {skills}. Uploaded certificates include {sports}, {cultural}, and {hackathon}. </s>"
    })

    training_data.append({
        "text": f"<s>[INST] What certificates has {name} uploaded? [/INST] {name} has uploaded certificates for {sports}, {cultural}, and {hackathon}. </s>"
    })

with open("train_data.json", "w") as f:
    json.dump(training_data, f, indent=2)

print("Training dataset created.")