def bmrPython()

    inchesToCm = 2.54
    ouncesToKg = 0.0283495
      
      # declare variabels
    years = 25
    feet = 5
    inches = 10
    pounds = 160
    ounces = 3
      
      # BMR arithmetic
    weightInOunces = (pounds * 16) + ounces
    weightInKg = weightInOunces * ouncesToKg
      
    heightInInches = (feet * 12) + inches
    heightInCm = heightInInches * inchesToCm
      
    maleBmr = 10 * weightInKg + 6.25 * heightInCm - 5 * years + 5
    girlBmr = 10 * weightInKg + 6.25 * heightInCm - 5 * years - 161
      
      
      # Print out BMR
      print("Male BMR is " + maleBmr + " calories/day.")