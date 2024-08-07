class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        dic = {
            0: '',
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        def get_3_digits(n: int):
            ans = []
            a3 = n // 100
            if a3 > 0:
                ans.append(f'{dic[a3]} {dic[100]}')
            a12 = n % 100
            if a12 >= 20:
                a2, a1 = a12 - a12%10, a12%10
                ans.append(f'{dic[a2]} {dic[a1]}'.rstrip())
            else:
                ans.append(dic[a12])
            return ' '.join(ans).rstrip()

        ans = []
        b = num // 1000000000
        if b > 0:
            ans.append(f'{get_3_digits(b)} {dic[1000000000]}')
        m = (num % 1000000000) // 1000000
        if m > 0:
            ans.append(f'{get_3_digits(m)} {dic[1000000]}')
        t = (num % 1000000) // 1000
        if t > 0:
            ans.append(f'{get_3_digits(t)} {dic[1000]}')
        r = num % 1000
        if r > 0:
            ans.append(f'{get_3_digits(r)}')

        return ' '.join(ans)