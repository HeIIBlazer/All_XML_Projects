import xml.etree.ElementTree as ET

'''CURRENCY_PARSE '''
Currency = ET.parse('Currency.xml')
root = Currency.getroot()

roots = []

for item in root.findall('./country'):
    currency = {}
    currency['country'] = item.attrib['name']
    for child in item:
        if child.tag == 'symbol':
            currency['symbol'] = child.text
        if child.tag == 'currency':
            currency['currency'] = child.text
        if child.tag == 'year':
            currency['year'] = child.text

    roots.append(currency)
print(roots)


'''IVKHK_PARSE'''

print ( )
ivkhk = ET.parse('Vassiljev_ivkhk.xml')  
staff = ivkhk.getroot()

staffs = []

for item in staff.findall('./department'):
    sphere = {}
    sphere['Department'] = item.attrib['name']
    for child in item:
        if child.tag == 'speciality':
            sphere['Speciality'] = child.attrib['name']
            staffs.append(sphere)
            for child1 in child:
                if child1.tag == 'group':
                    group={}
                    group['Group'] = child1.attrib['name']
                    staffs.append(group)
                    for child2 in child1:
                        if child2.tag == 'student':
                            student = {}
                            student['student'] = child2.text
                            staffs.append(student)


print(staffs)