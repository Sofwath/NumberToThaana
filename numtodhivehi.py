# -*- coding: utf-8 -*-
#ޮ old code from python 2 migrated to python 3 to be used for part of the dhivehi TTS
# input must be int 

ehbari = ["ސުމެއް","އެއް","ދޭ","ތިން","ހަތަރު","ފަސް","ހަ","ހަތް","އަށް","ނުވަ","ދިހަ","އެގާރަ","ބާރަ","ތޭރަ","ސާދަ","ފަނަރަ","ސޯޅަ","ސަތާރަ","އަށާރަ","އޮނަވިހި"]
dhihabari = ["ސުން","ދިހަ","ވިހި","ތިރީސް","ސާޅީސް","ފަންސާސް","ފަސްދޮޅަސް","ހައްދިހަ","އާހި","ނަވައި"]
sunbari = ["","ހާސް","މިލިޔަން","ބިލިޔަން","ޓްރިލިޔަން"]

def Badhalu(inputString):
    intNum = eval(inputString.strip())
    if intNum < 1000:
        return HaasSub(inputString)
    else:
        return HaasMathi(inputString)

def HaasSub(inputNumber):
    number = int(inputNumber)
    if 0 <= number <= 19:
        return ehbari[number]
    elif 20 <= number <= 99:
        return (dhihabari[int(inputNumber[0])] if inputNumber[-1] == '0'
                 else dhihabari[int(inputNumber[0])] + ' '
                + ehbari[int(inputNumber[1])])
    elif 100 <= number <= 999:
        rem = number % 100
        dig = number // 100
        return (ehbari[dig] + "ސަތޭކަ" if rem == 0 else ehbari[dig]
                + "ސަތޭކަ " + HaasSub(str(rem)))

def constractSun(arrZero):
    z = 0
    while z <= arrZero[::-1]:
    	wrd = HaasSub(str(z)) + " "
        zap = sunbari[lenArr] + " "
        if wrd == " ":
            break
        elif wrd == "ސުން ":
            wrd, zap = "", ""
        resArr.append(wrd + zap)
        lenArr -= 1
    yield resArr

def HaasMathi(inputNumber):
    number = int(inputNumber)
    arrZero = HaasBuri(number)
    lenArr = len(arrZero) - 1
    resArr = []
    res = "".join(constractSun(resArr)).strip()
    if res[-1] == ",": res = res[:-1]
    return res

def HaasBuri(inputNumber):
    number = int(inputNumber)
    arrHaas = []
    while number != 0:
        arrHaas.append(number % 1000)
        number //= 1000
    return arrHaas

strNum = input('integer:\n>> ')
print Badhalu(strNum)
