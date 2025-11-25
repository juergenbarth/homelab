#!/todo/bin/python3
# -*- coding: utf-8 -*-
import sys
from escpos import *

printer_ip = sys.argv[1]
title = sys.argv[2]
text = sys.argv[3].replace("<br>", '\n')
subheader = sys.argv[4]
due_date = sys.argv[5]
added_date = sys.argv[6]

""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T20IV) """
Epson = printer.Network(printer_ip, profile="TM-T20II")
Epson.set(align='center', double_width=True, double_height=True)
Epson.textln(title)
Epson.textln(subheader)
Epson.textln(due_date)
Epson.textln("----------")
Epson.set(align='left', normal_textsize=True)
Epson.textln(text)
Epson.ln(1)
Epson.text(added_date)
Epson.cut()
