from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class TestUserProgram(StageTest): # создаем списки, которые будут хранить информацию о поступающих данных
    def generate(self, card_answer, description_answer):
        List_answers =[]
        List_definition = []
        card_answers_list = [red, green, blue, grey]
        card_answers_list2 = [read, gren, blu, gray]


    def first_check(self):                                                  # проверяем  тип данных и сверяем есть ли возможные слова в списке возможных ответов
        if (type(card_answer) == str:
            if card_answer in card_answers_list:
                 List_answers.append = card_answer
            if card_answer in card_answers_list2:
                return Check_result.wrong(
                    "ошибка в правописание слова"
                ) 
            else:
                Check_result.wrong(
                    "попробуйте другой вариант ответа"
                ) 
        else:
            return CheckResult.wrong(
                    "Ваш ответ должен описывать цвет карточки"
                )

        return card_answer

    def second_check(self):            # проверяем  тип данных и сверяем есть ли возможные слова в списке возможных ответов уже в описании карточки
        if (type(description_answer) == str:
            if description_answer in card_answers_list:
                List_answers.append = description_answer

            if description_answer in card_answers_list2:
                return Check_result.wrong(
                    "ошибка в правописание слова"
                )
            else:
                return Check_result.wrong(
                    "попробуйте другой вариант ответа"
                ) 
        else:
                return CheckResult.wrong(
                    "Ваш ответ должен описывать содержание карточки"
                )


    def third_check(self):
        if card_answer in List_answers:
            return check_result.wrong(
                'этот цвет уже использован'
            )
        if card_answer in card_answers_list2:
            return CheckResult.wrong(
                "Проверьте на наличие ошибок в правописании"
            )
        else:
            return CheckResult.wrong(
                "Попробуйте что-нибудь другое"
            )
        elif:
            List_answers.append = card_answer

    def fourt_check(self):
        if description_answer in List_answers:
            return check_result.wrong(
                'этот цвет уже использован'
            )
        if description_answer in card_answers_list2:
            return Check_result.wrong(
                    "ошибка в правописание слова"
                )
        else:
            return Check_result.wrong(
                    "попробуйте другой вариант ответа"
                ) 
        elif:
            List_answers = card_answer

    def fifth_check(self):
        if (card_answer.index('input  word') - card_answer('require word')) == 1:
            return check_result.true(
                "Ваш ответ верный"
            )
        else:
            return check_result.wrong(
                "Ваш ответ неверен"
            )



        
