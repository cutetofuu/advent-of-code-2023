import re
from calibration_doc import calibration_doc_str

def get_two_digit_num(line):
    new_line = line.replace("nine", "nninee").replace("eight", "eeightt").replace("seven", "ssevenn").replace("six", "ssixx").replace("five", "ffivee").replace("four", "ffourr").replace("three", "tthreee").replace("two", "ttwoo").replace("one", "oonee")

    new_line_2 = new_line.replace("nine", "9").replace("eight", "8").replace("seven", "7").replace("six", "6").replace("five", "5").replace("four", "4").replace("three", "3").replace("two", "2").replace("one", "1")
     
    all_digits = re.findall("\d", new_line_2)

    if (len(all_digits) > 1):
        two_digit_num = int(f"{all_digits[0]}{all_digits[len(all_digits) - 1]}")
    else:
        two_digit_num = int(f"{all_digits[0]}{all_digits[0]}")

    return two_digit_num

def get_calibration_value(calibration_doc):
    calibration_lines = calibration_doc.split("\n")
    calibration_value = 0

    for str in calibration_lines:
        two_digit_num = get_two_digit_num(str)
        calibration_value += two_digit_num

    return calibration_value

print(f"The calibration value is: {get_calibration_value(calibration_doc_str)}")