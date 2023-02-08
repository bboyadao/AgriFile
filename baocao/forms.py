from django import forms
from django_select2.forms import ModelSelect2Widget, Select2Widget, Select2Mixin

from baocao.models import BaoCao
from setmeup.models import LichBaoCao


class CustomSelect(Select2Mixin, forms.widgets.Select):
    def __init__(self, attrs=None, choices=(), modify_choices=()):
        super(CustomSelect, self).__init__(attrs, choices=choices)
        self.modify_choices = modify_choices

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super(CustomSelect, self).create_option(name, value, label, selected, index, subindex, attrs)
        for pk, la, class_hell, in self.modify_choices:
            if value == pk:
                option['attrs']['class'] = f"bg-{class_hell}"
                option['attrs']['label'] = f"(#{pk})---{la}"
        return option


class BaoCaoForm(forms.ModelForm):
    file_field = forms.FileField(
        required=False, label="File đính kèm",
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }),
    )
    thoigian = forms.DateTimeField(
        label="Thời gian",
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.TextInput(
            attrs={
                'class': 'datetimepicker',
                "autocomplete": "off"
            }
        ))

    def __init__(self, *args, **kwargs):
        nof_instance = kwargs.pop('nof', None)
        if nof_instance:
            self.base_fields['nof'].initial = nof_instance
            queryset = LichBaoCao.objects.all()
            self.base_fields['nof'] = forms.ModelChoiceField(
                label="Thông báo:",
                initial=nof_instance, queryset=LichBaoCao.objects.all(),
                widget=CustomSelect(
                    modify_choices=tuple(
                        (i.pk, i.get_full_title, i.get_class_hell) for i in
                        queryset))
            )

        icons = getattr(self.Meta, 'icons', dict())
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if nof_instance and field_name == "nof":
                field.widget.attrs["disabled"] = True
                field.widget.attrs["readonly"] = "readonly"
                field.widget.attrs["pointer-events"] = ": none;"
                field.widget.attrs["class"] = f"form-control  bg-{nof_instance.get_class_hell} disabled color-palette"

            if field_name in icons:
                field.icon = icons[field_name]

    class Meta:
        model = BaoCao
        fields = [
            "nof",
            "name",
            "noidung",
            "nguoi_soan",
            "nguoi_duyet",
            "nguoi_ky",
            "phongban",
            "noinhan",
            "thoigian",
            "file_field",
            "note"
        ]

        labels = {
            "name": "Tên",
            'nof': "Lịch báo cáo",
            'file_field': "File đính kèm",
            "noidung": "Nội dung",
            "nguoi_duyet": "Người duyệt",
            "nguoi_ky": "Người Ký",
            "phongban": "Phòng ban",
            "noinhan": "Nơi nhận",
            "thoigian": "Thời gian",
            "nguoi_soan": "Người soạn",
            "note": "Ghi chú"
        }
        icons = {
            "thoigian": "far fa-clock"
        }
        widgets = {
            "nguoi_soan": Select2Widget(),
            "nguoi_duyet": Select2Widget(),
            "nguoi_ky": Select2Widget(),
            "noinhan": Select2Widget(),
            "nof": Select2Widget(),
            "note": forms.Textarea(
                attrs={
                    'class': 'input',
                    'placeholder': 'Ghi chú',
                    'background-color': '!important #fdf4d9',
                }
            )
        }
