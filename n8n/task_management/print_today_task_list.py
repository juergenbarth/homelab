#!/todo/bin/python3
# -*- coding: utf-8 -*-
import sys
from escpos import *

printer_ip = sys.argv[1]
title = sys.argv[2].replace("<br>", '\n')
weather = sys.argv[3].replace("<br>", '\n')
tasks = sys.argv[4].replace("<br>,", '\n').replace("<br>", '\n')
motd = sys.argv[5].replace("<br>", '\n')

""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T20IV) """
Epson = printer.Network(printer_ip, profile="TM-T20II")
Epson.set(align='center', double_width=True, double_height=True)
Epson.textln(title)
Epson.set(align='center', normal_textsize=True, bold=True)
Epson.textln(weather)
Epson.textln("----------")
Epson.set(align='left', normal_textsize=True)
Epson.textln(tasks)
Epson.textln("----------")
Epson.textln(motd)
Epson.cut()
