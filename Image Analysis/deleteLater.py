import re

#text = " we have event dr. mohammed ahmed ali one two three weriwejrweiorwerjiowe wperwejroi 234234"
text="يقدمها المحاضر / أ. رامى علاء الدين شحاتة"
text = "يسر عمادة شؤون المكتبات بجامعة الملك عبدالعزيز تقديم ورشة عمل بعنوان: TURNITIN& ITHENTICATE يقدمها المحاضر / أ. رامى علاء الدين شحاتة أونلاين - عبر البلاك بورد رئيس قسم قواعد المعلومات والحوسبة في جامعة البترا سابقا المدير الإقليمي لشركة تكنوليدج في السمودية والبحرين وبلاد الشام يوم الثلاثاء 1٤٤٣/٣/٣ ه الموافق D) الفئة المستهدفة: أعضاء هيئة التدريس وطلاب وطالبات الدراسات العليا والباحثين والمهتمين للحصول على الشهادة: الدخول بالاسم الثلاي حضور كامل ورشة الهمل @Librarykau Kaulibrary fKaulibrary D0569808352 Kaulib ف عمادة شؤون المكتبات جامعة الملك عبدالعزيز Library@kau.edu.sa"


pattern1=r' د.\s+((?:\w+(?:\s+|$)){2})'
pattern2=r' أ.\s+((?:\w+(?:\s+|$)){2})'


# name=""

# if((re.search(pattern1, text))):
#      print("found 1 ")
#      name = re.search(pattern1, text).group()


# elif((re.search(pattern2, text))):
#      print("found 2 ")
#      name = re.search(pattern2, text).group()
# else:
#     print("no")


# print(name)

date = "٣٤٤٣/٣/٣"



