import os
import helper as s
import glob
def preprocess(input_file)
    s.extract_pages(input_file)
    direct = glob.glob("*.pdf")
    for i in direct:
        s.add_class_teacher_sign(i)
        s.add_principal_sign(i)
    all = glob.glob("*.pdf")
    want = glob.glob("*_f*")
    for i in want:
        all.remove(i)
    for j in all:
        os.remove(j)
    for k in want:
        s.encrypt(k)
    all = glob.glob("*.pdf")
    want = glob.glob("*_E*")
    for l in want:
        all.remove(l)
    for t in all:
        os.remove(t)

