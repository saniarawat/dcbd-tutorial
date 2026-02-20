class Polynomial:
    def __init__(self, terms=None):
        #Set a Polynomial object from a list of tuples that act as coefficients and exponents.
        if terms is None:
            self.terms = {}
            return
        #Check that all exponents are non-negative integers
        for _, exp in terms:
            if exp < 0 or not isinstance(exp, int):
                raise ValueError("exponents can only be non-negative integers.")
        # Using a temporary dictionary to sum coefficients for the same exponent
        temp_dict = {}    
        for c, exp in terms:
            temp_dict[exp] = temp_dict.get(exp, 0) + c #for an exponent save the corresponding coeficient in the tuple as value, else 0
        # Filter out terms with zero coefficients and store as {exp:coeff}
        self.terms = {exp: coeff for exp, coeff in temp_dict.items() if coeff != 0}

    def iszero(self):
        #return True for zero polynomial, which is the empty dictionary 
        return not self.terms

    def __str__(self):
        if self.iszero():
            return "0" #representation of zero polynomial is "0"
        sorted_exponents = sorted(self.terms.keys(), reverse=True) #sort the dictionary made above containing {exp:coeff}
        term_strings = [] 
        for i, exp in enumerate(sorted_exponents):
            coeff = self.terms[exp]
            abs_coeff = abs(coeff) #find absolute value of the coefficients 
            #Sign handling 
            sign = ""
            if i > 0:
                sign = " + " if coeff > 0 else " - "
            elif coeff < 0:
                sign = "-"
            #Coefficient handling and omit '1' unless it's a constant
            coeff_str = ""
            if exp == 0 or abs_coeff != 1:
                 coeff_str = str(abs_coeff)
            #Exponent handling
            if exp == 0:
                exp_str = ""
            elif exp == 1:
                exp_str = "x"
            else:
                exp_str = f"x^{exp}"
            term_strings.append(f"{sign}{coeff_str}{exp_str}") 
        return "".join(term_strings).strip()

    def __add__(self, other): #define addition (+) operation to return a new polynomial 
        new_terms = self.terms.copy() #make a copy of the {exp:coeff} dictionary of self polynomial
        for exp, coeff in other.terms.items():
            new_terms[exp] = new_terms.get(exp, 0) + coeff   #assign values to the exponents by adding the coeff of same exponent of "other"
                                                            #polynomial to the coefficient of self, and 0 if the exponent not in "other" 
                                                            #polynomial
        new_terms_list = [(coeff, exp) for exp, coeff in new_terms.items()]    #Passing these combined terms back to make a list 
        return Polynomial(new_terms_list)

    def __sub__(self, other): #define subtraction (-) operation to return a new polynomial 
        new_terms = self.terms.copy() #make a copy of the {exp:coeff} dictionary of self polynomial
        for exp, coeff in other.terms.items():
            new_terms[exp] = new_terms.get(exp, 0) - coeff #assign values to the exponents by subtracting the coeff of same exponent of "other"
                                                            #polynomial from the coefficient of self, and 0 if the exponent not in "other" 
                                                            #polynomial
        new_terms_list = [(coeff, exp) for exp, coeff in new_terms.items()]   #Passing these combined terms back to make a list 
        return Polynomial(new_terms_list) 

    def __mul__(self, other): #define multiplication (*) operation to return a new polynomial 
        new_terms = {}  #dictionary that will hold exp:coeff of the product
        for exp1, coeff1 in self.terms.items(): #traverse the exp,coeff of self polynomial
            for exp2, coeff2 in other.terms.items(): #traverse the exp, coeff of other polynomials
                new_exp = exp1 + exp2 #adding the exponents because x^a * x^b = x^(a+b)
                new_coeff = coeff1 * coeff2 #multiplying the coefficients to get a new coefficient for the above exponent
                new_terms[new_exp] = new_terms.get(new_exp, 0) + new_coeff #updating the values of exp and coeff obtained in the dictionary
        new_terms_list = [(coeff, exp) for exp, coeff in new_terms.items()]  #Passing these combined terms back to make a list 
        return Polynomial(new_terms_list)

    def degree(self):
        if self.iszero(): #set the degree of zero polynomial to be 1
            return -1
        return max(self.terms.keys()) #degree is the max exponent in the polynomial 
        
    def _leading_coefficient(self):
        if self.iszero(): #leading coeff of zero polynomial is trivial
            return 0
        return self.terms[self.degree()] #leading coeff is the coeff of the exponent that is the degree
        
    def __eq__(self, other): #equal to(==) operator
        if not isinstance(other, Polynomial): #check if "other" is indeed a polynomial 
            return False 
        return self.terms == other.terms #if all {exp:coeff} terms are same, they are equal 
        
    def __lt__(self, other): #less than(<) operator
        if not isinstance(other, Polynomial):  #check if "other" is indeed a polynomial 
            return NotImplemented
        #Getting sorted exponents for both polynomials
        self_exps = sorted(self.terms.keys(), reverse=True)
        other_exps = sorted(other.terms.keys(), reverse=True)
        #Iterating through the exponents, from highest to lowest
        max_len = max(len(self_exps), len(other_exps))
        for i in range(max_len):
            self_exp = self_exps[i] if i < len(self_exps) else -1
            other_exp = other_exps[i] if i < len(other_exps) else -1
            self_coeff = self.terms.get(self_exp, 0)
            other_coeff = other.terms.get(other_exp, 0)
            #Compare degrees 
            if self_exp < other_exp:
                return True
            if self_exp > other_exp:
                return False
            #If degrees are equal, compare coefficients
            if self_coeff < other_coeff:
                return True
            if self_coeff > other_coeff:
                return False
        return False  # If all terms are equal, the polynomials are equal
    def __gt__(self, other): #define greater than(>) operator
        if not isinstance(other, Polynomial):
            return NotImplemented 
        # check if the self is neither equal to nor less than other 
        return not (self == other or self < other)
    def __le__(self, other): #define less than or equal to(<=) operator
        if not isinstance(other, Polynomial):
            return NotImplemented 
        # check if self is not greater than other
        return not (self > other)
    def __ge__(self, other): #define greater than or equal to(>=) operator
        if not isinstance(other, Polynomial):
            return NotImplemented  
        # check if self is not less than other
        return not (self < other)


print("Hello World")
