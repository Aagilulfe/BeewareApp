import os
import xml.etree.ElementTree as ET

"""""""""""Student Info"""""""""""

options_path = os.path.dirname(os.path.abspath(__file__)) + "/resources/student_options.xml"
tree = ET.parse(options_path)
root = tree.getroot()

# print(root.find("language").text)

student_language = root.find("language").text
student_level = root.find("level").text
student_UE3_1 = root.find("UE3_1").text
student_UE3_2 = root.find("UE3_2").text

# print(student_language, student_level, student_UE3_1, student_UE3_2)