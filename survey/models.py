from django.db import models
from django import forms

# Part 1: General Information
class GeneralInformation(models.Model):
    business_name = models.CharField(max_length=255, verbose_name="Tên doanh nghiệp")
    year_established = models.PositiveIntegerField(verbose_name="Năm thành lập")
    business_address = models.CharField(max_length=255, verbose_name="Địa chỉ của Doanh nghiệp")
    respondent_name = models.CharField(max_length=255, verbose_name="Họ và tên người trả lời")
    email = models.EmailField(verbose_name="Địa chỉ e-mail (thư điện tử)")
    phone_number = models.CharField(max_length=20, verbose_name="Số điện thoại")
    
    def __str__(self):
        return self.business_name

# Part 2: Business Type and Size
class BusinessType(models.Model):
    TYPES = [
        ("private", "Tư nhân trong nước"),
        ("foreign", "Đầu tư nước ngoài"),
        ("state", "Cổ phần vốn góp của nhà nước (trên 50% vốn điều lệ)"),
        ("other", "Loại hình khác"),
    ]
    type = models.CharField(max_length=50, choices=TYPES, verbose_name="Loại hình doanh nghiệp")

class BusinessField(models.Model):
    FIELDS = [
        ("agriculture", "Nông nghiệp, lâm nghiệp và thủy sản"),
        ("mining", "Khai khoáng"),
        ("manufacturing", "Chế biến và chế tạo"),
        ("utilities", "Sản xuất và phân phối điện, nước"),
        ("construction", "Xây dựng"),
        ("retail", "Bán buôn và bán lẻ; sửa chữa xe có động cơ"),
        ("transport", "Vận tải kho bãi"),
        ("hospitality", "Dịch vụ lưu trú và ăn uống"),
        ("ict", "Thông tin và truyền thông"),
        ("finance", "Hoạt động ngân hàng, tài chính và bảo hiểm"),
        ("science", "Hoạt động chuyên môn, KHCN"),
        ("education", "Giáo dục và đào tạo"),
        ("health", "Y tế và hoạt động trợ giúp xã hội"),
        ("arts", "Nghệ thuật, vui chơi, giải trí"),
        ("other", "Ngành nghề khác"),
    ]
    field = models.CharField(max_length=50, choices=FIELDS, verbose_name="Lĩnh vực kinh doanh")

class BusinessSize(models.Model):
    SIZES = [
        ("<5", "< 5 người"),
        ("5-9", "5 - 9 người"),
        ("10-49", "10 - 49 người"),
        ("50-199", "50 - 199 người"),
        ("200-299", "200 - 299 người"),
        ("300-999", "300 - 999 người"),
        ("1000-4999", "1000 - 4999 người"),
        (">5000", "5000 người"),
    ]
    size = models.CharField(max_length=20, choices=SIZES, verbose_name="Quy mô lao động")

# Part 3: Strategy and Operation
from django.db import models

class StrategyOperation(models.Model):
    # Define constants for the Likert scale
    LIKERT_CHOICES = [(i, str(i)) for i in range(1, 8)]

    vision = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Tầm nhìn của Doanh nghiệp', default='1')
    mission = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Sứ mệnh của Doanh nghiệp', default='1')
    strategic_goals = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Mục tiêu chiến lược của Doanh nghiệp', default='1')
    technology_absorption = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Khả năng hấp thụ công nghệ mới', default='1')
    r_and_d_spending = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Chi tiêu cho nghiên cứu và phát triển', default='1')
    competitive_advantage = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Bản chất của lợi thế cạnh tranh', default='1')
    value_chain = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Độ rộng của chuỗi giá trị', default='1')
    innovation_capacity = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Năng lực đổi mới sáng tạo', default='1')
    operational_process = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Quy trình vận hành', default='1')
    technology_use = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Sử dụng công nghệ', default='1')
    performance_measurement = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Hiệu quả đo lường', default='1')
    marketing_level = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Mức độ tiếp thị', default='1')
    customer_service = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Chăm sóc khách hàng', default='1')
    core_values = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Xác định giá trị cốt lõi', default='1')
    core_values_building = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Xây dựng giá trị cốt lõi', default='1')
    organizational_chart = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Sơ đồ tổ chức', default='1')
    job_description = models.CharField(max_length=1, choices=LIKERT_CHOICES, verbose_name='Mô tả công việc', default='1')

    # Timestamp for when the response was submitted
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"StrategyOperation {self.id}"



# Part 4: General Feedback
class GeneralFeedback(models.Model):
    feedback = models.TextField(verbose_name="Góp ý chung")

class Business(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)