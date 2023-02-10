# from django.utils import timezone
# from pandas import DataFrame
# TZ = timezone.get_current_timezone().key
#
# thongke_labels = [
# 		"ID", "Tên báo cáo", "Nội dung", "Ngày ký", "Phòng ban", "Người soạn", "Người duyệt", "Người ký", "Ngày gửi",
# 		"Phòng ban nhận"
# 	]
#
#
# def create_df(qs, labels)-> DataFrame:
#
#
#
#
# 	df = DataFrame(list(qs.values_list(*val_list)), columns=labels)
# 	return df
#
#
# qs = BaoCao.objects.all()
# qs.select_related('nguoi_soan', 'nguoi_ky', 'nguoi_duyet', 'phongban')
# 	val_list = (
# 		"pk", 'name', 'noidung', 'thoigian',
# 		'phongban__name', 'nguoi_soan__full_name', 'nguoi_duyet__full_name',
# 		'nguoi_ky__full_name', 'thoigian',
# 		'noinhan__name'
# 	)
# df = create_df(qs, labels=thongke_labels)
# df['Ngày ký'] = df['Ngày ký'].dt.tz_convert(TZ).dt.tz_localize(None)
# df['Ngày gửi'] = df['Ngày gửi'].dt.tz_convert(TZ).dt.tz_localize(None)
