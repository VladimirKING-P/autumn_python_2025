# Модель учебных материалов
#todo: Создайте иерархию классов для представления различных типов учебных материалов.
# Требования: Базовый класс LearningMaterial:
# Свойства: title, author, duration_minutes
# Методы:
# display_info() - выводит основную информацию
# get_difficulty() - возвращает сложность материала (должен быть переопределен в дочерних классах)
# Дочерние классы:
# VideoLesson:
# Дополнительные свойства: video_quality, subtitles_available
# Сложность: "Средняя"
# Article:
# Дополнительные свойства: word_count, reading_level
# Сложность: рассчитывается как word_count / 1000 (легкая если <1, средняя 1-3, сложная >3)
# Quiz:
# Дополнительные свойства: questions_count, passing_score
# Сложность: "Высокая" если passing_score > 80, иначе "Средняя"


class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.author = author
        self.duration_minutes = duration_minutes

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Длительность: {self.duration_minutes} мин")

    def get_difficulty(self):
        raise NotImplementedError("Метод get_difficulty должен быть переопределён в дочернем классе")


class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        super().__init__(title,author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available

    def get_difficulty(self):
        return "Средняя"

    def display_info(self):
        super().display_info()
        print(f"Качество видео: {self.video_quality}")
        print(f"Субтитры: {'есть' if self.subtitles_available else 'нет'}")

class Article(LearningMaterial):
    def __init__(self, title, author, duration_minutes, word_count, reading_level):
        super().__init__(title, author, duration_minutes)
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self):
        difficulty_ratio = self.word_count / 1000
        if difficulty_ratio < 1:
            return "Лёгкая"
        elif 1 <= difficulty_ratio <= 3:
            return "Средняя"
        else:
            return "Сложная"

    def display_info(self):
        super().display_info()
        print(f"Уровень чтения{self.reading_level}")
        print(f"Количество слов: {self.word_count}")

class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes, questions_count, passing_score):
        super().__init__(title, author, duration_minutes)
        self.questions_count = questions_count
        self.passing_score = passing_score

    def get_difficulty(self):
        return "Высокая" if self.questions_count > 80 else "Средняя"

    def display_info(self):
        super().display_info()
        print(f"Количество вопросов: {self.questions_count}")
        print(f"Проходной балл: {self.passing_score}%")


materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 1200, 2500, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 10, 75)
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")


