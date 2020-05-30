#!/usr/bin/env python
import json
import yaml
uni = {'students':[{'firstName': 'Nikki', 'lastName': 'Roysden'},
                    {'firstName':'Mervin' ,'lastName': 'Friedland'},
                    {'firstName':'Aron', 'lastName': 'Wilkins'}],
        'teachers':[{'firstName':'Amberly', 'lastName': 'Calico'},
                    {'firstName':'Regine','lastName': 'Agtarap'}]}
jsonDict = json.dumps(uni)
yamlDict = yaml.dump(uni)

print("Json is: \n{0}".format(jsonDict))
print("YAML is: \n{0}".format(yamlDict))

print("fjsd     ".rstrip())
