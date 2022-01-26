import unittest
from student_profile import Profile


class ProfileTest(unittest.TestCase):

    def test_create_profile(self):
        new_profile = Profile()

        new_profile.set_password("newPassword")
        new_profile.set_last_name("Okoroafor")
        new_profile.set_first_name("Kelechi")
        new_profile.set_phone_number("08082167764")

        self.assertIsNotNone(new_profile)  # add assertion here


if __name__ == '__main__':
    unittest.main()
