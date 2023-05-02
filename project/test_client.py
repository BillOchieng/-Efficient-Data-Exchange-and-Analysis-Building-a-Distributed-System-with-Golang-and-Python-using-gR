import os
import subprocess
import time
import unittest

import requests


class TestClient(unittest.TestCase):
    def setUp(self):
        self.server_process = subprocess.Popen(
            ["python", "server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # wait for the server to start listening
        time.sleep(1)

    def tearDown(self):
        self.server_process.terminate()
        self.server_process.wait()
        for f in os.scandir():
            if f.name.endswith(".log") and f.is_file():
                with open(f, "r") as logfile:
                    print(logfile.read())

    def test_welcome(self):
        response = requests.get("http://localhost:8080/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome", response.text)

    def test_contact(self):
        response = requests.get("http://localhost:8080/contact")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Contact", response.text)

    def test_submit(self):
        response = requests.post(
            "http://localhost:8080/submit",
            data={
                "name": "John Doe",
                "email": "john.doe@example.com",
                "message": "Hello, World!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Thank you", response.text)

    def test_users(self):
        p = subprocess.Popen(
            ["python", "client.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        stdout, stderr = p.communicate(b"Aidan\n")
        self.assertIn(b"Name: Aidan", stdout)
        self.assertIn(b"Email: aidan@example.com", stdout)
        self.assertIn(b"Phone: 513-495-1234", stdout)
        self.assertNotIn(b"No user found", stdout)
        p.stdin.write(b"quit\n")
        p.stdin.close()
        p.wait()
        self.assertEqual(p.returncode, 0)


if __name__ == "__main__":
    unittest.main()
