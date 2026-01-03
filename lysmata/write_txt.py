import os
import datetime


def write_output_to_file(output):
    directory = "output"
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"test_result__{timestamp}.txt"
    file_path = os.path.join(directory, file_name)

    with open(file_path, "w") as file:
        file.write(output)

    print("Risutato riportato su ", file_path)
