class Calculator:
    @staticmethod
    def calculate(input_str):
        if not input_str:
            return 0

        custom_delimiter = ','

        if len(input_str) > 2 and input_str[0] == input_str[1]:
            custom_delimiter = input_str[0]
            input_str = input_str[2:]

        delimiters = [custom_delimiter, '\n']
        numbers = []
        for delimiter in delimiters:
            input_str = input_str.replace(delimiter, ',')

        numbers = input_str.split(',')

        sum_total = 0
        for number in numbers:
            if number:
                num = int(number)
                if num < 0:
                    raise ValueError("Negative numbers are not allowed.")
                if num <= 1000:
                    sum_total += num

        return sum_total