This was my first python project - the simple tax calculator.

Getting used to syntax, arithmetic operators and overall usage. 

The program is fairly simple - 

User inputs their name, prints a hello (user), then indicates the user on how to input the tax rate.

Asks the user what's their yearly income, prints said yearly income and afterwards asks for the tax rate (25 for example) 

Afterwards, I introduced a simple equation that dictates the tax will be divided by 100, so after it can be multiplied with the yearly
income to present the correct answer. 

taxes_b (divides the inputed tax  by 100)
taxes_c ( 1 - the int of taxes_b) so for example: if user inputs 30, 30/100 = 0.3, 1 - 0.3 = 0.7, so:

yearly income * 0.7 = the ammount after taxes. 

Which is exactly what happens and prints the yearly_income after taxes. 

If the user inputs a number bellow 0 or over 100 it'll print an error message instead that says "ERROR: Taxes cannot be above 100 or under 0".

