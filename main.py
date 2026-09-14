# ICT Skills Test
from pyscript import display, document

# Setting variables
def get_receipt(e):
    document.getElementById('receipt').innerHTML = ""

    tickitem1 = float(document.getElementById('usa').value) * document.getElementById("usa").checked
    tickitem2 = float(document.getElementById('jelly').value) * document.getElementById("jelly").checked
    tickitem3 = float(document.getElementById('cm').value) * document.getElementById("cm").checked
    tickitem4 = float(document.getElementById('affogato').value) * document.getElementById("affogato").checked
    tickitem5 = float(document.getElementById('cold').value) * document.getElementById("cold").checked
    tickitem6 = float(document.getElementById('mocha').value) * document.getElementById("mocha").checked

    subtotal = tickitem1 + tickitem2 + tickitem3 + tickitem4 + tickitem5 + tickitem6
    vat = float(subtotal * 0.12)

# Displays the Subtotal, VAT, and Total
    display(f'Subtotal: ₱{subtotal}', target='receipt')
    display(f'VAT: ₱{vat}', target='receipt')
    display(f'Total: ₱{subtotal + vat}', target='receipt')