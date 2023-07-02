class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def caluculate_bmi(self):
        # bmiを計算するメソッド
        return self.weight / ((self.height**2))


# BMIクラスのインスタンス化
tanaka_bmi = BMI(height=1.80, weight=67.0)
sasaki_bmi = BMI(height=1.50, weight=77.0)
print(tanaka_bmi.height)
print(sasaki_bmi.weight)

print(tanaka_bmi.caluculate_bmi())
print(sasaki_bmi.caluculate_bmi())
