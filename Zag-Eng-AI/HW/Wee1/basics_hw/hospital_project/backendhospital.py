class BackEnd:
    def __init__(self, test_data=None):
       
        self.patients = {}

        if test_data:
            for spec, name, status in test_data:
                self.add_patient(spec, name, status)

    def add_patient(self, specialization, name, status):
        if specialization not in self.patients:
            self.patients[specialization] = {0: [], 1: [], 2: []}

        self.patients[specialization][status].append(name)

    def get_next_patient(self, specialization):
        if specialization not in self.patients:
            return None

        for status in [2, 1, 0]:  
            if self.patients[specialization][status]:
                return self.patients[specialization][status].pop(0)

        return None

    def remove_patient(self, specialization, name):
        if specialization not in self.patients:
            return False

        for status in [0, 1, 2]:
            if name in self.patients[specialization][status]:
                self.patients[specialization][status].remove(name)
                return True

        return False

    def get_all_patients(self):
        return self.patients
