vp = float(input("Digite o valor de VP(total de verdadeiros positivos): "))
fp = float(input("Digite o valor de FP(total de falsos positivos): "))
fn = float(input("Digite o valor de VP(total de falsos negativos: "))
vn = float(input("Digite o valor de VP(total de verdadeiros negativos): "))

n = vp + fp + fn + vn
ag = (vp + vn)/n
precision = vp/(vp + fp)
recall = vp/(vp + fn)
f1 = (2 * precision * recall)/(precision + recall)

print("""
AG: {}
Precision: {}
Recall: {}
F1-Score: {}""".format(ag, precision, recall, f1))