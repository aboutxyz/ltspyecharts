from pyecharts import Bar

voyagename = ['CAT','NEAX','PAN NKT1','SITC NJ1','SITC NA1','SCT', 'NT1','ST2','CPS','CPF','CHS','CTI','EASNSP']

CATV = [314,67,406,338,188,86,120,101]
NEAXV = [147,63,191,135,146,410,340,468]
NKT1V = [533,282,427,500,295,426,543,430]
NJ1V = [259,99,219,306,272,247,274,270]
NA1V = [130,100,157,219,176,172,236,163]
SCTV = [619,592,616,1144,661,535,946,630]
NT1V = [126,142,214,162,218,133,231,150]
ST2V = [4,0,0,0,0,94,0,0]
CPSV = [1623,556,1477,1822,1406,1071,1391,1272]
CPFV = [965,144,762,784,986,673,916,1078]
CHSV = [296,149,519,444,431,507,386,432]
CTIV = [185,52,153,166,175,30,91,57]
EASNSPV = [44,44,82,78,80,100,77,66]

attr = ["{}月".format(i) for i in range(1,13)]
bar = Bar("按月统计各航线出货量")
bar.add("CAT",attr, CATV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NEAX",attr, NEAXV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NKT1",attr, NKT1V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("SCT",attr, SCTV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NA1",attr, NA1V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("NT1",attr, NT1V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("ST2",attr, ST2V, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CPS",attr, CPSV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CPF",attr, CPFV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CHS",attr, CHSV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("CTI",attr, CTIV, mark_line = ["average"], mark_point = ["max","min"])
bar.add("EASNSP",attr, EASNSPV, mark_line = ["average"], mark_point = ["max","min"])

bar