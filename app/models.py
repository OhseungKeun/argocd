from django.db import models
from django.contrib.auth.models import User

# 유저 포인트 조회
class UserPoint(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} - {self.balance}P"

# --- 카테고리별 모의고사 ---
class QuizCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = "quiz_category"
    def __str__(self):
        return self.name

# --- 각 문제 ---
class Quiz(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    choice1 = models.CharField(max_length=100)
    choice2 = models.CharField(max_length=100)
    choice3 = models.CharField(max_length=100)
    choice4 = models.CharField(max_length=100)
    answer = models.IntegerField()  # 1~4 정답 번호

    class Meta:
        db_table = 'quiz_question'
    def __str__(self):
        return f"[{self.category.name}] {self.question}"

# --- 유저별 모의고사 기록 ---
class UserExamRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)  # 통과 여부
    score = models.IntegerField(default=0)

    class Meta:
        db_table = "user_exam_record"
        unique_together = ('user', 'category')  # ✅ 카테고리별 중복 통과 방지

    def __str__(self):
        return f"{self.user.username} - {self.category.name}: {'통과' if self.passed else '미통과'}"