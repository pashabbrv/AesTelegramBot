from dotenv import load_dotenv
import os

load_dotenv()


to_start = '[В начало]'
back = '[Назад]'
education = {
    'Бакалавриат': [
        'Промышленная электроника'
    ],
    'Магистратура': [
        'Силовая микроэлектроника', 
        'Перспективные силовые преобразователи', 
        'Разработка электронных приборов и систем инерциальной навигации', 
        'Системы и технологии радиомониторинга', 
        'Автоматизация и дигитализация технологических процессов', 
        'Промышленные лазеры', 
        'Системы автоматизированного проектирования микроэлектроники', 
        'Управление проектами внедрения цифровых двойников промышленных систем', 
        'Конструирование и технологии производства элементов и устройств радиоэлектроники', 
        'Системы и технологии технического зрения'
    ]
}
questions = [
    'Узнать больше о программе',
    'Чем обучение в ПИШ отличается от обычных факультетов',
    'Правила приема в ПИШ',
    'Вступительные испытания',
    'Сроки приема документов',
    'Количество бюджетных мест',
    'Стоимость обучения'
]
question_recipient = {
    'Менеджер образовательной программы': os.getenv('RECIPIENT_1'),
    'Дирекция ПИШ': os.getenv('RECIPIENT_2')
}