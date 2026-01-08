class FrontEnd:
    def menu_options(self):
        print("\nProgram Options:")
        print("1) Add new patient")
        print("2) Print all patients")
        print("3) Get next patient")
        print("4) Remove a patient")
        print("5) Exit")

    def get_choice(self):
        return int(input("Enter your choice (from 1 to 5): "))

    def get_specialization(self):
        return input("Enter specialization: ")

    def get_patient_data(self):
        name = input("Enter patient name: ")
        print("Enter status (0: Normal, 1: Urgent, 2: Super Urgent)")
        status = int(input("Status: "))
        return name, status

    def print_all_patients(self, patients):
        if not patients:
            print("No patients found.")
            return

        for spec, queues in patients.items():
            print(f"\nSpecialization: {spec}")
            print("  Normal:", queues[0])
            print("  Urgent:", queues[1])
            print("  Super Urgent:", queues[2])

    def print_next_patient(self, patient):
        if patient:
            print("Next patient:", patient)
        else:
            print("No patients available.")

    def notify_patient_removed(self, success, name):
        if success:
            print(f"Patient '{name}' removed successfully.")
        else:
            print(f"Patient '{name}' not found.")
