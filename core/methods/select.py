#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
_____, ___
   '+ .;
    , ;
     .

       .
     .;.
     .;
      :
      ,


┌─[Vailyn]─[~]
└──╼ VainlyStrain
"""


from core.colors import color
from core.methods.print import listprint, print_techniques
from core.variables import rce
from core.variables import payloadlist as totalpayloadlist


def select(payloadlist, nullbytes=False, wrappers=False, nosploit=False):
    """
    select specific payloads or nullbytes for phase 2
    @params:
        payloadlist - payloads or nullbytes found in phase 1
    """
    # filter duplicates
    payloadlist = list(set(payloadlist))
    if nullbytes:
        print("\n{0}[+]{1}{2} {3:{4}}{1}{0}|{1}".format(
            color.RD,
            color.END,
            color.O,
            len(payloadlist),
            len(str(len(totalpayloadlist))),
        ) + " Operative nullbytes:")
    elif wrappers:
        print("\n{0}[+]{1}{2} {3:{4}}{1}{0}|{1}".format(
            color.RD,
            color.END,
            color.O,
            len(payloadlist),
            len(str(len(totalpayloadlist))),
        ) + " Operative PHP wrappers:")
    else:
        print("\n{0}[+]{1}{2} {3:{4}}{1}{0}|{1}".format(
            color.RD,
            color.END,
            color.O,
            len(payloadlist),
            len(str(len(totalpayloadlist))),
        ) + " Operative payloads:")

    listprint(payloadlist, nullbytes, wrappers)
    invalid = True
    while invalid:
        if not nosploit:
            payloads = input(
                "{0}[?]{1}{3}{4}{1}{0}|{1}{5}{0} └──{1} {2}{6}{1} :> ".format(
                    color.RD, color.END, color.CURSIVE, color.O,
                    " Payloads", "Select indices\n", "comma-separated",
                )
            )
            try:
                if payloads.strip().lower() == "a":
                    return payloadlist
                elif (
                    (nullbytes or wrappers)
                    and payloads.strip().lower() == "n"
                ):
                    return []
                selected = [
                    payloadlist[int(i.strip())] for i in payloads.split(",")
                ]
                invalid = False
            except Exception:
                pass
        else:
            selected = []
            invalid = False
    return selected


def select_techniques():
    """
    select techniques to use in RCE module
    @return:
        selected techniques, as a list
    """
    techniques = []
    invalid = True
    print_techniques()
    while invalid:
        selected = input(
            "{0}[?]{1}{3}{4}{1}{0}|{1}{5}{0} └──{1} {2}{6}{1} :> ".format(
                color.RD, color.END, color.CURSIVE, color.O,
                " Techniques", "Select indices\n", "comma-separated",
            )
        )
        try:
            error = False
            if selected.strip().lower() == "a":
                return list(range(1, len(rce.items()) + 1))
            for i in selected.split(","):
                technique = int(i.strip())
                if technique not in range(1, len(rce.items()) + 1):
                    error = True
                elif technique not in techniques:
                    techniques.append(technique)
            if techniques and not error:
                invalid = False
            else:
                techniques = []
        except Exception:
            pass

    return techniques
