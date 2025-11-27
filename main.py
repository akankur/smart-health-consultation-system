from database import create_database, save_record, get_all_records, export_to_csv
from consultation import predict_diseases
from diseases_data import diseases
from colorama import Fore, Style, init

init(autoreset=True)

def new_consultation():
    print("\n🩺 NEW HEALTH CONSULTATION\n")

    name = input("Enter your name: ")
    symptoms = input("Enter your symptoms (comma separated): ").lower().split(",")

    top_diseases = predict_diseases(symptoms, top_n=3)

    if top_diseases:
        print("\n===== Consultation Result =====")
        for idx, (disease, matches) in enumerate(top_diseases, start=1):
            details = diseases[disease]

            # Color severity
            severity = details['severity']
            if severity.lower() == "high":
                severity_color = Fore.RED + severity + " ⚠️"
            elif severity.lower() == "medium":
                severity_color = Fore.YELLOW + severity
            else:
                severity_color = Fore.GREEN + severity

            print(f"\n{idx}. Predicted Disease: {Fore.CYAN + disease}")
            print(f"   Severity Level: {severity_color}")
            print(f"   Doctor Recommended: {Fore.MAGENTA + details['doctor']}")
            print(f"   Advice: {Fore.WHITE + details['advice']}")

        # Save only best prediction (index 0)
        best_disease = top_diseases[0][0]
        best_details = diseases[best_disease]

        save_record(
            name,
            ", ".join([s.strip() for s in symptoms]),
            best_disease,
            best_details["severity"],
            best_details["doctor"]
        )

        print("\n💾 Consultation saved successfully!")

    else:
        print("\n❌ Could not identify the disease with given symptoms.")


def view_consultations():
    print("\n📄 CONSULTATION HISTORY\n")

    records = get_all_records()

    if not records:
        print("No past consultations found.")
        return

    for row in records:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Symptoms: {row[2]}")
        print(f"Disease: {row[3]}")
        print(f"Severity: {row[4]}")
        print(f"Doctor: {row[5]}")
        print("--------------------------------------------------")


def export_data():
    export_to_csv("consultations.csv")


def main_menu():
    create_database()

    while True:
        print("\n==============================")
        print("🩺 SMART HEALTH CONSULTATION")
        print("==============================")
        print("1. New Consultation")
        print("2. View Past Consultations")
        print("3. Export Consultations to CSV")
        print("4. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            new_consultation()
        elif choice == "2":
            view_consultations()
        elif choice == "3":
            export_data()
        elif choice == "4":
            print("\n👋 Exiting... Stay Healthy!")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
