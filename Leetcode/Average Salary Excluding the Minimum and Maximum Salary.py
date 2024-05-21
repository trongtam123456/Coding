salary = [5000, 7000, 3000, 4000, 6000, 9000]
#sap xep luong
salary = sorted(salary)
salary_min = salary[0]
salary_max = salary[-1]
salary.remove(salary[-1])
salary.remove(salary[0])
sum = 0
for i in range(0, len(salary)):
    sum = sum + salary[i]
print('luong thap nhat la', salary_min)
print('luong cao nhat la', salary_max)
print('luong trung binh la (chua tinh min va max)', sum/len(salary))

