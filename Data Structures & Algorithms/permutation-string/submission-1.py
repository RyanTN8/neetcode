class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        table1 = {}
        table2 = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] in table1:
                table1[s1[i]] += 1
            else:
                table1[s1[i]] = 1

            if s2[i] in table2:
                table2[s2[i]] += 1
            else:
                table2[s2[i]] = 1
        print(table1)
        print(table2)
        if table1 == table2:
            return True

        for i in range(len(s2) - len(s1)):
            l = s2[i]
            r = s2[i + len(s1)]
            table2[l] -= 1
            if table2[l] == 0:
                table2.pop(l)
            if r in table2:
                table2[r] += 1
            else:
                table2[r] = 1
            print(table2)
            if table1 == table2:
                return True
        return False


            