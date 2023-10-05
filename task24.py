# import unittest
# import string
# from random import randint

# class Test_Case(unittest.TestCase):
#     def test_one(self):
#         self.assertIn(10, [5, 7, 8, 10], "Test 1 => 10 Is Found In This List [5, 7, 8, 10]")
#     def test_two(self):
#         self.assertEqual(type(10), int, "Test 2 => The Type Of 10 Is Int")
#     def test_three(self):
#         self.assertTrue(100, "Test 3 => Number 100 Return True")
#     def test_four(self):
#         self.assertFalse([], "Test 4 => Empty List [] Return False")
#     def test_five(self):
#         self.assertGreaterEqual(100, 90, "Test 5 => 100 Is Larger Than Or Equal 90")

# if __name__ == "__main__":
#     unittest.main()

# def serial_numbers():
#     count = 14
#     all_chars = string.ascii_letters + string.digits
#     chars_len = len(all_chars)
#     random_list = []
#     while count > 0:
#         random_char = randint(0, chars_len -1)
#         random_list.append(all_chars[random_char])
#         if len(random_list) == 4:
#             random_list.append("-")
#         elif len(random_list) == 9:
#             random_list.append("-")
#         elif len(random_list) == 16:
#             break
#         count -= 1
#     return "".join(random_list)

# print(serial_numbers())
