class Doctor:
    def __init__(self, name, speciality):
        self._name = name
        self.speciality = speciality
        self.patients = []

    def assign_patient(self, patient):
        return self.patients.append(patient)

    def get_assigned_patient(self):
        return self.patients


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.assigned_doctor = None

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor

    def get_assigned_doctor(self):
        return self.assigned_doctor


if __name__ == "__main__":
    doctor1 = Doctor("Dr. Smith", "Cardiologist")
    doctor2 = Doctor("Dr. Johnson", "Neurologist")
    patient1 = Patient("Alice", 30)
    patient3 = Patient("Eve", 55)

    doctor1.assign_patient(patient1)
    doctor2.assign_patient(patient3)

    print(f"{doctor1.name}'s assigned patients:")
    for patient in doctor1.get_assigned_patient():
        print(f"- {patient.name}")

    print(f"\n{doctor2.name}'s assigned patients:")
    for patient in doctor2.get_assigned_patient():
        print(f"- {patient.name}")
