# func_py_leap_year.py

def func_py_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def test_leap_year():
    years = [1900, 2000, 2024, 2025]
    for y in years:
        print(f"{y} is leap year: {func_py_leap_year(y)}")

if __name__ == "__main__":
    test_leap_year()
