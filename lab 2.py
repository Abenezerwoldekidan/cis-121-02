human_age=float(input("enter your age:"))
dog_year=7*human_age
x=(dog_year)-int(dog_year)
dog_year_month=x*365
no_of_days_in_months=30
dog_month= dog_year_month // no_of_days_in_months
y= dog_month*30
z=dog_year_month-y
print( "your age in dog years is",dog_year,"years", dog_month,"month", z,"days")

cat_year=9/365
no_of_days_in_months=30
cat_month= cat_year // no_of_days_in_months
y=cat_month*30
z= cat_year-y
print("your age in cat is",cat_year,"years",cat_month,"month", z,"days")
horseyears = horseage // 1
horsemonths = ((horseage % 1) * 12) //1
horsedays = (((((horseage % 1) * 12)%1 )*30)//1)
print("You're age in horse years is", horseyears, "years", horsemonths, "months", horsedays, "days")
