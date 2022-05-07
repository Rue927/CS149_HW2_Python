# CS149_HW2_Python
cs149 homework assignment 2 redone in python

MU's home page sometimes includes messages like "#2 public school in the South by U.S. News and World Report". It's fun to turn these messages into Mad Libs (Links to an external site.). Write a program named MadLib.java that begins with the following lines:

int count = 149;
String noun = "cats";
String phrase = "tap dance";
Then write a series of print statements that use these variables to output the following message:

Over 149 JMU students do research, take care of cats, or tap dance on campus.
Make sure your sentence ends with a newline character. (Hint: Use a combination of print and println statements).

Autolab will change the values of count, noun, and phrase before compiling and running your program. Your output must correspond to the values chosen by Autolab. For example, your program could be made to display this message instead:

Over 4321 JMU students do research, take care of a pile of rocks, or look for jobs on campus.
Exercise 2.2   Greeting
Write a program named Greeting.java that introduces yourself to the instructor. Declare and initialize the following variables: name (String), major(String), classOf (int), and sleep (double). Then use these variables to display the following output (replacing the color text):

Hi! My name is John Bowers, and I'm a Computer Science major. I plan to graduate with the class of 2008, but I only get about 6.5 hours of sleep per night. Go Dukes!
Notice that there is only one line of text. Be careful not to introduce additional newlines or spaces. For this exercise, Autolab will reject submissions that do not match the expected output 100%. You should use your own values for the four variables, not "John Bowers", etc. 

Exercise 2.3   Fun Facts
Write a program named FunFacts.java that declares and initializes a single integer variable named number. Then use this number to calculate and print the following results. For example, if the number is 74:

74 squared is 5476
74 cubed is 405224
One tenth of 74 is 7.4
74 plus 123 is 197
74 minus 456 is -382
Autolab will change the value of number before compiling and running your program. Your output must be correct for any integer chosen.

The point of this exercise is to combine print statements with arithmetic expressions. Do NOT declare any other variables besides number.

Your solution must NOT use the Math class (Chapter 4). For this exercise, Autolab will reject submissions that have the word "Math" anywhere in the file.

Exercise 2.4   Baking Bread
The holidays are approaching, and you need to buy ingredients for baking (possibly many) loaves of bread. Write a program named Baking.java that declares and initializes the following variables: breadWeight (integer), servingSize (double), and guests (integer). The output will look like this:

For 25 people, you will need 3.90625 loaves of bread:

  5.859375 teaspoons instant yeast
  5.859375 teaspoons salt
  5.859375 teaspoons sugar
  9.765625 cups all-purpose flour
  7.8125 cups sourdough starter
  1.953125 cups lukewarm water
In the above example, breadWeight is 16 (ounces), servingSize is 2.5 (ounces), and guests is 25 (people). Can you figure out how to compute the total number of loaves needed? If not, ask for help -- but don't think too hard!

According to King Arthur Flour (Links to an external site.), you will need the following ingredients for each loaf: 1 1/2 teaspoons instant yeast, 1 1/2 teaspoons salt, 1 1/2 teaspoons sugar, 2 1/2 cups all-purpose flour, 2 cups sourdough starter, and 1/2 cup lukewarm water.

Make sure your output matches the above example exactly. Notice that there are two spaces at the beginning of each line of the recipe. Autolab will change the initial value of each variable before compiling and running your program.

Exercise 2.5   Calculate BMR
Write a program named Calories.java that calculates basal metabolic rate (Links to an external site.) (BMR), which is the amount of energy you use while at rest. Declare and initialize the following integer variables: years, feet, inches, pounds, and ounces. Your program should output two lines:

Male BMR is 1717.847685 calories/day.
Female BMR is 1551.847685 calories/day.
The above example is for a 25-year-old who is 5'10" and 160 pounds, 3 ounces. Here are the formulas for BMR:

Male BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(y) + 5
Female BMR = 10 × weight(kg) + 6.25 × height(cm) - 5 × age(y) - 161
Before you can output the results, you will need to convert height and weight to the metric system (Links to an external site.). To convert inches to centimeters, multiply by 2.54. To convert from ounces to kilograms, multiply by 0.0283495. Remember also that one foot is 12 inches, and one pound is 16 ounces.

Notice that the BMR formulas are the same except for the last term. Avoid making the same calculation twice in your source code.
