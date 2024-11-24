import numpy as np


class Activity:
    def __init__(self) -> None:
        self.activities = []
        self.numerical_activities = []

    def display_activities(self):
        print("Daftar Kegiatan:")
        for i, activity in enumerate(self.activities);
            print(f"{i+1}. {activity}")

    def add_activity(self, new_activity):
        self.activities.append(new_activity)

    def convert_to_numerical(self):
        numerical_activities = {
            activity: i for i, activity in enumerate(self.activities)
        }
        self.numerical_activities = numerical_activities

    def generate_input_matrix(self):
        n = len(self.numerical_activities)
        matrix = np.zeros((n, n), dtype=int)

        # Contoh hardcoded hubungan antar kegiatan
        matrix[0][1] = 1  # Kegiatan 1 dihubungkan dengan kegiatan 2
        matrix[1][0] = 1  # Kegiatan 2 dihubungkan dengan kegiatan 3
        matrix[2][0] = 1  # Kegiatan 3 dihubungkan kembali dengan kegiatan 1
        matrix[0][2] = 1  # Kegiatan 1 juga dihubungkan dengan kegiatan 3

        matrix[2][4] = 1
        matrix[4][2] = 1

        matrix[4][3] = 1
        matrix[3][4] = 1

        matrix[3][1] = 1
        matrix[1][3] = 1

        return matrix
