'''pprint is used to display complex Python data structures in a clean and readable format.'''
import pprint
emp = {}

emp['eid'] = [101, 102, 103, 104]
emp['ename'] = ['harshith', 'ram', 'chintu', 'chotu']
emp['edept'] = ['it', 'sales', 'hr', 'sales']

emp['dob'] = {
    'DOB': [
        {'DOB': '1st nov'},
        {'DOB': '2nd dec'},
        {'DOB': '3rd Jan'},
        {'DOB': '4th feb'}
    ]
}

pprint.pprint(emp)
