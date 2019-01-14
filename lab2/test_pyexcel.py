import pyexcel
from collections import OrderedDict

a_list_of_drictory_national=[
OrderedDict({
    "Name" :'Ha',
    "Age"  :28
}),
OrderedDict({
    "Name" : 'Nguyen',
    "Age"   :29
})
,
OrderedDict({
    "Name" :'Duc',
    "Age"   :30
})
]
pyexcel.save_as(records=a_list_of_drictory_national,dest_file_name="your_file.xls")