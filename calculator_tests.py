from calculator import Calculator

class Tests:
    @staticmethod
    def given_empty_string_when_calculating_then_return_zero():
        # Given
        input_str = ""
        expected_result = 0

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @staticmethod
    def given_single_number_when_calculating_then_return_number():
        # Given
        input_str = "5"
        expected_result = 5

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @staticmethod
    def given_two_numbers_separated_by_comma_when_calculating_then_return_their_sum():
        # Given
        input_str = "3,4"
        expected_result = 7

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @staticmethod
    def given_two_numbers_separated_by_newline_when_calculating_then_return_their_sum():
        # Given
        input_str = "3\n4"
        expected_result = 7

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @staticmethod
    def given_three_numbers_separated_by_comma_or_newline_when_calculating_then_return_their_sum():
        # Given
        input_comma = "1,2,3"
        expected_comma_result = 6

        input_newline = "1\n2\n3"
        expected_newline_result = 6

        input_mixed = "1,2\n3"
        expected_mixed_result = 6

        # When
        result_comma = Calculator.calculate(input_comma)
        result_newline = Calculator.calculate(input_newline)
        result_mixed = Calculator.calculate(input_mixed)

        # Then
        assert result_comma == expected_comma_result, f"Expected {expected_comma_result}, but got {result_comma}"
        assert result_newline == expected_newline_result, f"Expected {expected_newline_result}, but got {result_newline}"
        assert result_mixed == expected_mixed_result, f"Expected {expected_mixed_result}, but got {result_mixed}"

    @staticmethod
    def given_negative_number_when_calculating_then_throw_exception():
        try:
            # Given
            input_str = "-3,4"

            # When
            Calculator.calculate(input_str)

            # Then
            assert False, "Expected an exception to be thrown for negative numbers."
        except ValueError as ex:
            assert str(ex) == "Negative numbers are not allowed."

    @staticmethod
    def given_numbers_greater_than_1000_when_calculating_then_ignore_them():
        # Given
        input_str = "2,1001,6"
        expected_result = 8

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @staticmethod
    def given_custom_delimiter_when_calculating_then_return_sum():
        # Given
        input_str = "@@1@2@3"
        expected_result = 6

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @staticmethod
    def given_multi_character_delimiter_when_calculating_then_return_sum():
        # Given
        input_str = "[###]1###2###3"
        expected_result = 6

        # When
        result = Calculator.calculate(input_str)

        # Then
        assert result == expected_result, f"Expected {expected_result}, but got {result}"