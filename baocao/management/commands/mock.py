from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Mock user and aliases'
    RANGE = 5

    def create_bulk_users(self):
        from setmeup.models import PhongBan, Title, NoiNhan
        from user.models import User
        import secrets
        import string

        a = (("Phan Thị Thanh Hà", "Giám Đốc", "Ban Giám đốc"),
             ("Phạm Thị Thanh Yên", "Phó Giám đốc", "Ban Giám đốc"),
             ("Trịnh Ngọc Tú", "Phó Giám đốc", "Ban Giám đốc"),
             ("Nguyễn Thị Thu Thuỷ", "Trưởng phòng", "Tổng hợp"),
             ("Phan Duy Toàn", "Phó phòng", "Tổng hợp"),
             ("Trần Vân Thủy", "Phó phòng", "Tổng hợp"),
             ("Nguyễn Văn Khuê", "Phó phòng", "Tổng hợp"),
             ("Nguyễn Anh Tuyên", "Cán bộ", "Tổng hợp"),
             ("Bùi Thị Thúy Hà", "Cán bộ", "Tổng hợp"),
             ("Đặng Quang Hưng", "Cán bộ", "Tổng hợp"),
             ("Trần Thị Bích Ngọc", "Cán bộ", "Tổng hợp"),
             ("Phạm Đức Quý", "Cán bộ", "Tổng hợp"),
             ("Vũ Thị Tuyết Mai", "Cán bộ", "Tổng hợp"),
             ("Nguyễn Thị Hồng Liên", "Trưởng phòng", "Phát hành thẻ"),
             ("Bùi Đình Cương", "Phó phòng", "Phát hành thẻ"),
             ("Phạm Ngọc Thơ", "Phó phòng", "Phát hành thẻ"),
             ("Nguyễn Thị Mai Phương", "Phó phòng", "Phát hành thẻ"),
             ("Đinh Thị Thúy", "Cán bộ", "Phát hành thẻ"),
             ("Nguyễn Thị Tố Uyên", "Cán bộ", "Phát hành thẻ"),
             ("Nguyễn Thị Hương Lan", "Cán bộ", "Phát hành thẻ"),
             ("Đoàn Thị Thanh", "Cán bộ", "Phát hành thẻ"),
             ("Tô Lan Hương", "Cán bộ", "Phát hành thẻ"),
             ("Vũ Đức Trung", "Cán bộ", "Phát hành thẻ"),
             ("Hồ Thị Loan", "Cán bộ", "Phát hành thẻ"),
             ("Bùi Thị Mến", "Trưởng phòng", "Kế toán"),
             ("Nguyễn Bá Nhiệm", "Phó phòng", "Kế toán"),
             ("Đỗ Thị Thanh Thuỷ", "Phó phòng", "Kế toán"),
             ("Lê Thanh Loan", "Phó phòng", "Kế toán"),
             ("Nguyễn Thị Thanh Hương", "Cán bộ", "Kế toán"),
             ("Bùi Thị Hoài Thương", "Cán bộ", "Kế toán"),
             ("Lê Hương Giang", "Cán bộ", "Kế toán"),
             ("Hà Thị Ngân", "Cán bộ", "Kế toán"),
             ("Hoàng Việt Cường", "Trưởng phòng", "Quản lý rủi ro"),
             ("Nguyễn Xuân Hiếu", "Phó phòng", "Quản lý rủi ro"),
             ("Phạm Thị Thu Thủy", "Phó phòng", "Quản lý rủi ro"),
             ("Nguyễn Thị Phương Nga", "Phó phòng", "Quản lý rủi ro"),
             ("Vũ Hồng Ngọc", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Tùng Lâm", "Cán bộ", "Quản lý rủi ro"),
             ("Dương Thị Thùy Giang", "Cán bộ", "Quản lý rủi ro"),
             ("Trịnh Ngọc Minh", "Cán bộ", "Quản lý rủi ro"),
             ("Trịnh Thu Hương", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Thị Thùy Trang", "Cán bộ", "Quản lý rủi ro"),
             ("Ngô Thị Thu Hương", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Ngọc Thúy", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Hoài Phương", "Cán bộ", "Quản lý rủi ro"),
             ("Lương Minh Hiếu", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Diệu Linh", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Thị Thùy Trang", "Cán bộ", "Quản lý rủi ro"),
             ("Lê Mỹ Hạnh", "Cán bộ", "Quản lý rủi ro"),
             ("Nguyễn Quý Hợi", "Trưởng phòng", "Nghiên cứu và Phát triển"),
             ("Nguyễn Thị Mai Yên", "Phó phòng", "Nghiên cứu và Phát triển"),
             ("Trần Hồng Nhung", "Phó phòng", "Nghiên cứu và Phát triển"),
             ("Nguyễn Lan Anh", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Nguyễn Thế Anh", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Đỗ Thị Tuyết Minh", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Nguyễn Tuấn Hân", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Nguyễn Thị Như Quỳnh", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Vũ Phương Thảo", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Tô Thùy Linh", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Nguyễn Ngọc Quỳnh", "Cán bộ", "Nghiên cứu và Phát triển"),
             ("Hoàng Thị Thu Hiền", "Trưởng phòng", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Thị Quỳnh Trang", "Phó phòng", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Thanh Tùng", "Phó phòng", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Thị Thuý Loan", "Phó phòng", "Vận hành nghiệp vụ thẻ"),
             ("Vũ Thị Lan Anh", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Thị Xuân Tuyến", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Vũ Thị Hà", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Đinh Công Khánh", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Trần Thị Thu Huyền", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Vũ Thị Minh Phương", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Hoàng Mai", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Thị Thúy Trinh", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Hoàng Thị Thu Hường", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Hải Yến", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Lê Minh Thu", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Đỗ Thị Thu Hương", "Cán bộ", "Vận hành nghiệp vụ thẻ"),
             ("Nguyễn Tiến Thành", "Trưởng phòng", "Kỹ thuật"),
             ("Lê Hoàng Nhâm", "Phó phòng", "Kỹ thuật"),
             ("Khổng Minh Thảo", "Phó phòng", "Kỹ thuật"),
             ("Nguyễn Thị Cẩm Thơ", "Phó phòng", "Kỹ thuật"),
             ("Dương Cường Anh", "Cán bộ", "Kỹ thuật"),
             ("Nguyễn Thị Hương", "Cán bộ", "Kỹ thuật"),
             ("Trần Thu Trang", "Cán bộ", "Kỹ thuật"),
             ("Nguyễn Trung Hậu", "Cán bộ", "Kỹ thuật"),
             ("Vũ Thái Bằng", "Cán bộ", "Kỹ thuật"),
             ("Lê Mạnh Cường", "Cán bộ", "Kỹ thuật"),
             ("Phạm Thanh Tùng", "Cán bộ", "Kỹ thuật"),
             ("Phạm Thanh Đông", "Cán bộ", "Kỹ thuật"),
             ("Trần Thị Hằng", "Cán bộ", "Kỹ thuật"),
             ("Vũ Vân Giang", "Cán bộ", "Kỹ thuật"),
             ("Luyện Văn Thao", "Cán bộ", "Kỹ thuật"),
             ("Vũ Hà Long", "Cán bộ", "Kỹ thuật"),
             ("Nguyễn Phú Lâm", "Cán bộ", "Kỹ thuật"),
             ("Nguyễn Quốc Việt", "Cán bộ", "Kỹ thuật"),
             ("Vũ Duy Đông", "Cán bộ", "Kỹ thuật"),
             ("Hà Công Trung", "Cán bộ", "Kỹ thuật"),
             ("Nguyễn Thị Diễm Hằng", "Trưởng phòng", "Thanh toán thẻ"),
             ("Lê Thị Mỹ", "Phó phòng", "Thanh toán thẻ"),
             ("Trần Thị Huyền Trâm", "Phó phòng", "Thanh toán thẻ"),
             ("Nguyễn Hải Hà", "Phó phòng", "Thanh toán thẻ"),
             ("Vũ Thị Khánh Hưng", "Cán bộ", "Thanh toán thẻ"),
             ("Nguyễn Thị Tuyết", "Cán bộ", "Thanh toán thẻ"),
             ("Lã Thị Hương Giang", "Cán bộ", "Thanh toán thẻ"),
             ("Phạm Thị Quyên", "Cán bộ", "Thanh toán thẻ"),
             ("Nguyễn Thị Chinh Lương", "Cán bộ", "Thanh toán thẻ"),
             ("Bùi Thị Hương Lan", "Cán bộ", "Thanh toán thẻ"),
             ("Hoàng Thị Hằng", "Cán bộ", "Thanh toán thẻ"),
             ("Ngô Thị Hồng Vân", "Cán bộ", "Thanh toán thẻ"),
             ("Đặng Ngọc Trâm", "Cán bộ", "Thanh toán thẻ"),
             ("Nguyễn Thị Thanh Huyền", "Cán bộ", "Thanh toán thẻ"),
             ("Trương Thị Ngọc Tú", "Cán bộ", "Thanh toán thẻ"),
             ("Nguyễn Thượng Hiền", "Cán bộ", "Thanh toán thẻ"),
             ("Phạm Mạnh Quý", "Cán bộ", "Thanh toán thẻ"),
             ("Phạm Thị Hương Thảo", "Cán bộ", "Thanh toán thẻ"),
             ("Nguyễn Mạnh Hùng", "Trưởng phòng", "Kiểm soát nội bộ"),
             ("Điêu Văn Đông", "Phó phòng", "Kiểm soát nội bộ"),
             ("Nguyễn Hùng Cường", "Phó phòng", "Kiểm soát nội bộ"),
             ("Đặng Văn Nghĩa", "Phó phòng", "Kiểm soát nội bộ"),
             ("Lại Thị Xuân", "Cán bộ", "Kiểm soát nội bộ"),
             ("Phạm Đình Hải", "Cán bộ", "Kiểm soát nội bộ"),
             ("Nguyễn Tuấn Quang", "Cán bộ", "Kiểm soát nội bộ"),
             ("Vũ Thị Nguyệt", "Cán bộ", "Kiểm soát nội bộ"))

        from django.conf import settings

        aa = []
        for i in a:
            t, _ = Title.objects.get_or_create(name=i[1])
            p, _ = PhongBan.objects.get_or_create(name=i[2])
            alphabet = string.ascii_letters + string.digits
            username = ''.join(secrets.choice(alphabet) for i in range(20))
            u = User()
            u.full_name = i[0]
            u.title = t
            u.phongban = p
            u.username = settings.USER_IMPORT_PREFIX + username
            aa.append(u)

        User.objects.bulk_create(aa)

        User.objects.create_superuser(
            full_name="a van min",
            username="admin",
            email="admin@gmail.com",
            password="admin123",
            phongban=PhongBan.objects.last(),
            title=Title.objects.last())

        a = ("ĐẢNG ỦY",
             "HỘI ĐỒNG THÀNH VIÊN",
             "BAN ĐIỀU HÀNH",
             "BAN KIỂM SOÁT",
             "BAN THƯ KÝ HỘI ĐỒNG THÀNH VIÊN",
             "PHÒNG TỔNG HỢP",
             "ỦY BAN NHÂN SỰ VÀ TỔ CHỨC ĐẢNG",
             "BAN KẾ HOẠCH NGUỒN VỐN",
             "BAN KIỂM TRA NỘI BỘ",
             "BAN TÀI CHÍNH KẾ TOÁN",
             "BAN TỔ CHỨC LAO ĐỘNG VÀ TIỀN LƯƠNG",
             "ỦY BAN ĐẦU TƯ",
             "BAN CỔ PHẦN HÓA",
             "BAN ĐẦU TƯ",
             "ỦY BAN CHÍNH SÁCH",
             "BAN NGHIÊN CỨU PHÁT TRIỂN SẢN PHẨM DỊCH VỤ",
             "BAN PHÁP CHẾ VÀ KIỂM SOÁT TUÂN THỦ",
             "ỦY BAN QUẢN LÝ RỦI RO",
             "VĂN PHÒNG TRỤ SỞ CHÍNH",
             "BAN ĐỊNH CHẾ TÀI CHÍNH",
             "BAN KHÁCH HÀNG HỘ SẢN XUẤT VÀ CÁ NHÂN",
             "BAN KHÁCH HÀNG LỚN",
             "BAN QUẢN LÝ TÀI SẢN PHÚC LỢI",
             "BAN QUẢN LÝ ĐẦU TƯ NỘI NGÀNH",
             "BAN QUẢN LÝ DỰ ÁN ĐẦU TƯ XÂY DỰNG KHU VỰC",
             "BAN TIỀN TỆ - KHO QUỸ",
             "VĂN PHÒNG ĐOÀN THANH NIÊN",
             "BAN TÍN DỤNG",
             "BAN THI ĐUA KHEN THƯỞNG",
             "BAN TRUYỀN THÔNG",
             "CƠ QUAN CÔNG ĐOÀN AGRIBANK",
             "TRUNG TÂM CHĂM SÓC, HỖ TRỢ KHÁCH HÀNG",
             "TRUNG TÂM DỊCH VỤ THANH TOÁN VÀ KIỀU HỐI",
             "TRUNG TÂM LƯU TRỮ",
             "TRUNG TÂM QUẢN LÝ RỦI RO",
             "TRUNG TÂM THANH TOÁN",
             "TRUNG TÂM VỐN",
             "TRUNG TÂM CÔNG NGHỆ THÔNG TIN",
             "TRUNG TÂM THẺ",
             "TRƯỜNG ĐÀO TẠO CÁN BỘ AGRIBANK")

        aa = []
        for i in a:
            n = NoiNhan(name=i.capitalize())
            aa.append(n)

        NoiNhan.objects.bulk_create(aa)

    def handle(self, *args, **options):
        self.create_bulk_users()

