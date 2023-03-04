def TShirtCheck(numberInShop, sizeInShop, requestNumber, requestSize):
    if numberInShop < requestNumber:
        return False
    else:
        requestSize_Num = []
        sizeInShop_Num = []
        requestSize = requestSize.split(" ")
        sizeInShop = sizeInShop.split(" ")
        for i in range(0, len(requestSize)):
            count = 1
            for j in range(0, len(requestSize[i])):
                if requestSize[i][j] == "X":
                    count += 1
            requestSize_Num.append(count)

        for i in range(0, len(sizeInShop)):
            count = 1
            for j in range(0, len(sizeInShop[i])):
                if sizeInShop[i][j] == "X":
                    count += 1
            sizeInShop_Num.append(count)

        for i in range(len(requestSize_Num)):
            if "L" in requestSize[i]:
                requestSize_Num[i] *= 1.1
            elif "M" in requestSize[i]:
                requestSize_Num[i] *= 1
            elif "S" in requestSize[i]:
                requestSize_Num[i] *= 0.9

        for i in range(len(sizeInShop_Num)):
            if "L" in sizeInShop[i]:
                sizeInShop_Num[i] *= 1.1
            elif "M" in sizeInShop[i]:
                sizeInShop_Num[i] *= 1
            elif "S" in sizeInShop[i]:
                sizeInShop_Num[i] *= 0.9

        sorted(requestSize_Num)
        sorted(sizeInShop_Num)

        # print("requestSize_Num:", requestSize_Num)
        # print("sizeInShop_Num:", sizeInShop_Num)
        checkList = []
        for i in range(0, len(sizeInShop_Num)):
            j = 0
            if sizeInShop_Num[i] >= requestSize_Num[j]:
                j += 1
                checkList.append(True)
            else:
                continue
        
        # print("checklist: ", len(checkList))
        # print("request: ", len(requestSize_Num))
        if len(checkList) >= len(requestSize_Num):
            return True
        else:
            return False

# print(TShirtCheck(5, "XL XXXXXXXXXL XXS M XXS", 4, "L M L XXS"))
# print(TShirtCheck(4, "S S S L", 3, "L M S"))

    