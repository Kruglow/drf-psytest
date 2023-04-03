from .models import Test, Question, Interpretation

def create_test_data():
    test = Test.objects.create(
        name='Тест на знание английского языка',
        description='Тест для проверки уровня знания английского языка',
        questions=[
            {
                'text': 'Какой язык является родным для Англии?',
                'options': {
                    'a': 'Испанский',
                    'b': 'Английский',
                    'c': 'Французский',
                    'd': 'Немецкий',
                }
            },
            {
                'text': 'Какой глагол используется для обозначения действия "есть"?',
                'options': {
                    'a': 'Eat',
                    'b': 'Drink',
                    'c': 'Sleep',
                    'd': 'Jump',
                }
            },
            {
                'text': 'Как переводится слово "computer"?',
                'options': {
                    'a': 'Компьютер',
                    'b': 'Автомобиль',
                    'c': 'Мороженое',
                    'd': 'Книга',
                }
            },
        ],
        interpretations=[
            {
                'min_score': 0,
                'max_score': 1,
                'text': 'Вы не знаете английский язык'
            },
            {
                'min_score': 2,
                'max_score': 2,
                'text': 'Вы немного знаете английский язык'
            },
            {
                'min_score': 3,
                'max_score': 3,
                'text': 'Вы отлично знаете английский язык'
            },
        ]
    )


    for i, question_data in enumerate(test.questions):
        question = Question.objects.create(
            test=test,
            text=question_data['text'],
            options=question_data['options']
        )

    for interpretation_data in test.interpretations:
        interpretation = Interpretation.objects.create(
            test=test,
            min_score=interpretation_data['min_score'],
            max_score=interpretation_data['max_score'],
            text=interpretation_data['text']
        )

