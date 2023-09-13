class Utils:
    def reversed(number):
        reverse = 0
        if not(isinstance(number, int)):
            return "incorrect data type entered to reversed function"
        
        while number > 0:
            reverse = reverse + number % 10
            number = number // 10
            if number > 0:
                reverse = reverse * 10
        return reverse

    def formatter(number):
        if not(isinstance(number, int)):
            return "incorrect data type entered to reversed function"

        binary = bin(number)
        octo = oct(number)

        return (binary, octo)
    

