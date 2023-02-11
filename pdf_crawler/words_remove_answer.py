from docx import Document


infile = "saa_dump.docx"
outfile = "saa_nump_remove_answer.docx"


delete_list = ["Answer: C","Answer: D"]
fin=open(infile,"r", encoding='utf-8')
fout = open(outfile,"w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()