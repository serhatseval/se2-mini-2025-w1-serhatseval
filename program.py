from calculator_tests import Tests

Tests.given_empty_string_when_calculating_then_return_zero()
Tests.given_single_number_when_calculating_then_return_number()
Tests.given_two_numbers_separated_by_comma_when_calculating_then_return_their_sum()
Tests.given_two_numbers_separated_by_newline_when_calculating_then_return_their_sum()
Tests.given_three_numbers_separated_by_comma_or_newline_when_calculating_then_return_their_sum()
Tests.given_negative_number_when_calculating_then_throw_exception()
Tests.given_numbers_greater_than_1000_when_calculating_then_ignore_them()
Tests.given_custom_delimiter_when_calculating_then_return_sum()
