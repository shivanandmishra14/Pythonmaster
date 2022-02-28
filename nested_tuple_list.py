bio_data = [("shivanand", "Allahabad", 1992),
            ("sohan", "JHarkhand", 1993),
            ("Madan", "TamilNadu", 1991)
            ]

print(len(bio_data))
for name, place, dob in bio_data:
    print("name:{}, place:{}, DOB:{}".format(name, place, dob ))
