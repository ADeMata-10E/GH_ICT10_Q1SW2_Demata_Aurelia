# how to use numerical value from an html
from pyscript import display, document

def ordering_form(e):
    item1 = document.getElementById('menu1')
    item2 = document.getElementById('menu2')
    item3 = document.getElementById('menu3')
    item4 = document.getElementById('menu4')

    customerfirstname = document.getElementById('firstname').value
    contactnumber = document.getElementById('phonenumber').value    
    customeraddress = document.getElementById('address').value

    document.getElementById('output').innerText = ''

    total = (float(item1.value) * item1.checked + 
             float(item2.value) *  item2.checked + float(item3.value) * item3.checked + 
             float(item4.value) * item4.checked)

    customersummary = f""" Order Summary

    Customer Name: {customerfirstname}
    Contact Number: {contactnumber}
    Address: {customeraddress}

    """

    
    display(customersummary, target='output')
    display(f'The total is ₱{total}', target='output')
    #i used ds2 as a reference for the formatting of the string message and the customer form part
    #i also used it for the output inner text part. it was from the sample of the form.
    #most of this is leftovers from the previous discussion in class when we started