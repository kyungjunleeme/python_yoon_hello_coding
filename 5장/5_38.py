with open("info.txt", "r") as file:
    for line in file:
        # 변수를 선언합니다.
        (name, weight, height) = line.strip().split(",")
        # 데이터가 문제 없는지 확인합니다: 문제가 있으면 지나감
        if (not name) or (not weight) or (not height):
            continue
        # 결과를 계산합니다.

        # bmi 구하는 방법
        # height = height * 0.01
        # bmi = weight / (height * height)
        
        # error1
        # TypeError: can't multiply sequence by non-int of type 'float'
        # abc * 0.01 (x) 이런 오류로 보임
        # abc에 어떤 데이터를 입력받은 후에 0.01만큼을 곱해서 계산하고 싶었음. 하지만 오류 발생
        # float(abc) * 0.01 (o)
        # error2
        # SyntaxError: “can't assign to function call”
        # float(height) = float(hegit) * 0.01 (x)변수선언 시에는 타입 지정을 변수명에 포함시키지 않음. 그래서 오류 남
        # height = float(height) * 0.01 (o)

        bmi = int(weight) / ((int(height)/100) * (int(height)/100))  
        
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"
        # 출력합니다. # tab 으로 구분해서 보는게 보기 좋으므로 난 '\n' 대신 '\t' 사용
        print('\t'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()