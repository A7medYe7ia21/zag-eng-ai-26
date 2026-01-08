from frontendhospital import FrontEnd
from backendhospital import BackEnd
from test import Test


class HospitalManager:
    def __init__(self):
        test_data = Test.get()
        self.front = FrontEnd()
        self.back = BackEnd(test_data)

    def run(self):
        while True:
            self.front.menu_options()
            choice = self.front.get_choice()

            if choice == 1:
                spec = self.front.get_specialization()
                name, status = self.front.get_patient_data()
                self.back.add_patient(spec, name, status)

            elif choice == 2:
                self.front.print_all_patients(self.back.get_all_patients())

            elif choice == 3:
                spec = self.front.get_specialization()
                patient = self.back.get_next_patient(spec)
                self.front.print_next_patient(patient)

            elif choice == 4:
                spec = self.front.get_specialization()
                name = input("Enter patient name: ")
                success = self.back.remove_patient(spec, name)
                self.front.notify_patient_removed(success, name)

            elif choice == 5:
                print("Exiting system...")
                break

            else:
                print("Invalid choice!")


if __name__ == "__main__":
    manager = HospitalManager()
    manager.run()
