import json
import random

students = [
("230177",301,"SCT23AM001","Aadil Sandeep","Male"),
("230411",302,"SCT23AM002","Abhay Krishna","Male"),
("230578",303,"SCT23AM003","Abhin C","Male"),
("230508",304,"SCT23AM004","Adithyan B M","Male"),
("230233",305,"SCT23AM005","Adithyan R","Male"),
("230232",306,"SCT23AM006","Adithyan U M","Male"),
("230641",307,"SCT23AM007","Advaith S Vinod","Male"),
("230542",308,"SCT23AM008","Aishwarya S A","Female"),
("230207",309,"SCT23AM009","Aiswarya Sreekumar","Female"),
("230571",310,"SCT23AM010","Akash A J","Male"),
("230196",311,"SCT23AM011","Akhilesh S","Male"),
("230555",312,"SCT23AM012","Alfin Muhammed S","Male"),
("230549",313,"SCT23AM013","Alna Mariya C T","Female"),
("230100",314,"SCT23AM014","Amarnath D J","Male"),
("230235",315,"SCT23AM015","Anantha Padmanabhan D","Male"),
("230491",316,"SCT23AM016","Anjali S Nair","Female"),
("230538",317,"SCT23AM017","Annu Maria Soney","Female"),
("230030",318,"SCT23AM018","Ansiba S N","Female"),
("230229",319,"SCT23AM019","Ashish M Thaha","Male"),
("230215",320,"SCT23AM020","Ashlin Jones","Female"),
("230412",321,"SCT23AM021","Ashwin Prakash","Male"),
("230545",322,"SCT23AM022","Aswin Binoy","Male"),
("230505",323,"SCT23AM023","Athira C","Female"),
("230101",324,"SCT23AM024","Athul Krishna Naduvilpura","Male"),
("230241",325,"SCT23AM025","Benson Babu Jacob","Male"),
("230021",326,"SCT23AM026","Bhanupriya C P","Female"),
("230225",327,"SCT23AM027","Devadathya","Female"),
("230222",328,"SCT23AM028","Devanand J","Male"),
("230217",329,"SCT23AM029","Devika I","Female"),
("230211",330,"SCT23AM030","Diva Ajith","Female"),
("230534",331,"SCT23AM031","Diva M P","Female"),
("230252",332,"SCT23AM032","Ebin Babu","Male"),
("230008",333,"SCT23AM033","Eben B Gilbert","Male"),
("230231",334,"SCT23AM034","Gautam B S","Male"),
("230231",335,"SCT23AM035","Gautam B S","Male"),
("230226",336,"SCT23AM036","Gowri R R","Female"),
("230098",337,"SCT23AM037","Harshan Nair","Male"),
("230224",338,"SCT23AM038","Jeffin Mathew","Male"),
("230246",339,"SCT23AM039","Kailas S S","Male"),
("230208",340,"SCT23AM040","Keerthi P","Female"),
("230190",341,"SCT23AM041","Kevin Varghese","Male"),
("230221",342,"SCT23AM042","Lakshmi R","Female"),
("230219",343,"SCT23AM043","Lekshmi S Nair","Female"),
("230215",344,"SCT23AM044","Madhav Krishna","Male"),
("230216",345,"SCT23AM045","Meenakshy Aj","Female"),
("230220",346,"SCT23AM046","Mehthab Yasir","Male"),
("230208",347,"SCT23AM047","Muhammed Sinan D","Male"),
("230586",348,"SCT23AM048","Mukundan V S","Male"),
("230247",349,"SCT23AM049","Nakhathe Bhargavi","Female"),
("230234",350,"SCT23AM050","Nikhil Prasad","Male"),
("230237",351,"SCT23AM051","Paul Johnston","Male"),
("230585",352,"SCT23AM052","Pranav M Nair","Male"),
("230540",353,"SCT23AM053","Rinu Antony","Female"),
("230023",354,"SCT23AM054","Riya Kunjumon","Female"),
("230526",355,"SCT23AM055","Rohit Raj","Male"),
("230218",356,"SCT23AM056","Rohit V S","Male"),
("230409",357,"SCT23AM057","S Aathira","Female"),
("230248",358,"SCT23AM058","S Govind Krishnan","Male"),
("230230",359,"SCT23AM059","Shahnas M","Male"),
("230004",360,"SCT23AM060","Sidharth S","Male"),
("230236",361,"SCT23AM061","Soorya Narayanan S","Male"),
("230223",362,"SCT23AM062","S R Brahan Madhav","Male"),
("230251",363,"SCT23AM063","S R Mekha","Female"),
("230256",364,"SCT23AM064","Thejas Baiju","Male"),
("230240",365,"SCT23AM065","Vidya Vijayan S","Female"),
("240025",366,"SCT23AM066","Adhway Satheesh K","Female"),
("240012",367,"SCT23AM067","Devduth","Male"),
("240037",368,"SCT23AM068","Gokul S","Male"),
("240017",369,"SCT23AM069","Gokul B S","Male"),
("240023",370,"SCT23AM070","Nikhil P S","Male"),
("240001",371,"SCT23AM071","Rahul J A","Male")
]

sports = ["Football","Cricket","Badminton","Basketball","Volleyball"]
culturals = ["Dance","Music","Drama","Photography","Debate"]
hackathons = ["Smart India Hackathon","AI Innovation Hackathon","Campus Hackathon"]
skills = ["Python","Machine Learning","SQL","Java","React","AWS"]

dataset=[]

for s in students:

    sgpa=[round(random.uniform(7.5,9.5),2) for _ in range(8)]
    cgpa=round(sum(sgpa)/8,2)

    student={
        "name":s[3],
        "admission_no":s[0],
        "roll_no":s[1],
        "univ_reg_no":s[2],
        "gender":s[4],

        "sgpa":{
            "sem1":sgpa[0],
            "sem2":sgpa[1],
            "sem3":sgpa[2],
            "sem4":sgpa[3],
            "sem5":sgpa[4],
            "sem6":sgpa[5],
            "sem7":sgpa[6],
            "sem8":sgpa[7]
        },

        "cgpa":cgpa,

        "uploaded_certificates":{
            "sports":[
                {
                    "event":random.choice(sports),
                    "certificate_file":f"{s[3].replace(' ','_').lower()}_sports.pdf",
                    "verified_by":"sports_coordinator"
                }
            ],

            "cultural":[
                {
                    "event":random.choice(culturals),
                    "certificate_file":f"{s[3].replace(' ','_').lower()}_cultural.pdf",
                    "verified_by":"cultural_committee"
                }
            ],

            "hackathons":[
                {
                    "event":random.choice(hackathons),
                    "certificate_file":f"{s[3].replace(' ','_').lower()}_hackathon.pdf",
                    "verified_by":"innovation_cell"
                }
            ]
        },

        "skills":random.sample(skills,3),

        "internships":[
            {
                "company":"TechCorp",
                "role":"Software Intern",
                "certificate_file":f"{s[3].replace(' ','_').lower()}_internship.pdf"
            }
        ]
    }

    dataset.append(student)

with open("students_dataset.json","w") as f:
    json.dump(dataset,f,indent=2)

print("Dataset created: students_dataset.json")