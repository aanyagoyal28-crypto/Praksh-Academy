'''
E1. GDP Growth Classifier Write a program that takes a country's GDP growth rate (a float, e.g. 2.5) and prints whether the economy is in "Recession" (growth < 0), "Stagnant" (0 <= growth < 2), or "Growing" (growth >= 2). Use if/elif/else.

E2. Currency Code Slicing You have the string ticker = "USD/INR". Using slicing, extract the base currency ("USD") and the quote currency ("INR") into two separate variables, without using .split().

E3. Formatted Price Tag You have product = "Coffee" and price = 3.5. Use an f-string to print: Coffee costs $3.50 (price must show exactly 2 decimal places).

E4. Sum of Quarterly Revenues Given a list revenues = [120000, 135000, 98000, 150000] representing four quarters, use a for loop to compute and print the total annual revenue.

E5. Unique Industries Set Given a list industries = ["tech", "finance", "tech", "retail", "finance", "energy"], create a set of unique industries and print how many distinct industries there are.
'''
#q1
# growth= float(input("Enter the GDP : "))
# if growth<0:
#     print("Recession")
# elif growth<2:
#     print("Stagnant")
# else:
#     print("Growing")

# #q2
# ticker = "USD/INR"
# print(ticker[:3])
# print(ticker[4:7])

# #q3
# product = "Coffee"
# price = 3.5
# print(f"{product} costs Rs {price:.2f}")

#q4
# revenues = [120000, 135000, 98000, 150000]
# print(sum(revenues))
# total=0
# for i in revenues:
#     total+=i
# print(total)

#q5
# industries = ["tech", "finance", "tech", "retail", "finance", "energy"]
# unique_industries= set(industries)
# print(unique_industries)


#q6
# inflation = [1.2, 3.4, 5.6, 2.1, 7.8, 0.5, 4.4]
# for i in inflation:
#     if i<2:
#       print("low")
#     elif i<5:
#      print("moderate")
#     else:
#      print("High")



nominal_wages = [50000, 62000, 45000, 80000]
inflation_rate = 0.06  # 6%
real_wages= [round(w / (1 + inflation_rate), 2) for w in nominal_wages]
print(real_wages)


gdp_per_capita = {"India": 2600, "USA": 76000, "Japan": 39000, "Nigeria": 2200, "Germany": 51000}