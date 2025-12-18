import math
import statistics

def get_numbers():
    n = int(input("How many numbers do you want to enter? : "))
    nums = []
    for i in range(n):
        nums.append(float(input(f"Enter number {i+1}: ")))
    return nums

def scientific_calculator():
    while True:
        print("\n====== SCIENTIFIC CALCULATOR ======")
        print("1. Addition (n numbers)")
        print("2. Subtraction (n numbers)")
        print("3. Multiplication (n numbers)")
        print("4. Division (n numbers)")
        print("5. Power (a^b)")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Trigonometry")
        print("9. Statistics")
        print("10. Exit")

        choice = input("Select an option (1-10): ")

        # -------- BASIC OPERATIONS --------
        if choice == '1':
            nums = get_numbers()
            print("Result:", sum(nums))

        elif choice == '2':
            nums = get_numbers()
            result = nums[0]
            for n in nums[1:]:
                result -= n
            print("Result:", result)

        elif choice == '3':
            nums = get_numbers()
            result = 1
            for n in nums:
                result *= n
            print("Result:", result)

        elif choice == '4':
            nums = get_numbers()
            result = nums[0]
            try:
                for n in nums[1:]:
                    result /= n
                print("Result:", result)
            except ZeroDivisionError:
                print("❌ Error: Division by zero")

        # -------- SCIENTIFIC --------
        elif choice == '5':
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", math.pow(a, b))

        elif choice == '6':
            x = float(input("Enter number: "))
            if x >= 0:
                print("Result:", math.sqrt(x))
            else:
                print("❌ Error: Negative number")

        elif choice == '7':
            x = float(input("Enter number: "))
            base = input("Enter base (10/e): ").lower()
            if x > 0:
                if base == 'e':
                    print("Result:", math.log(x))
                else:
                    print("Result:", math.log10(x))
            else:
                print("❌ Error: Log of non-positive number")

        # -------- TRIGONOMETRY --------
        elif choice == '8':
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print("sin:", math.sin(rad))
            print("cos:", math.cos(rad))
            print("tan:", math.tan(rad))

        # -------- STATISTICS --------
        elif choice == '9':
            nums = get_numbers()
            print("Mean:", statistics.mean(nums))
            print("Median:", statistics.median(nums))
            print("Standard Deviation:", statistics.stdev(nums))

        elif choice == '10':
            print("👋 Exiting Calculator")
            break

        else:
            print("❌ Invalid choice")

# Run calculator
scientific_calculator()
