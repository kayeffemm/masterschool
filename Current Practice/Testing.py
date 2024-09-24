tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},
                   {'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'},
                   {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'},
                   {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'},
                   {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'},
                   {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
#{outer_key: {inner_key: myfunc(inner_value) for inner_key, inner_value in outer_value.items()}
# for outer_key, outer_v in outer_dict.items()}
compri = [i["name"] for i in tester["info"]]
print(compri)
#print(tester["info"][0]["name"])

for i in tester["info"]:
    print(i["name"])

print(len(tester["info"]))