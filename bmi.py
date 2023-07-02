class BMI:
    def __init__(self, height, weight):
        self.value = weight / (height**2)
        if not (10 <= self.value <= 40):
            raise ValueError("BMIの正常値を超えています")

    def __str__(self):
        return f"{self.value:.2f}"


# BMIクラスのインスタンス化
tanaka_bmi = BMI(height=1.80, weight=67.0)
sasaki_bmi = BMI(height=1.50, weight=77.0)
bob_bmi = BMI(height=1.70, weight=750000.0)

print(tanaka_bmi)
