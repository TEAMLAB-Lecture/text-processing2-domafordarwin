#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    """
    인풋으로 받는 스트링에서 숫자만 추출하여 영어 단어로 변환하여 단어들이 연결된 스트링을 반환함
    아래의 요건들을 충족시켜야함
    * 반환하는 단어들은 영어 소문자여야함
    * 단어들 사이에는 띄어쓰기 한칸이 있음
    * 만약 인풋 스트링에서 숫자가 존재하지 않는 다면, 빈 문자열 (empty string)을 반환함

        Parameters:
            input_string (string): 영어로 된 대문자, 소문자, 띄어쓰기, 문장부호, 숫자로 이루어진 string
            ex - "Zip Code: 19104"

        Returns:
            digit_string (string): 위 요건을 충족시킨 숫자만 영어단어로 추출된 string
            ex - 'one nine one zero four'

        Examples:
            >>> import text_processing2 as tp2
            >>> digits_str1 = "Zip Code: 19104"
            >>> tp2.digits_to_words(digits_str1)
            'one nine one zero four'
            >>> digits_str2 = "Pi is 3.1415..."
            >>> tp2.digits_to_words(digits_str2)
            'three one four one five'
    """

    def num_to_char(number): # 숫자를 문자로 변환하는 함수
        char_list=["zero", "one", "two", "three", "foue", "five", "six", "seven", "eight", "nine"]
        x = number
        char_for_num =" "
        
        if x == 0:
            char_for_num = char_list[0]
        elif x == 1:
            char_for_num = char_list[1]
        elif x == 2:
            char_for_num = char_list[2]
        elif x == 3:
            char_for_num = char_list[3]
        elif x == 4:
            char_for_num = char_list[4]
        elif x == 5:
            char_for_num = char_list[5]
        elif x == 6:
            char_for_num = char_list[6]
        elif x == 7:
            char_for_num = char_list[7]
        elif x == 8:
            char_for_num = char_list[8]
        elif x == 9:
            char_for_num = char_list[9]
            
        return char_for_num

    def eliminate_sign(input_string):
        sign_list= ["'", '"', ',', '.', '?', '!', ':', ';', '(',')','-']

        temp = input_string

        for i in sign_list:
            if i in temp:
                temp = temp.replace(i, "")
        return temp

    # 문자열을 소문자로 처리하기
    input_string = input_string.lower()

    # 문장 부호 제거하기

    input_string = eliminate_sign(input_string)

    digit_string = []

    for str in input_string:
        if str.isdigit():
            for i in str:
                digit_string.append(num_to_char(int(i)))
        else:
            continue
    
    digit_string=" ".join(digit_string)
    print(digit_string)   
    return digit_string


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    """
    이 문제에서 첫번째 규칙 'underscore variable' 에서 두번째 규칙 'camelcase variable'으로 변환함
    * 앞과 뒤에 여러개의 'underscore'는 무시해도 된
    * 만약 어떤 변수 이름이 underscore로만 이루어 진다면, 빈 문자열만 반환해도 됨

        Parameters:
            underscore_str (string): underscore case를 따른 스트링

        Returns:
            camelcase_str (string): camelcase를 따른 스트링

        Examples:
            >>> import text_processing2 as tp2
            >>> underscore_str1 = "to_camel_case"
            >>> tp2.to_camel_case(underscore_str1)
            "toCamelCase"
            >>> underscore_str2 = "__EXAMPLE__NAME__"
            >>> tp2.to_camel_case(underscore_str2)
            "exampleName"
            >>> underscore_str3 = "alreadyCamel"
            >>> tp2.to_camel_case(underscore_str3)
            "alreadyCamel"
    """
    camelcase_str = underscore_str

    camelcase_str = camelcase_str.lower()
    camelcase_str = camelcase_str.replace("_", " ")
    camelcase_str = camelcase_str.split()

    # 리스트로 변환된 문자열의 첫 글자를 대문자로 변환하기
    for i in range(len(camelcase_str)):
        if i > 0:
            camelcase_str[i] = camelcase_str[i].capitalize()

    camelcase_str="".join(camelcase_str)

    print(camelcase_str)

    return camelcase_str
'''
test_str = "My number: 010-1234-5678"
test_str2 = "not_Camel_Yet"

digits_to_words(test_str)
to_camel_case(test_str2)
'''
